# Plataforma

## Descrição

Representa uma superfície sólida e imóvel das fases básicas. O sprite da
plataforma não possui margens transparentes, de modo que a superfície visível
começa no topo da colisão. Usa um retângulo verde enquanto o sprite não existe.

## Localização

`src/entidades/plataforma.py`

## Propriedades

### `retangulo`

- Tipo: `pygame.Rect`
- Valor inicial: informado na criação.
- Descrição: define a posição, as dimensões e a área de colisão.

## Métodos

### `desenhar(superficie)`

- Objetivo: desenhar o sprite ou a forma temporária.
- Parâmetros: superfície de destino.
- Retorno: nenhum.
- Efeito no jogo: exibe a plataforma.
