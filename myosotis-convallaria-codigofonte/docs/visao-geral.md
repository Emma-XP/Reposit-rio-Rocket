# Visão geral

Myosotis convallaria é um jogo narrativo de plataforma em Python com Pygame,
desenvolvido para a Semana Nacional de Ciência e Tecnologia (SNCT), com o tema
“Mulheres na Ciência”. A experiência acompanha Diana na infância, adolescência
e vida adulta.

## Arquitetura

O fluxo de cada quadro é receber eventos, atualizar a única cena ativa,
desenhar e exibir o quadro. `ControladorCenas` realiza as trocas, chamando
`sair()` e `entrar()`. `EstadoJogo` conserva somente o progresso da execução
atual, sem arquivos de save.

As três fases usam a mesma classe `FasePlataforma`. Layouts, textos, idade,
paleta e caminhos de fundo vêm das instâncias imutáveis de `DefinicaoFase` em
`src/configuracao/fases.py`.

As cenas são desenhadas em uma área lógica de 1920×1080. Antes de exibir cada
quadro, `Jogo` ajusta essa área para a janela configurada como 1920×1080 ou
1366×768. A opção `RESOLUCAO_ATIVA`, em
`src/configuracao/configuracoes.py`, alterna entre os dois tamanhos sem mudar
o campo de visão, as posições ou as colisões.

```text
ABERTURA -> EXPLORACAO -> MENSAGEM_FLOR -> EXPLORACAO
                                      \-> ENCERRAMENTO -> TRANSICAO
```

Durante qualquer diálogo, física e controles do mundo ficam pausados. A quinta
mensagem abre o encerramento; ele conduz à próxima fase ou à conclusão.

## Tentativa e progressão

Cada fase possui exatamente cinco flores. A mensagem depende da ordem de
coleta, nunca da posição. Uma queda ou `R` restaura spawn, velocidades, flores
e índice narrativo. A abertura, mantida no `EstadoJogo`, não se repete nessa
fase. O reinício da conclusão limpa toda a execução.

## Animação e recursos

Diana possui estados de parada, caminhada, salto e queda. Cada idade espera
dois, quatro, um e um quadros, respectivamente. A direção esquerda é criada
por espelhamento em cache. A colisão conserva sempre o mesmo retângulo.

Todos os caminhos ficam em `src/configuracao/caminhos.py`. Se imagens ou fonte
não existirem, o jogo usa formas geométricas e quadros procedurais. Não há
áudio externo nesta versão.

## Controles

- `A`/`D` ou setas: movimento;
- `W`, seta para cima ou espaço: pulo;
- `Enter`: completar ou avançar diálogo;
- `R`: reiniciar a tentativa durante a exploração.

Não há contador de flores na interface.
