"""Testes das regras narrativas e da progressão da experiência."""

import unittest

import pygame

from src.cenas.fase_plataforma import EstadoFase, FasePlataforma
from src.configuracao.fases import FASES, DefinicaoFase
from src.entidades.flor import Flor
from src.estado_jogo import EstadoJogo
from src.interface.caixa_dialogo import CaixaDialogo


class TesteDefinicoesFase(unittest.TestCase):
    def test_tres_fases_respeitam_limites_de_conteudo(self) -> None:
        self.assertEqual(len(FASES), 3)
        for fase in FASES:
            self.assertEqual(len(fase.posicoes_flores), 5)
            self.assertEqual(len(fase.mensagens_flores), 5)
            self.assertLessEqual(len(fase.dialogo_abertura), 3)
            self.assertLessEqual(len(fase.dialogo_encerramento), 2)

    def test_flores_estao_apoiadas_e_percurso_tem_saltos_tolerantes(self) -> None:
        for fase in FASES:
            for x, y in fase.posicoes_flores:
                self.assertTrue(
                    any(
                        px <= x <= px + largura and y + 54 == py
                        for px, py, largura, _ in fase.plataformas
                    )
                )
            for atual, proxima in zip(fase.plataformas, fase.plataformas[1:]):
                borda_atual = atual[0] + atual[2]
                self.assertLessEqual(proxima[0] - borda_atual, 100)
                self.assertLessEqual(atual[1] - proxima[1], 140)

    def test_rejeita_quantidade_invalida_de_flores(self) -> None:
        dados = dict(FASES[0].__dict__)
        dados["posicoes_flores"] = ((0, 0),)
        with self.assertRaises(ValueError):
            DefinicaoFase(**dados)


class TesteCaixaDialogo(unittest.TestCase):
    def setUp(self) -> None:
        pygame.init()

    def tearDown(self) -> None:
        pygame.quit()

    def test_enter_primeiro_completa_e_depois_fecha(self) -> None:
        caixa = CaixaDialogo(("Uma frase curta.",), velocidade_texto=1)
        enter = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_RETURN)
        caixa.tratar_evento(enter)
        self.assertTrue(caixa.fala_completa)
        self.assertFalse(caixa.concluido)
        caixa.tratar_evento(enter)
        self.assertTrue(caixa.concluido)

    def test_revelacao_depende_do_tempo(self) -> None:
        caixa = CaixaDialogo(("abcdefghij",), velocidade_texto=5)
        caixa.atualizar(1)
        self.assertEqual(int(caixa.quantidade_caracteres), 5)


class TesteFlor(unittest.TestCase):
    def setUp(self) -> None:
        pygame.init()

    def tearDown(self) -> None:
        pygame.quit()

    def test_nao_pode_ser_coletada_duas_vezes(self) -> None:
        flor = Flor((0, 0))
        self.assertTrue(flor.coletar())
        self.assertFalse(flor.coletar())


class TesteProgressaoFase(unittest.TestCase):
    def setUp(self) -> None:
        pygame.init()
        self.estado = EstadoJogo()
        self.estado.marcar_abertura_vista(FASES[0].id)
        self.conclusoes = 0
        self.fase = FasePlataforma(
            FASES[0], self.estado, self._registrar_conclusao
        )
        self.fase.entrar()
        self.fase.atualizar(0)

    def tearDown(self) -> None:
        pygame.quit()

    def _registrar_conclusao(self) -> None:
        self.conclusoes += 1

    def _fechar_dialogo(self) -> None:
        assert self.fase.caixa_dialogo is not None
        enter = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_RETURN)
        self.fase.caixa_dialogo.tratar_evento(enter)
        self.fase.caixa_dialogo.tratar_evento(enter)
        self.fase.atualizar(0)

    def test_coletas_seguem_indice_e_quinta_abre_encerramento(self) -> None:
        primeira = self.fase.registrar_coleta(self.fase.flores[-1])
        self.assertEqual(primeira, FASES[0].mensagens_flores[0])
        self._fechar_dialogo()
        for indice in range(1, 5):
            mensagem = self.fase.registrar_coleta(self.fase.flores[0])
            self.assertEqual(mensagem, FASES[0].mensagens_flores[indice])
            self._fechar_dialogo()
        self.assertEqual(self.fase.estado_fase, EstadoFase.ENCERRAMENTO)
        self.assertEqual(self.conclusoes, 0)

    def test_reinicio_zera_tentativa_e_preserva_abertura(self) -> None:
        self.fase.registrar_coleta(self.fase.flores[0])
        self.fase.reiniciar_tentativa()
        self.assertEqual(self.fase.quantidade_coletada, 0)
        self.assertEqual(len(self.fase.flores), 5)
        self.assertEqual(self.fase.estado_fase, EstadoFase.EXPLORACAO)
        self.assertTrue(self.estado.abertura_foi_vista(FASES[0].id))

    def test_dialogo_pausa_fisica_e_ignora_movimento(self) -> None:
        self.fase.estado_fase = EstadoFase.MENSAGEM_FLOR
        self.fase._abrir_dialogo(("Pausa.",), EstadoFase.MENSAGEM_FLOR)
        posicao = self.fase.jogadora.retangulo.topleft
        self.fase.tratar_evento(
            pygame.event.Event(pygame.KEYDOWN, key=pygame.K_d)
        )
        self.fase.atualizar(1)
        self.assertEqual(self.fase.jogadora.retangulo.topleft, posicao)
        self.assertEqual(self.fase.jogadora.velocidade_vertical, 0)

    def test_queda_reinicia_toda_a_tentativa(self) -> None:
        self.fase.registrar_coleta(self.fase.flores[0])
        self.fase.reiniciar_tentativa()
        self.fase.registrar_coleta(self.fase.flores[0])
        self._fechar_dialogo()
        self.fase.jogadora.retangulo.top = 1300
        self.fase.jogadora._posicao_y = 1300.0
        self.fase.atualizar(0)
        self.assertEqual(self.fase.quantidade_coletada, 0)
        self.assertEqual(len(self.fase.flores), 5)
        self.assertEqual(
            self.fase.jogadora.retangulo.topleft,
            self.fase.definicao.spawn_jogadora,
        )

    def test_encerramento_solicita_transicao_uma_vez(self) -> None:
        self.fase.quantidade_coletada = 5
        self.fase._abrir_dialogo(
            self.fase.definicao.dialogo_encerramento, EstadoFase.ENCERRAMENTO
        )
        while self.fase.caixa_dialogo is not None:
            self._fechar_dialogo()
        self.fase.atualizar(0)
        self.assertEqual(self.conclusoes, 1)


class TesteEstadoExecucao(unittest.TestCase):
    def test_reinicio_final_limpa_todo_progresso(self) -> None:
        estado = EstadoJogo()
        estado.marcar_abertura_vista("infancia")
        estado.concluir_fase("infancia", 1)
        estado.concluir_jogo()
        estado.reiniciar_execucao()
        self.assertEqual(estado.indice_fase_atual, 0)
        self.assertFalse(estado.aberturas_vistas)
        self.assertFalse(estado.fases_concluidas)
        self.assertFalse(estado.jogo_concluido)


if __name__ == "__main__":
    unittest.main()
