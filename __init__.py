"""
Project Name: Unicat
Created By: RavinClaw

Github: github.com/RavinClaw
Github Repo: github.com/RavinClaw/Unicat

Files withing Project:
__init__.py
mathf.py
unicat.py
"""

# __init__.py File Content

# From Mathf
from .mathf import add
from .mathf import subtract
from .mathf import multiply
from .mathf import divide
from .mathf import calculate_degrees
from .mathf import calculate_radians
from .mathf import sine, cosine, tangent
from .mathf import inverse_sine, inverse_cosine, inverse_tangent

# From Unicat
from .unicat import Console

__all__ = [
    "add",
    "subtract",
    "multiply",
    "divide",
    "Console",
    "calculate_degrees",
    "calculate_radians",
    "sine",
    "cosine",
    "tangent",
    "inverse_sine",
    "inverse_cosine",
    "inverse_tangent"
]

# END OF FILE