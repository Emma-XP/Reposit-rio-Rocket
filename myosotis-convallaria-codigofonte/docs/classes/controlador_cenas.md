# ControladorCenas

## Descrição

Mantém uma única cena ativa e encaminha a ela o ciclo do jogo.

## Localização

`src/controlador_cenas.py`

## Propriedades

### `cena_ativa`

- Tipo: `Cena | None`
- Valor inicial: `None`.
- Descrição: cena que recebe eventos, atualização e desenho.

## Métodos

### `trocar_cena(proxima_cena)`

- Objetivo: substituir a cena atual.
- Parâmetros: próxima cena.
- Retorno: nenhum.
- Efeito no jogo: chama `sair()` na anterior e `entrar()` na próxima.

### `tratar_evento(evento)`, `atualizar(delta_tempo)` e `desenhar(superficie)`

- Objetivo: encaminhar cada etapa do quadro.
- Parâmetros: o dado correspondente à etapa.
- Retorno: nenhum.
- Efeito no jogo: executa a etapa na cena ativa.

### `encerrar()`

- Objetivo: encerrar e remover a cena ativa.
- Parâmetros: nenhum.
- Retorno: nenhum.
- Efeito no jogo: chama `sair()` e limpa a referência.
