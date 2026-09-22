# FasePlataforma

## Descrição

Monta uma fase narrativa a partir de `DefinicaoFase` e controla sua máquina
de estados, tentativa, flores, diálogos e transição.

## Localização

`src/cenas/fase_plataforma.py`

## Propriedades

### `definicao`

- Tipo: `DefinicaoFase`
- Valor inicial: informado na criação.
- Descrição: fornece layout, conteúdo e identidade visual.

### `jogadora`

- Tipo: `Jogadora | None`
- Valor inicial: `None`, preenchido em `entrar()`.
- Descrição: entidade controlada na fase.

### `flores` e `quantidade_coletada`

- Tipo: `list[Flor]` e `int`
- Valor inicial: lista vazia e zero.
- Descrição: representam os coletáveis ativos e a ordem narrativa.

### `estado_fase`

- Tipo: `EstadoFase`
- Valor inicial: `ABERTURA`.
- Descrição: determina se a cena trata diálogo, exploração ou transição.

## Métodos

### `entrar()`

- Objetivo: criar entidades, flores, fundo e abertura uma única vez.
- Parâmetros: nenhum.
- Retorno: nenhum.
- Efeito no jogo: prepara a tentativa conforme a definição.

### `atualizar(delta_tempo)`

- Objetivo: atualizar diálogo ou mundo e detectar coleta e queda.
- Parâmetros: tempo decorrido em segundos.
- Retorno: nenhum.
- Efeito no jogo: pode mudar o estado narrativo.

### `tratar_evento(evento)`

- Objetivo: isolar eventos de diálogo e exploração e tratar `R`.
- Parâmetros: evento do Pygame.
- Retorno: nenhum.
- Efeito no jogo: impede que `Enter` seja processado como movimento.

### `registrar_coleta(flor)`

- Objetivo: contar uma flor uma vez e selecionar a próxima mensagem.
- Parâmetros: flor em colisão.
- Retorno: mensagem selecionada ou `None`.
- Efeito no jogo: pausa o mundo e abre diálogo.

### `reiniciar_tentativa()`

- Objetivo: restaurar spawn, cinco flores e índice narrativo.
- Parâmetros: nenhum.
- Retorno: nenhum.
- Efeito no jogo: preserva a abertura já vista.

