"""Conteúdo e layouts das três fases de Myosotis convallaria."""

from dataclasses import dataclass
from pathlib import Path

from src.configuracao.caminhos import IMAGENS_FUNDO


@dataclass(frozen=True)
class DefinicaoFase:
    """Reúne os dados imutáveis necessários para construir uma fase."""

    id: str
    nome: str
    idade: str
    spawn_jogadora: tuple[int, int]
    plataformas: tuple[tuple[int, int, int, int], ...]
    posicoes_flores: tuple[tuple[int, int], ...]
    dialogo_abertura: tuple[str, ...]
    mensagens_flores: tuple[str, ...]
    dialogo_encerramento: tuple[str, ...]
    imagem_fundo: Path | None
    cor_fundo: tuple[int, int, int]
    musica: Path | None = None

    def __post_init__(self) -> None:
        if len(self.posicoes_flores) != 5:
            raise ValueError("Cada fase deve possuir exatamente cinco flores.")
        if len(self.mensagens_flores) != 5:
            raise ValueError("Cada fase deve possuir exatamente cinco mensagens.")
        if not 1 <= len(self.dialogo_abertura) <= 3:
            raise ValueError("A abertura deve possuir de uma a três falas.")
        if not 1 <= len(self.dialogo_encerramento) <= 2:
            raise ValueError("O encerramento deve possuir uma ou duas falas.")


FASES = (
    DefinicaoFase(
        id="infancia",
        nome="Infância",
        idade="infancia",
        spawn_jogadora=(70, 838),
        plataformas=(
            (0, 920, 400, 160),
            (470, 820, 310, 40),
            (850, 710, 310, 40),
            (1230, 820, 280, 40),
            (1580, 690, 340, 390),
        ),
        posicoes_flores=(
            (260, 866), (650, 766), (1030, 656), (1390, 766), (1740, 636)
        ),
        dialogo_abertura=(
            "Diana gostava de desmontar brinquedos para descobrir como funcionavam.",
            "Na escola, ela corria para a mesa das experiências sempre que podia.",
        ),
        mensagens_flores=(
            "Algumas vozes diziam que aquelas experiências não eram coisa de menina.",
            "Diana sentiu sua curiosidade encolher, como se ocupasse espaço demais.",
            "Mas desde quando a curiosidade escolhe quem pode senti-la?",
            "Cada pergunta que ela fazia abria um caminho que antes não existia.",
            "Diana decidiu guardar suas perguntas, não as expectativas dos outros.",
        ),
        dialogo_encerramento=(
            "Naquele dia, Diana voltou para casa pensando em tudo que ainda queria descobrir.",
        ),
        imagem_fundo=IMAGENS_FUNDO["infancia"],
        cor_fundo=(41, 55, 74),
    ),
    DefinicaoFase(
        id="adolescencia",
        nome="Adolescência",
        idade="adolescencia",
        spawn_jogadora=(70, 778),
        plataformas=(
            (0, 860, 330, 220),
            (400, 740, 300, 40),
            (770, 850, 300, 40),
            (1140, 720, 300, 40),
            (1510, 820, 410, 260),
        ),
        posicoes_flores=(
            (220, 806), (570, 686), (940, 796), (1310, 666), (1740, 766)
        ),
        dialogo_abertura=(
            "Anos depois, Diana aprendeu a medir cada palavra antes de falar.",
            "Parecer aceita às vezes parecia mais importante do que ser ouvida.",
        ),
        mensagens_flores=(
            "Diziam como Diana deveria parecer, sorrir e falar para caber no grupo.",
            "Ela começou a esconder opiniões que antes dizia sem medo.",
            "Pertencer precisava mesmo significar desaparecer um pouco?",
            "Sua voz podia mudar uma conversa sem pedir licença para existir.",
            "Diana falou com firmeza e percebeu que ainda pertencia a si mesma.",
        ),
        dialogo_encerramento=(
            "A voz de Diana não ficou mais alta; ficou mais sua.",
        ),
        imagem_fundo=IMAGENS_FUNDO["adolescencia"],
        cor_fundo=(61, 46, 76),
    ),
    DefinicaoFase(
        id="vida_adulta",
        nome="Vida adulta",
        idade="vida_adulta",
        spawn_jogadora=(70, 818),
        plataformas=(
            (0, 900, 350, 180),
            (420, 780, 300, 40),
            (790, 650, 300, 40),
            (1160, 780, 300, 40),
            (1530, 640, 390, 440),
        ),
        posicoes_flores=(
            (230, 846), (590, 726), (960, 596), (1330, 726), (1730, 586)
        ),
        dialogo_abertura=(
            "Já adulta, Diana entrou em uma sala onde seu trabalho seria avaliado.",
            "Ela conhecia cada detalhe do projeto que havia ajudado a construir.",
        ),
        mensagens_flores=(
            "Mesmo preparada, Diana era interrompida e precisava provar o óbvio outra vez.",
            "O esforço dobrado trouxe cansaço e uma dúvida que não era dela.",
            "Por que sua competência parecia sempre começar sob suspeita?",
            "Diana apresentou os dados com clareza e reconheceu o valor do próprio trabalho.",
            "A pressão continuava ali, mas já não definia do que ela era capaz.",
        ),
        dialogo_encerramento=(
            "Diana terminou a apresentação sem diminuir o que sabia.",
            "Ao sair da sala, levou consigo a certeza que construiu ao longo do caminho.",
        ),
        imagem_fundo=IMAGENS_FUNDO["vida_adulta"],
        cor_fundo=(37, 58, 63),
    ),
)


FASES_POR_ID = {fase.id: fase for fase in FASES}
