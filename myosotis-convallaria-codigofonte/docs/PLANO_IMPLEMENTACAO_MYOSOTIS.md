# Plano de implementação — Myosotis convallaria

## 1. Objetivo deste plano

Este documento orienta um agente Codex a implementar, em uma game jam de 72 horas, a versão jogável completa de **Myosotis convallaria** sobre a base Pygame já existente.

O resultado esperado é uma experiência linear de aproximadamente 6 a 10 minutos, para público de 10 a 16 anos, composta por três fases curtas da vida de Diana. O jogo deve conscientizar sobre pressões sociais enfrentadas por mulheres exclusivamente por meio da trajetória da personagem, sem uma mensagem didática direta ao jogador.

Este plano parte da estrutura informada (`jogo.py`, `src/entidades/`, `src/cenas/`, `src/configuracao/`, controlador de cenas, estado do jogo e testes). O executor deve primeiro conferir o repositório real e adaptar nomes e caminhos; não deve criar sistemas duplicados quando já houver abstrações equivalentes.

## 2. Escopo fechado

### 2.1 Fases e narrativa

| Fase | Diana | Conflito central | Resultado narrativo |
| --- | --- | --- | --- |
| 1 | Infância | Exclusão e desestímulo por “isso não é coisa de menina” | Diana começa a separar seus interesses das expectativas externas. |
| 2 | Adolescência | Cobrança estética, necessidade de aceitação e silenciamento | Diana reconhece que não precisa apagar sua voz para pertencer. |
| 3 | Vida adulta | Desvalorização profissional e necessidade de provar competência | Diana sustenta seu valor sem aceitar que a pressão defina sua capacidade. |

Cada fase contém:

- cena inicial com no máximo 3 caixas de diálogo;
- percurso de plataforma curto;
- exatamente 5 flores obrigatórias;
- 5 mensagens apresentadas em sequência fixa, independentemente da posição da flor;
- cena final com no máximo 2 caixas de diálogo;
- transição automática para a fase seguinte depois que a quinta mensagem e a cena final forem concluídas.

Depois da terceira fase, deve existir uma cena de conclusão dentro da história de Diana, seguida da opção de reiniciar a experiência.

### 2.2 Sequência das mensagens

As cinco flores de cada fase devem seguir esta função dramática:

1. apresentar a pressão externa;
2. mostrar o sentimento de Diana;
3. questionar a expectativa imposta;
4. oferecer uma nova perspectiva;
5. consolidar a aprendizagem da fase.

As mensagens são associadas ao índice de coleta, e não à coordenada da flor. A primeira flor alcançada sempre apresenta a mensagem 1; a segunda, a mensagem 2; e assim por diante.

### 2.3 Regras de jogo

- Não mostrar contador de flores na interface.
- Coletar uma flor abre imediatamente a caixa de diálogo e pausa a simulação da fase.
- O texto aparece letra por letra em uma caixa posicionada na parte superior.
- Enquanto o texto está sendo digitado, `Enter` completa a frase instantaneamente.
- Depois que a frase está completa, `Enter` fecha a mensagem ou avança para a próxima fala.
- Durante diálogos, movimento, salto, gravidade e colisões dinâmicas ficam pausados.
- Ao cair para fora do mapa, reiniciar a tentativa atual: posição inicial, cinco flores e sequência de mensagens.
- A cena inicial não deve ser reproduzida novamente após uma queda na mesma fase.
- Ao fechar a mensagem da quinta flor, iniciar a cena final; não exigir que o jogador caminhe até uma saída.
- O progresso existe somente durante a execução atual; não criar arquivo de save.

### 2.4 Animações de Diana

Criar um conjunto visual diferente para infância, adolescência e vida adulta. Cada conjunto contém:

- parado: 2 quadros;
- caminhada: 4 quadros;
- salto/subida: 1 quadro;
- queda: 1 quadro;
- direção esquerda gerada em tempo de execução por espelhamento horizontal.

Total previsto: 8 quadros por idade, 24 quadros originais. Não produzir animações exclusivas de coleta, diálogo, dano ou emoção nesta versão.

