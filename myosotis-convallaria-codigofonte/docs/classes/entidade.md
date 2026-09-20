# Entidade

## Descrição

Define o contrato comum para qualquer objeto pertencente a uma cena.

## Localização

`src/entidades/entidade.py`

## Propriedades

### `ativa`

- Tipo: `bool`
- Valor inicial: `True`
- Descrição: indica se a entidade deve receber eventos e atualizações.

### `visivel`

- Tipo: `bool`
- Valor inicial: `True`
- Descrição: indica se a entidade deve ser desenhada.

## Métodos

### `atualizar(delta_tempo)`

- Objetivo: atualizar o estado próprio da entidade.
- Parâmetros: tempo em segundos desde o quadro anterior.
- Retorno: nenhum.
- Efeito no jogo: depende da implementação especializada.

### `desenhar(superficie)`

- Objetivo: desenhar a representação sem alterar estado.
- Parâmetros: superfície de destino do Pygame.
- Retorno: nenhum.
- Efeito no jogo: apresenta visualmente a entidade.

### `tratar_evento(evento)`

- Objetivo: receber uma entrada do Pygame.
- Parâmetros: evento recebido.
- Retorno: nenhum.
- Efeito no jogo: depende da implementação especializada.
