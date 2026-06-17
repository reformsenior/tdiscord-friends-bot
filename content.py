"""Listas de conteúdo para o Discord Friends Bot."""

import random

PIADAS: list[str] = [
    "Por que o programador usa óculos? Porque não consegue C#! 😎",
    "O que o zero disse para o oito? Bonito cinto! 🤣",
    "Por que o livro de matemática ficou triste? Porque tinha muitos problemas. 📚",
    "O que o pato disse pro outro pato? Estamos empatados! 🦆",
    "Por que o computador foi ao médico? Porque estava com vírus! 🖥️",
    "Qual é o cúmulo da velocidade? Correr ao redor de uma mesa e pegar a si mesmo! 🏃",
    "O que a impressora disse pro computador? Pode falar, estou toda ouvidos de papel! 🖨️",
]

RESPOSTAS_8BALL: list[str] = [
    "Com certeza! ✅",
    "Sem dúvida nenhuma! 🎯",
    "Pode contar com isso! 👍",
    "As estrelas dizem que sim! ⭐",
    "Tudo indica que sim! 🌟",
    "Talvez... pergunte de novo depois 🤔",
    "Hmm, não tenho certeza agora... 😶",
    "Não conte com isso ❌",
    "As chances são baixas... 📉",
    "Definitivamente não! 🚫",
]


def escolher_aleatorio(lista: list[str]) -> str:
    return random.choice(lista)
