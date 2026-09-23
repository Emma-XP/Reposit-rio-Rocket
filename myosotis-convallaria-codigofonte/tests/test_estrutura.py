"""Testes da infraestrutura de entidades, cenas e estado."""

import unittest

import pygame

from src.cenas.cena import Cena
from src.cenas.fase_plataforma import EstadoFase, FasePlataforma
from src.configuracao.fases import FASES
from src.configuracao.configuracoes import (
    ALTURA_JANELA,
    ALTURA_TELA,
    LARGURA_JANELA,
    LARGURA_TELA,
    RESOLUCAO_ATIVA,
    RESOLUCOES_SUPORTADAS,
)
from src.controlador_cenas import ControladorCenas
from src.entidades.entidade import Entidade
from src.entidades.jogadora import Jogadora
from src.entidades.plataforma import Plataforma
from src.estado_jogo import EstadoJogo


class EntidadeDeTeste(Entidade):
    """Registra chamadas recebidas durante os testes."""

    def __init__(self) -> None:
        super().__init__()
        self.atualizacoes = 0
        self.desenhos = 0
        self.eventos = 0

    def atualizar(self, delta_tempo: float) -> None:
        self.atualizacoes += 1

    def desenhar(self, superficie: pygame.Surface) -> None:
        self.desenhos += 1

    def tratar_evento(self, evento: pygame.event.Event) -> None:
        self.eventos += 1


class CenaDeTeste(Cena):
    """Registra entrada e saída para validar o controlador."""

    def __init__(self) -> None:
        super().__init__()
        self.entradas = 0
        self.saidas = 0

    def entrar(self) -> None:
        self.entradas += 1

    def sair(self) -> None:
        self.saidas += 1


class TesteCena(unittest.TestCase):
    def setUp(self) -> None:
        pygame.init()
        self.superficie = pygame.Surface((100, 100))

    def tearDown(self) -> None:
        pygame.quit()

    def test_aplica_adicao_e_remocao_ao_final_da_atualizacao(self) -> None:
        cena = Cena()
        entidade = EntidadeDeTeste()

        cena.adicionar_entidade(entidade)
        self.assertNotIn(entidade, cena.entidades)
        cena.atualizar(0.016)
        self.assertIn(entidade, cena.entidades)

        cena.remover_entidade(entidade)
        cena.atualizar(0.016)
        self.assertNotIn(entidade, cena.entidades)

    def test_respeita_estados_ativa_e_visivel(self) -> None:
        cena = Cena()
        entidade = EntidadeDeTeste()
        cena.adicionar_entidade(entidade)
        cena.atualizar(0.016)

        entidade.ativa = False
        entidade.visivel = False
        cena.tratar_evento(pygame.event.Event(pygame.USEREVENT))
        cena.atualizar(0.016)
        cena.desenhar(self.superficie)

        self.assertEqual(entidade.atualizacoes, 0)
        self.assertEqual(entidade.eventos, 0)
        self.assertEqual(entidade.desenhos, 0)


class TesteResolucao(unittest.TestCase):
    def test_oferece_as_duas_resolucoes_solicitadas(self) -> None:
        self.assertEqual(
            RESOLUCOES_SUPORTADAS,
            {
                "1920x1080": (1920, 1080),
                "1366x768": (1366, 768),
            },
        )
        self.assertEqual(
            (LARGURA_JANELA, ALTURA_JANELA),
            RESOLUCOES_SUPORTADAS[RESOLUCAO_ATIVA],
        )

    def test_area_logica_cobre_todo_o_layout_das_fases(self) -> None:
        self.assertEqual((LARGURA_TELA, ALTURA_TELA), (1920, 1080))
        for fase in FASES:
            for x, y, largura, altura in fase.plataformas:
                self.assertLessEqual(x + largura, LARGURA_TELA)
                self.assertLessEqual(y + altura, ALTURA_TELA)


