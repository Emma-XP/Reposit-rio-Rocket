"""Entidades que podem compor as cenas do jogo."""

from src.entidades.entidade import Entidade
from src.entidades.entidade_visual import EntidadeVisual
from src.entidades.flor import Flor
from src.entidades.jogadora import Jogadora
from src.entidades.plataforma import Plataforma
from src.entidades.texto import Texto

__all__ = [
    "Entidade",
    "EntidadeVisual",
    "Flor",
    "Jogadora",
    "Plataforma",
    "Texto",
]
