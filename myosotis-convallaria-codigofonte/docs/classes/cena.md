# Cena

## Descrição

Mantém entidades e organiza eventos, atualização e desenho de uma tela.

## Localização

`src/cenas/cena.py`

## Propriedades

### `entidades`

- Tipo: `list[Entidade]`
- Valor inicial: lista vazia.
- Descrição: entidades atualmente pertencentes à cena.

### `cor_fundo`

- Tipo: `tuple[int, int, int]`
- Valor inicial: `COR_FUNDO`.
- Descrição: cor usada para limpar a superfície.

## Métodos

### `entrar()`

- Objetivo: preparar a cena.
- Parâmetros: nenhum.
- Retorno: nenhum.
- Efeito no jogo: definido por cada cena especializada.

### `sair()`

- Objetivo: encerrar recursos da cena.
- Parâmetros: nenhum.
- Retorno: nenhum.
- Efeito no jogo: definido por cada cena especializada.

### `tratar_evento(evento)`

- Objetivo: distribuir uma entrada às entidades ativas.
- Parâmetros: evento do Pygame.
- Retorno: nenhum.
- Efeito no jogo: permite que entidades respondam à entrada.

### `atualizar(delta_tempo)`

- Objetivo: atualizar entidades e aplicar inclusões e remoções pendentes.
- Parâmetros: tempo em segundos desde o quadro anterior.
- Retorno: nenhum.
- Efeito no jogo: avança o estado da cena.

### `desenhar(superficie)`

- Objetivo: limpar o fundo e desenhar entidades visíveis.
- Parâmetros: superfície de destino.
- Retorno: nenhum.
- Efeito no jogo: compõe a imagem atual da cena.

### `adicionar_entidade(entidade)` e `remover_entidade(entidade)`

- Objetivo: agendar alteração segura na coleção.
- Parâmetros: entidade afetada.
- Retorno: nenhum.
- Efeito no jogo: aplica a alteração ao fim da atualização.