class TesteControladorCenas(unittest.TestCase):
    def test_troca_chama_saida_e_entrada(self) -> None:
        controlador = ControladorCenas()
        primeira = CenaDeTeste()
        segunda = CenaDeTeste()

        controlador.trocar_cena(primeira)
        controlador.trocar_cena(segunda)

        self.assertEqual(primeira.entradas, 1)
        self.assertEqual(primeira.saidas, 1)
        self.assertEqual(segunda.entradas, 1)
        self.assertIs(controlador.cena_ativa, segunda)


class TesteEstadoJogo(unittest.TestCase):
    def test_armazena_dados_persistentes(self) -> None:
        estado = EstadoJogo()
        estado.registrar_progresso("exemplo", 1)
        estado.definir_configuracao("volume", 0.5)

        self.assertEqual(estado.progresso["exemplo"], 1)
        self.assertEqual(estado.configuracoes["volume"], 0.5)


class TesteJogadora(unittest.TestCase):
    def setUp(self) -> None:
        pygame.init()
        self.plataforma = Plataforma(pygame.Rect(0, 300, 600, 40))
        self.jogadora = Jogadora((100, 100), [self.plataforma])

    def tearDown(self) -> None:
        pygame.quit()

    def test_cai_e_para_sobre_plataforma(self) -> None:
        for _ in range(60):
            self.jogadora.atualizar(1 / 60)

        self.assertEqual(self.jogadora.retangulo.bottom, self.plataforma.retangulo.top)
        self.assertTrue(self.jogadora.no_chao)

    def test_responde_a_movimento_e_pulo(self) -> None:
        for _ in range(60):
            self.jogadora.atualizar(1 / 60)

        posicao_antes = self.jogadora.retangulo.x
        self.jogadora.tratar_evento(
            pygame.event.Event(pygame.KEYDOWN, key=pygame.K_d)
        )
        self.jogadora.tratar_evento(
            pygame.event.Event(pygame.KEYDOWN, key=pygame.K_SPACE)
        )
        self.jogadora.atualizar(1 / 60)

        self.assertGreater(self.jogadora.retangulo.x, posicao_antes)
        self.assertLess(self.jogadora.velocidade_vertical, 0)

    def test_reiniciar_restaura_posicao_e_velocidade(self) -> None:
        self.jogadora.velocidade_vertical = 200
        self.jogadora.retangulo.topleft = (400, 500)

        self.jogadora.reiniciar()

        self.assertEqual(self.jogadora.retangulo.topleft, (100, 100))
        self.assertEqual(self.jogadora.velocidade_vertical, 0)

    def test_pulo_solicitado_antes_de_aterrissar_nao_se_perde(self) -> None:
        self.jogadora.retangulo.bottom = self.plataforma.retangulo.top - 1
        self.jogadora._posicao_y = float(self.jogadora.retangulo.y)
        self.jogadora.velocidade_vertical = 120
        self.jogadora.tratar_evento(
            pygame.event.Event(pygame.KEYDOWN, key=pygame.K_SPACE)
        )

        self.jogadora.atualizar(1 / 60)

        self.assertEqual(
            self.jogadora.retangulo.bottom,
            self.plataforma.retangulo.top,
        )
        self.assertLess(self.jogadora.velocidade_vertical, 0)
        self.assertFalse(self.jogadora.no_chao)

    def test_permite_pular_logo_depois_de_sair_da_plataforma(self) -> None:
        for _ in range(60):
            self.jogadora.atualizar(1 / 60)

        self.jogadora.retangulo.left = self.plataforma.retangulo.right + 1
        self.jogadora._posicao_x = float(self.jogadora.retangulo.x)
        self.jogadora.atualizar(1 / 60)
        self.jogadora.tratar_evento(
            pygame.event.Event(pygame.KEYDOWN, key=pygame.K_SPACE)
        )
        self.jogadora.atualizar(1 / 60)

        self.assertLess(self.jogadora.velocidade_vertical, 0)

    def test_soltar_botao_reduz_altura_do_pulo(self) -> None:
        for _ in range(60):
            self.jogadora.atualizar(1 / 60)

        self.jogadora.tratar_evento(
            pygame.event.Event(pygame.KEYDOWN, key=pygame.K_SPACE)
        )
        self.jogadora.atualizar(1 / 60)
        velocidade_antes = self.jogadora.velocidade_vertical
        self.jogadora.tratar_evento(
            pygame.event.Event(pygame.KEYUP, key=pygame.K_SPACE)
        )

        self.assertGreater(self.jogadora.velocidade_vertical, velocidade_antes)
        self.assertLess(self.jogadora.velocidade_vertical, 0)

    def test_carrega_quadros_png_e_espelhamento_em_cache(self) -> None:
        quantidades = {
            estado: len(quadros)
            for estado, quadros in self.jogadora._quadros_direita.items()
        }
        self.assertEqual(
            quantidades,
            {
                "parada": 1,
                "caminhada": 3,
                "frente": 2,
                "costas": 3,
                "salto": 3,
                "queda": 2,
            },
        )
        for estado, quadros in self.jogadora._quadros_esquerda.items():
            for original, espelhado in zip(
                quadros, self.jogadora._quadros_direita[estado]
            ):
                self.assertEqual(original.get_size(), espelhado.get_size())
                self.assertTrue(original.get_flags() & pygame.SRCALPHA)

    def test_salto_e_queda_mantem_direcao_correta(self) -> None:
        originais = self.jogadora._carregar_quadros()
        for estado in ("salto", "queda"):
            esperado = pygame.image.tobytes(originais[estado][0], "RGBA")
            esperado_espelhado = pygame.image.tobytes(
                pygame.transform.flip(originais[estado][0], True, False), "RGBA"
            )
            direita = pygame.image.tobytes(
                self.jogadora._quadros_direita[estado][0], "RGBA"
            )
            esquerda = pygame.image.tobytes(
                self.jogadora._quadros_esquerda[estado][0], "RGBA"
            )
            self.assertEqual(direita, esperado)
            self.assertEqual(esquerda, esperado_espelhado)

        caminhada_original = pygame.image.tobytes(originais["caminhada"][0], "RGBA")
        caminhada_esquerda = pygame.image.tobytes(
            self.jogadora._quadros_esquerda["caminhada"][0], "RGBA"
        )
        self.assertEqual(caminhada_esquerda, caminhada_original)