### 2.5 Fora do escopo

- menus de configuração;
- salvamento persistente;
- seleção de fases;
- controles por gamepad;
- localização para outros idiomas;
- inimigos, combate ou chefes;
- minijogos adicionais;
- inventário;
- animações cinematográficas;
- contador visível de flores;
- mensagem educativa dirigida diretamente ao jogador.

## 3. Princípios de implementação

1. **Manter uma única cena ativa.** Usar o controlador existente para trocar fases e conclusão.
2. **Dirigir conteúdo por dados.** Layout, falas, mensagens, sprites e tema de cada fase devem ser configuração, não três cópias de lógica.
3. **Separar tentativa de progresso global.** Flores coletadas pertencem à tentativa atual; fases concluídas e cenas iniciais vistas pertencem à execução atual.
4. **Manter fallbacks visuais.** Ausência temporária de uma imagem não deve impedir execução e testes.
5. **Implementar o caminho completo antes do polimento.** As três fases devem ser atravessáveis com arte provisória antes de produzir ou integrar áudio.
6. **Não ampliar o escopo durante a implementação.** Qualquer ideia nova vai para uma lista pós-game-jam.

## 4. Arquitetura proposta

Os nomes abaixo são sugestões. O executor deve reutilizar classes equivalentes já existentes.

### 4.1 Definição de fase orientada a dados

Criar uma estrutura imutável, preferencialmente uma `dataclass`, semelhante a:

```python
@dataclass(frozen=True)
class DefinicaoFase:
    id: str
    nome: str
    spawn_jogadora: tuple[int, int]
    plataformas: tuple[tuple[int, int, int, int], ...]
    posicoes_flores: tuple[tuple[int, int], ...]
    dialogo_abertura: tuple[str, ...]
    mensagens_flores: tuple[str, ...]
    dialogo_encerramento: tuple[str, ...]
    sprite_jogadora: str
    imagem_fundo: str | None
    musica: str | None
```

Validar na construção ou em teste que toda fase tenha exatamente 5 posições e 5 mensagens, no máximo 3 falas de abertura e no máximo 2 falas de encerramento.

Local sugerido: `src/configuracao/fases.py` ou módulo equivalente já existente.

### 4.2 Estado global da execução

O `EstadoJogo` deve guardar apenas dados que sobrevivem à troca ou ao reinício interno de uma cena:

- índice/id da fase atual;
- conjunto de cenas iniciais já vistas;
- fases concluídas, se necessário para a cena final;
- sinalização de conclusão do jogo.

Não armazenar nele objetos Pygame, superfícies, retângulos, flores da tentativa ou callbacks de cena.

### 4.3 Estado interno da fase

A cena de fase deve operar como uma pequena máquina de estados:

```text
ABERTURA -> EXPLORACAO -> MENSAGEM_FLOR -> EXPLORACAO
                                      \-> ENCERRAMENTO -> PROXIMA_FASE
```

Estados recomendados:

- `ABERTURA`: diálogo inicial; marca a abertura como vista ao terminar;
- `EXPLORACAO`: movimento, gravidade, colisões, coleta e detecção de queda;
- `MENSAGEM_FLOR`: mundo pausado até o diálogo ser fechado;
- `ENCERRAMENTO`: diálogo final da fase;
- `TRANSICAO`: solicita ao controlador a próxima cena uma única vez.

A troca de cena não deve acontecer dentro do laço de desenho. Produzir uma intenção de transição no processamento/atualização e entregá-la ao controlador conforme o padrão já existente.

### 4.4 Entidade Flor

Responsabilidades:

- posição e retângulo de colisão;
- desenho com imagem ou fallback geométrico;
- flag local de coletada ou remoção da coleção ativa;
- nenhuma responsabilidade narrativa.

A cena decide qual mensagem mostrar usando `quantidade_coletada` antes/depois da coleta. Isso impede que uma flor conheça conteúdo ou ordem narrativa.

### 4.5 Caixa de diálogo

Criar um componente reutilizável, não uma cena separada, com:

- fila de falas;
- fala atual e quantidade de caracteres revelados;
- velocidade baseada em tempo (`dt`), não em número de quadros;
- quebra de linha respeitando a largura da caixa;
- `Enter` para completar ou avançar;
- propriedade `concluido` ou callback consumido pela cena;
- fundo opaco/semitransparente com alto contraste;
- margem e tamanho de fonte legíveis na resolução atual.

O componente recebe eventos somente quando a fase está em estado de diálogo. Evitar que o mesmo `Enter` que fecha uma fala também seja processado como salto ou ação do mundo.

### 4.6 Animação da jogadora

Separar estado físico de estado visual. A seleção de animação deve seguir:

1. se não está no chão e velocidade vertical < 0: `SALTO`;
2. se não está no chão e velocidade vertical >= 0: `QUEDA`;
3. se velocidade horizontal diferente de zero: `CAMINHADA`;
4. caso contrário: `PARADA`.

Usar temporizadores com `dt`, reiniciar o índice ao trocar de estado e preservar a direção mais recente. Espelhar quadros para a esquerda em cache, não a cada frame.

Preferir folhas de sprites com metadados centralizados ou arquivos previsíveis por idade/estado. Todos os caminhos devem continuar centralizados em `src/configuracao/caminhos.py` ou equivalente.

### 4.7 Áudio

Áudio é opcional e vem depois do caminho completo. Se implementado:

- inicializar o mixer de forma tolerante a falhas;
- usar uma faixa em loop, podendo ser reutilizada nas três fases;
- efeitos opcionais apenas para coleta e avanço de diálogo;
- jogo deve iniciar e terminar normalmente em ambiente sem dispositivo de áudio;
- registrar origem, autor e licença em `CREDITOS.md`.

## 5. Alterações prováveis por arquivo

O executor deve confirmar a árvore real com `rg --files` antes de editar.

| Área/arquivo provável | Alteração |
| --- | --- |
| `jogo.py` | Manter inicialização e loop; ajustar apenas se a nova cena inicial exigir registro/configuração. |
| `src/configuracao/caminhos.py` | Acrescentar caminhos de sprites por idade, flores, fundos, fonte e áudio opcional. |
| `src/configuracao/fases.py` | Criar as três definições de fase e o conteúdo narrativo. |
| `src/estado_jogo.py` | Guardar fase atual e cenas iniciais vistas; expor operações pequenas e testáveis. |
| `src/controlador_cenas.py` | Suportar transição automática entre três fases e conclusão sem criar mais de uma cena ativa. |
| `src/entidades/flor.py` | Nova entidade coletável com colisão e fallback visual. |
| entidade da jogadora | Adicionar máquina de animação, escolha de sprite por idade e reinício no spawn. |
| componente de diálogo | Implementar digitação, quebra de linha, Enter e desenho no topo. |
| cena base de fase | Parametrizar layout e conteúdo; integrar estados, flores, queda e transições. |
| cena de conclusão | Encerrar a história de Diana e permitir reinício completo. |
| `tests/` | Testar dados, coleta, reinício, diálogos e transições. |
| `CREDITOS.md` | Registrar todo recurso externo utilizado. |

Não criar `fase1.py`, `fase2.py` e `fase3.py` com lógica copiada, salvo se o repositório já tiver esse desenho e uma refatoração for arriscada dentro do prazo. Mesmo nesse caso, extrair as regras comuns para uma base única.

## 6. Plano de execução em 72 horas

Os horários representam teto, não meta. Ao terminar uma etapa cedo, avançar para a próxima; não expandir a etapa.

### Marco 0 — Auditoria e linha de base (horas 0–3)

1. Ler `README`, `jogo.py`, controlador, estado, cenas, entidades, configurações e testes.
2. Executar o jogo atual e registrar controles/comportamentos.
3. Executar `python3 -m unittest discover -s tests`.
4. Identificar a classe real da jogadora, a cena técnica de fase, a regra de queda e a API de troca de cenas.
5. Registrar arquivos que serão alterados e mudanças locais preexistentes; não sobrescrevê-las.
6. Criar uma lista de verificação pós-game-jam para ideias fora do escopo.

