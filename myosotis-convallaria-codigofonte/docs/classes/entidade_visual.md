# EntidadeVisual

## Descrição

Desenha um sprite configurado ou uma forma geométrica enquanto o sprite não
existe.

## Localização

`src/entidades/entidade_visual.py`

## Propriedades

### `retangulo`

- Tipo: `pygame.Rect`
- Valor inicial: informado na criação.
- Descrição: posição e tamanho da representação.

### `caminho_imagem`

- Tipo: `Path | None`
- Valor inicial: `None`
- Descrição: arquivo que substitui automaticamente a forma temporária.

### `forma`

- Tipo: `str`
- Valor inicial: `"retangulo"`
- Descrição: forma temporária; aceita `"retangulo"` ou `"circulo"`.

## Métodos

### `desenhar(superficie)`

- Objetivo: exibir a imagem ou a forma temporária.
- Parâmetros: superfície de destino do Pygame.
- Retorno: nenhum.
- Efeito no jogo: desenha a representação visual configurada.