class TesteFasePlataforma(unittest.TestCase):
    def setUp(self) -> None:
        pygame.init()

    def tearDown(self) -> None:
        pygame.quit()

    def test_conclui_uma_unica_vez_ao_alcancar_saida(self) -> None:
        conclusoes = []
        estado = EstadoJogo()
        estado.marcar_abertura_vista(FASES[0].id)
        fase = FasePlataforma(
            definicao=FASES[0],
            estado_jogo=estado,
            ao_concluir=lambda: conclusoes.append(True),
        )
        fase.entrar()
        fase.atualizar(0)
        for flor in tuple(fase.flores):
            fase.estado_fase = EstadoFase.EXPLORACAO
            fase.registrar_coleta(flor)
            fase.caixa_dialogo.quantidade_caracteres = len(
                fase.caixa_dialogo.fala_atual
            )
            fase.caixa_dialogo.tratar_evento(
                pygame.event.Event(pygame.KEYDOWN, key=pygame.K_RETURN)
            )
            fase.atualizar(0)
        fase.caixa_dialogo.quantidade_caracteres = len(
            fase.caixa_dialogo.fala_atual
        )
        fase.caixa_dialogo.tratar_evento(
            pygame.event.Event(pygame.KEYDOWN, key=pygame.K_RETURN)
        )
        fase.atualizar(0)
        fase.atualizar(0)
        self.assertEqual(conclusoes, [True])
        self.assertEqual(fase.progresso, 5)


if __name__ == "__main__":
    unittest.main()
