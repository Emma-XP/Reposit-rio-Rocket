# Myosotis convallaria

Jogo narrativo de plataforma desenvolvido em Python com Pygame para a Semana
Nacional de Ciência e Tecnologia (SNCT), com o tema “Mulheres na Ciência”. A
experiência acompanha Diana em três momentos de sua vida e dura cerca de 6 a
10 minutos.

## Instalação e execução

Requer Python 3.10 ou mais recente. Na raiz do projeto:

```bash
python3 -m pip install -r requirements.txt
python3 jogo.py
```

O jogo funciona sem imagens, fontes ou áudio externos: formas e animações
provisórias são usadas automaticamente quando os arquivos esperados não
existem.

## Resolução

O jogo aceita janelas de `1920x1080` e `1366x768`. Para alternar entre elas,
edite apenas `RESOLUCAO_ATIVA` em `src/configuracao/configuracoes.py`:

```python
RESOLUCAO_ATIVA = "1920x1080"
```

Use `"1366x768"` para retornar à resolução menor. As cenas conservam o mesmo
campo de visão, posições e colisões nos dois modos.

## Controles

- `A`/`D` ou setas esquerda/direita: movimentar Diana;
- `W`, seta para cima ou espaço: pular;
- `Enter`: completar a digitação ou avançar uma fala;
- `R`: reiniciar a tentativa atual durante a exploração.

Encontre as cinco flores de cada fase. Cada flor pausa o percurso e revela uma
parte da trajetória na ordem de coleta. Cair ou pressionar `R` restaura todas
as flores daquela tentativa sem repetir a abertura da fase.

## Testes

```bash
SDL_VIDEODRIVER=dummy SDL_AUDIODRIVER=dummy python3 -m unittest discover -s tests -v
```

Os caminhos para substituir as formas provisórias estão centralizados em
`src/configuracao/caminhos.py`. Consulte [CREDITOS.md](CREDITOS.md) antes de
adicionar recursos de terceiros.
