# Flor

## Descrição

Entidade coletável responsável somente por posição, colisão, desenho e pelo
registro local de coleta.

## Localização

`src/entidades/flor.py`

## Propriedades

### `coletada`

- Tipo: `bool`
- Valor inicial: `False`.
- Descrição: impede que a mesma flor seja contada duas vezes.

## Métodos

### `coletar()`

- Objetivo: marcar uma coleta inédita.
- Parâmetros: nenhum.
- Retorno: `True` somente na primeira chamada.
- Efeito no jogo: desativa e oculta a flor.

### `desenhar(superficie)`

- Objetivo: desenhar imagem ou fallback geométrico.
- Parâmetros: superfície do Pygame.
- Retorno: nenhum.
- Efeito no jogo: nenhum; desenho não altera estado.