**Gate:** jogo e testes atuais executados; arquitetura real compreendida; nenhuma alteração funcional ainda.

### Marco 1 — Modelo de dados e conteúdo provisório (horas 3–8)

1. Criar `DefinicaoFase` e as três configurações.
2. Preencher diálogos provisórios dentro dos limites de 3/5/2.
3. Criar validações das quantidades e testes dessas validações.
4. Adaptar a cena de fase para receber uma definição, mantendo as plataformas atuais como ponto de partida.
5. Garantir que seja possível instanciar qualquer fase sem carregar recursos inexistentes.

**Gate:** as três fases são construídas a partir de dados e todos os testes anteriores continuam passando.

### Marco 2 — Sistema de diálogo (horas 8–14)

1. Implementar caixa superior e quebra de texto.
2. Implementar revelação por `dt`.
3. Implementar os dois comportamentos de `Enter`.
4. Pausar completamente a simulação durante diálogos.
5. Integrar abertura e encerramento, ainda sem flores.
6. Marcar a abertura como vista e verificar que ela não reaparece após reinício da tentativa.

**Gate:** cada fase abre e fecha seus diálogos corretamente; pressionar Enter não movimenta nem faz Diana saltar.

### Marco 3 — Flores e progressão narrativa (horas 14–21)

1. Implementar `Flor` e posicionar cinco por definição de fase.
2. Detectar colisão uma única vez por flor.
3. Mostrar a mensagem correspondente ao número da coleta.
4. Remover ou ocultar a flor coletada.
5. Depois da quinta mensagem, iniciar o encerramento.
6. Depois do encerramento, carregar a fase seguinte; após a terceira, carregar a conclusão.
7. Confirmar que não existe contador de flores no HUD.

**Gate:** com formas provisórias, é possível atravessar as três fases, ler as 15 mensagens na ordem correta e chegar à conclusão.

### Marco 4 — Queda e reinício da tentativa (horas 21–25)

1. Centralizar `reiniciar_tentativa()` na cena.
2. Recriar as cinco flores e zerar o índice das mensagens.
3. Reposicionar e zerar velocidades da jogadora.
4. Manter a abertura marcada como vista.
5. Evitar referências antigas a entidades removidas.
6. Verificar `R` e decidir: manter como reinício manual com as mesmas regras da queda.

**Gate:** cair ou pressionar `R` restaura a tentativa inteira sem repetir a abertura e sem duplicar flores.

### Marco 5 — Layouts finais das fases (horas 25–31)

1. Criar percursos de 2–3 minutos no máximo.
2. Manter dificuldade baixa e saltos tolerantes.
3. Distribuir flores de modo que todas fiquem visíveis ou naturalmente alcançáveis.
4. Evitar caminhos sem retorno que obriguem reinício para buscar uma flor.
5. Garantir que uma queda nunca gere softlock.

**Gate:** três playthroughs consecutivos por fase conseguem coletar tudo sem falha de layout.

### Marco 6 — Sistema de animação (horas 31–39)

1. Implementar o controlador de animação antes da arte final, usando quadros provisórios.
2. Integrar os quatro estados visuais e espelhamento.
3. Confirmar que colisão usa um retângulo estável, independente do tamanho visual dos quadros.
4. Trocar conjunto de sprites conforme a idade da fase.
5. Testar mudança de estado, direção e reinício.

**Gate:** o código aceita os 24 quadros previstos e funciona com placeholders sem alterar a física.

### Marco 7 — Produção e integração visual (horas 39–54)

1. Definir tamanho, pivô, transparência e caixa ocupada por todos os quadros antes de desenhar.
2. Produzir primeiro os 8 quadros da infância e validar no jogo.
3. Usar a mesma estrutura para adolescência e vida adulta.
4. Produzir flor, fundo e plataformas somente no nível necessário para coerência visual.
5. Integrar cada conjunto assim que estiver pronto; não esperar os 24 desenhos para testar.
6. Se houver atraso, simplificar detalhes dos desenhos, nunca remover estados ou fases já aceitos.

