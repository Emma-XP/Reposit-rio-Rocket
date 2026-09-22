AGENT.md — Myosotis convallaria
1. Projeto

Myosotis convallaria é um jogo educativo desenvolvido em Python com Pygame para a Semana Nacional de Ciência e Tecnologia (SNCT), com o tema “Mulheres na Ciência”.

A proposta completa do jogo ainda será definida. Até lá:

Não invente histórias, mecânicas, personagens, fases ou informações científicas sem aprovação.
Como os sprites ainda não existem, represente as entidades com formas simples, como círculos e retângulos, implemente um arquivo com os paths, que substituiram as figuras geometricas futuramente e deixe tudo pronto para que isso seja simples e rapido de implementar
2. Regras de desenvolvimento
Escreva todo o código e a documentação em português do Brasil.
Prefira soluções simples, legíveis e fáceis de explicar.
Cada classe deve possuir uma responsabilidade principal.
Mantenha cada classe, sempre que possível, em seu próprio arquivo.
Use métodos pequenos e nomes claros.
Não adicione bibliotecas sem necessidade e justificativa.
Não altere partes do projeto que não estejam relacionadas à tarefa atual.
Coloque valores reutilizados em constantes ou configurações.
Antes de concluir uma mudança, execute o jogo e verifique se não há erros.
Padrão de nomes
Classes: PascalCase, como Jogadora e TelaInicial.
Variáveis, funções e métodos: snake_case, como velocidade_x.
Constantes: letras maiúsculas, como LARGURA_TELA e FPS.
Arquivos: snake_case, como tela_inicial.py.
3. Arquitetura do jogo

A arquitetura deve ser baseada em entidades, cenas e fases.

Entidade

Uma entidade é qualquer objeto que existe dentro de uma cena, como personagens, obstáculos, itens, botões, textos e efeitos.

Toda entidade deve possuir:

atualizar(delta_tempo): atualiza seu estado e comportamento.
desenhar(superficie): desenha sua representação.
tratar_evento(evento): recebe entradas quando necessário.
ativa: indica se deve ser atualizada.
visivel: indica se deve ser desenhada.

A entidade deve controlar apenas o próprio estado. Ela não deve trocar cenas diretamente, mas pode informar à cena que algum evento ocorreu.

Cena

Uma cena representa uma tela ou estado do jogo, como menu, fase, pausa, créditos ou resultado.

Cada cena possui e controla suas próprias entidades. Em cada quadro, a cena ativa deve:

Tratar os eventos.
Atualizar as entidades ativas.
Limpar o fundo.
Desenhar as entidades visíveis.
Remover entidades que não serão mais usadas.

Toda cena deve possuir:

entrar(): prepara a cena.
sair(): encerra ou libera seus recursos.
tratar_evento(evento): trata e distribui eventos.
atualizar(delta_tempo): atualiza a cena e suas entidades.
desenhar(superficie): desenha a cena e suas entidades.
adicionar_entidade(entidade): adiciona uma entidade.
remover_entidade(entidade): agenda a remoção de uma entidade.

A atualização deve acontecer antes do desenho. O método desenhar() não deve alterar o estado do jogo.

Entidades não devem ser adicionadas ou removidas enquanto a lista estiver sendo percorrida. Essas alterações devem ser aplicadas ao final da atualização.

Fase

Uma fase é uma cena especializada que pode controlar:

Objetivo e progresso.
Condições de vitória ou derrota.
Cenário e limites do mapa.
Personagens, itens, obstáculos e desafios.
Transição para outra fase ou cena.

Menus, créditos e pausa são cenas, mas não são fases.

Controle de cenas

O jogo deve possuir um controlador que mantenha apenas uma cena ativa.

Fluxo principal:

receber eventos → atualizar cena → desenhar cena → exibir quadro

Ao trocar de cena, o controlador deve chamar sair() na cena atual e entrar() na próxima.

Dados persistentes, como progresso e configurações, devem ficar em um objeto próprio de estado do jogo, evitando variáveis globais.

4. Estrutura sugerida
myosotis-convallaria/
├── jogo.py
├── assets/
│   ├── imagens/
│   ├── sons/
│   └── fontes/
├── src/
│   ├── cenas/
│   ├── entidades/
│   ├── interface/
│   └── configuracao/
├── docs/
│   ├── visao-geral.md
│   └── classes/
└── tests/

A estrutura poderá ser ajustada quando a proposta do jogo estiver completa.

5. Classes e documentação

Cada classe deve possuir:

Arquivo Python próprio, quando possível.
Uma docstring com sua finalidade.
Nomes claros para propriedades e métodos.
Um arquivo correspondente em docs/classes/.

Exemplo:

src/entidades/jogadora.py
docs/classes/jogadora.md

Modelo da documentação:

# NomeDaClasse

## Descrição

Explique brevemente a responsabilidade da classe.

## Localização

`src/caminho/arquivo.py`

## Propriedades

### `nome`

- Tipo:
- Valor inicial:
- Descrição:

## Métodos

### `nome(parametros)`

- Objetivo:
- Parâmetros:
- Retorno:
- Efeito no jogo:

Atualize a documentação quando classes, propriedades importantes, métodos públicos, controles ou regras forem alterados.

6. Commits

Cada commit deve conter uma mudança pequena e completa.

Formato:

tipo: descrição curta

Exemplos:

feat: adiciona cena inicial
fix: corrige movimento da jogadora
docs: documenta classe Fase

Use mensagens em português e confirme que o jogo funciona antes do commit.

7. Checklist final

Antes de concluir uma tarefa, verifique:

 O código está simples e legível.
 O jogo inicia sem erros.
 A mudança funciona corretamente.
 Não existem dados pessoais, senhas ou chaves no projeto.
 A documentação foi atualizada.
 Classes novas possuem documentação própria.
 O commit segue o padrão definido.