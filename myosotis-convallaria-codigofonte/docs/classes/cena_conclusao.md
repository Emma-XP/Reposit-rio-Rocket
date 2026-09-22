# CenaConclusao

## Descrição

Conclui a trajetória de Diana dentro da história e oferece o reinício integral
da experiência.

## Localização

`src/cenas/cena_conclusao.py`

## Propriedades

### `ao_reiniciar`

- Tipo: `Callable[[], None]`
- Valor inicial: função informada na criação.
- Descrição: limpa o estado e volta à primeira fase.

### `_reinicio_solicitado`

- Tipo: `bool`
- Valor inicial: `False`.
- Descrição: impede duas solicitações de reinício.

## Métodos

### `entrar()`

- Objetivo: preparar os textos finais.
- Parâmetros: nenhum.
- Retorno: nenhum.
- Efeito no jogo: agenda os textos para inclusão.

### `tratar_evento(evento)`

- Objetivo: reconhecer `Enter` uma única vez.
- Parâmetros: evento do Pygame.
- Retorno: nenhum.
- Efeito no jogo: solicita uma nova execução.