**Gate:** três idades são visualmente distintas; nenhum quadro desloca a personagem, muda colisão ou ultrapassa limites de forma indesejada.

### Marco 8 — Redação definitiva e revisão autoral (horas 54–59)

1. Substituir textos provisórios pelos definitivos.
2. Verificar uma única pressão central por fase.
3. Evitar culpabilizar Diana, naturalizar a agressão ou sugerir que suportar pressão é maturidade.
4. Evitar estereótipos excessivos e frases longas.
5. Ler todo o arco em sequência e conferir coerência dos saltos cronológicos.
6. Confirmar que a conclusão continua dentro da história.

**Gate:** 15 mensagens e 15 caixas de cenas revisadas, legíveis e dentro dos limites definidos.

### Marco 9 — Testes e correções (horas 59–66)

Implementar ou ajustar testes automatizados para:

1. toda fase possuir exatamente 5 flores e 5 mensagens;
2. limites de falas de abertura e encerramento;
3. primeira coleta selecionar a mensagem 1 e quinta coleta selecionar a mensagem 5;
4. flor não ser contada duas vezes;
5. quinta mensagem levar ao encerramento, não diretamente à próxima fase;
6. conclusão do encerramento avançar apenas uma vez;
7. queda zerar flores e índice narrativo;
8. queda preservar `abertura_vista`;
9. encerramento da terceira fase abrir a conclusão;
10. reinício final voltar à primeira fase com estado limpo.

Executar testes manuais para:

- A/D, setas, W, seta para cima e espaço;
- Enter durante e depois da digitação;
- pausa real durante todos os diálogos;
- colisões, limites, quedas e `R`;
- animações nas duas direções;
- jogo sem assets opcionais;
- jogo sem dispositivo de áudio;
- playthrough completo do início ao reinício final.

**Gate:** suíte verde e dois playthroughs completos sem travamentos ou softlocks.

### Marco 10 — Áudio, créditos e empacotamento (horas 66–69)

1. Só iniciar se todos os gates anteriores estiverem verdes.
2. Integrar uma música em loop; efeitos de coleta e diálogo são opcionais.
3. Confirmar licença de cada recurso externo.
4. Preencher `CREDITOS.md` com nome, autor, origem e licença.
5. Atualizar README com execução, controles, objetivo e créditos.

**Gate:** remover/indisponibilizar áudio não quebra nenhuma tela nem teste.

### Marco 11 — Buffer e entrega (horas 69–72)

1. Congelar funcionalidades.
2. Rodar suíte completa.
3. Executar em ambiente limpo com o comando documentado.
4. Fazer playthrough final cronometrado.
5. Verificar arquivos não rastreados necessários, especialmente assets.
6. Remover logs de depuração e comentários temporários.
7. Registrar limitações conhecidas sem iniciar correções arriscadas.

**Gate final:** versão demonstrável do começo ao fim usando apenas teclado.

## 7. Ordem de dependências

```text
Auditoria
  -> dados das fases
    -> diálogo
      -> flores e ordem narrativa
        -> reinício
          -> layouts finais
            -> sistema de animação
              -> arte final
                -> texto definitivo
                  -> testes completos
                    -> áudio opcional
                      -> entrega
```

Não começar arte final antes de o sistema de animação aceitar placeholders. Não começar áudio antes de o caminho completo estar estável.

## 8. Estratégia de testes técnicos

Para evitar dependência excessiva de janela e vídeo nos testes, separar regras puras de Pygame sempre que possível:

- função/objeto que seleciona a mensagem por índice;
- operação que registra coleta;
- operação que reinicia tentativa;
- decisão de próximo estado;
- validação de `DefinicaoFase`.

Nos testes que precisam de Pygame, usar driver de vídeo `dummy` quando compatível com a suíte existente. Não transformar a arquitetura inteira apenas para testar desenho pixel a pixel.

### Casos críticos de regressão

