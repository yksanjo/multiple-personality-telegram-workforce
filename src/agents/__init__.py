#!/usr/bin/env python3
"""
Multiple Personality Telegram Workforce - Agents Module

Your AI dream team with distinct personalities:
- Monica: Chief of Staff (organized, perfectionist)
- Dwight: Research Specialist (intense, thorough)
- Kelly: Social Media Manager (trendy, chatty)
- Ross: Lead Engineer (technical, detailed)
- Pam: Creative Assistant (artistic, kind)
- Rachel: LinkedIn Manager (professional, stylish)
"""

__version__ = "1.0.0"
__author__ = "Your Name"

from .base_agent import BaseAgent
from .monica import MonicaAgent
from .dwight import DwightAgent
from .kelly import KellyAgent
from .ross import RossAgent
from .pam import PamAgent
from .rachel import RachelAgent

__all__ = [
    'BaseAgent',
    'MonicaAgent',
    'DwightAgent',
    'KellyAgent',
    'RossAgent',
    'PamAgent',
    'RachelAgent'
]
