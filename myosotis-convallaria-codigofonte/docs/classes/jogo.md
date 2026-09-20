# Jogo

## Descrição

Inicializa o Pygame, cria a área lógica de 1920×1080 e executa o ciclo
principal na ordem definida pelo projeto. Cada quadro é ajustado à resolução
de janela selecionada nas configurações.

## Localização

`jogo.py`

## Propriedades

### `controlador_cenas`

- Tipo: `ControladorCenas`
- Valor inicial: controlador seguido da primeira fase.
- Descrição: encaminha eventos, atualização e desenho à cena ativa.

### `estado`

- Tipo: `EstadoJogo`
- Valor inicial: estado vazio.
- Descrição: mantém progresso em memória separado das cenas.

### `janela`

- Tipo: `pygame.Surface`
- Valor inicial: resolução indicada por `RESOLUCAO_ATIVA`.
- Descrição: superfície visível que recebe o quadro ajustado.

### `superficie`

- Tipo: `pygame.Surface`
- Valor inicial: área lógica de 1920×1080.
- Descrição: superfície na qual a cena ativa é desenhada.

## Métodos

### `executar(limite_quadros=None)`

- Objetivo: processar os quadros do jogo.
- Parâmetros: limite opcional para verificações automatizadas.
- Retorno: nenhum.
- Efeito no jogo: recebe eventos, atualiza, desenha e exibe.

### `encerrar()`

- Objetivo: finalizar cena e Pygame com segurança.
- Parâmetros: nenhum.
- Retorno: nenhum.
- Efeito no jogo: encerra a execução.

### `_exibir_quadro()`

- Objetivo: ajustar a área lógica ao tamanho da janela.
- Parâmetros: nenhum.
- Retorno: nenhum.
- Efeito no jogo: copia ou redimensiona o quadro antes da exibição.

### `_iniciar_fase(indice)`

- Objetivo: criar uma fase orientada a dados ou a conclusão.
- Parâmetros: índice da definição.
- Retorno: nenhum.
- Efeito no jogo: troca a única cena ativa.

### `_concluir_fase(indice)`

- Objetivo: registrar conclusão e avançar.
- Parâmetros: índice concluído.
- Retorno: nenhum.
- Efeito no jogo: abre a próxima fase ou conclusão.

### `_reiniciar_jogo()`

- Objetivo: limpar o estado em memória e voltar à infância.
- Parâmetros: nenhum.
- Retorno: nenhum.
- Efeito no jogo: inicia uma nova execução.
