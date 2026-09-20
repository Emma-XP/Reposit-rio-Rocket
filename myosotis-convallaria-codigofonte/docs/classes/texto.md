# Texto

## Descrição

Renderiza uma linha de texto centralizada em uma posição.

## Localização

`src/entidades/texto.py`

## Propriedades

### `conteudo`

- Tipo: `str`
- Valor inicial: informado na criação.
- Descrição: texto apresentado.

### `posicao`

- Tipo: `tuple[int, int]`
- Valor inicial: informado na criação.
- Descrição: centro do texto na superfície.

### `caminho_fonte`

- Tipo: `Path | None`
- Valor inicial: `None`
- Descrição: fonte personalizada; usa a fonte padrão quando ausente.

## Métodos

### `desenhar(superficie)`

- Objetivo: renderizar e posicionar o texto.
- Parâmetros: superfície de destino do Pygame.
- Retorno: nenhum.
- Efeito no jogo: apresenta uma linha de texto.