| Caso | Preparação | Ação | Resultado esperado |
| --- | --- | --- | --- |
| Coleta inicial | 0 flores | Colidir com qualquer flor | Flor removida e mensagem 1 aberta. |
| Ordem espacial diferente | Coletar outra posição primeiro | Colidir | Ainda apresentar mensagem 1. |
| Enter durante digitação | Texto incompleto | Pressionar Enter | Texto completo, diálogo ainda aberto. |
| Enter após digitação | Texto completo | Pressionar Enter | Diálogo fecha/avança uma vez. |
| Quinta flor | 4 flores | Coletar e fechar mensagem | Cena final começa. |
| Queda | 1–4 flores | Sair do mapa | 0 flores, spawn restaurado, abertura não repetida. |
| Terceira fase | Encerramento aberto | Finalizar falas | Cena de conclusão. |
| Reiniciar jogo | Conclusão | Acionar reinício | Fase 1, progresso e aberturas limpos. |

## 9. Critérios de aceite

### Funcionais

- [ ] O jogo abre diretamente na primeira fase.
- [ ] Existem três fases distintas e um salto cronológico compreensível.
- [ ] Cada fase contém cinco flores coletáveis.
- [ ] As mensagens seguem a ordem de coleta e não a posição.
- [ ] A caixa de diálogo fica no topo, digita progressivamente e responde corretamente a Enter.
- [ ] O mundo permanece pausado durante os diálogos.
- [ ] A quinta flor conduz ao encerramento e depois à próxima fase.
- [ ] Cair reinicia flores e mensagens, mas não repete a abertura.
- [ ] Não existe contador de flores na interface.
- [ ] A terceira fase conduz à conclusão e permite reiniciar.

### Visuais

- [ ] Infância, adolescência e vida adulta usam conjuntos diferentes.
- [ ] Cada conjunto possui 2 quadros parado, 4 andando, 1 saltando e 1 caindo.
- [ ] Sprites são espelhados para a esquerda sem arte duplicada.
- [ ] Animações não alteram a caixa de colisão.
- [ ] Texto é legível e não sai da caixa.

### Qualidade

- [ ] Testes antigos e novos passam.
- [ ] Dois playthroughs completos não apresentam travamento ou softlock.
- [ ] O jogo funciona sem áudio.
- [ ] Assets ausentes usam fallback ou produzem erro claro durante desenvolvimento.
- [ ] Recursos externos estão registrados em `CREDITOS.md`.
- [ ] README contém instalação, execução e controles atualizados.

## 10. Política de cortes

Ao alcançar um marco atrasado, aplicar cortes nesta ordem:

1. efeitos sonoros;
2. música;
3. fundos exclusivos, substituídos por cores/paletas;
4. detalhes visuais dos quadros, mantendo os 8 quadros e os estados definidos para cada idade;
5. polimento visual não funcional.

Não cortar:

- as três fases;
- as cinco flores por fase;
- a sequência narrativa;
- as cenas de abertura e encerramento;
- o reinício consistente;
- a conclusão da história;
- legibilidade e ausência de softlocks.

Se a produção dos 24 quadros ameaçar o caminho completo, preservar os arquivos e estados esperados usando variações simples/temporárias. Nunca deixar a implementação bloqueada esperando arte perfeita.

## 11. Protocolo de trabalho para o Codex executor

Em cada marco, o executor deve:

1. inspecionar antes de editar;
2. declarar arquivos que pretende alterar;
3. preservar mudanças existentes e não relacionadas;
4. implementar o menor incremento completo;
5. executar testes relevantes imediatamente;
6. relatar resultado e eventuais limitações;
7. só então avançar ao próximo marco.

Se encontrar divergência entre este plano e o repositório, deve preservar o comportamento já testado e adaptar os nomes/integrações. Deve pedir decisão humana apenas quando a divergência mudar escopo, narrativa ou experiência; questões puramente técnicas devem ser resolvidas seguindo a arquitetura existente.

## 12. Definição final de pronto

Myosotis convallaria está pronto para a game jam quando uma pessoa consegue iniciar o jogo, acompanhar Diana pela infância, adolescência e vida adulta, coletar as 15 flores, ler toda a narrativa, chegar à conclusão e reiniciar a experiência, sem travamento, softlock ou necessidade de instrução externa além dos controles documentados.
