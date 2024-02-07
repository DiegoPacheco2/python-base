"""Hello Word Multi Linguas.

Dependendo da lingua configurada no ambiente o programa exibe a mensagem
correspondente.

Como usar:

Tenha a variável LANG devidamente configurada ex:

    export LANG=pt_BR

Execução:
  
    python hello.py
    ou
    ./
"""

__version__ = "0.0.1"
__author__ = "Diego Rocha"
__license__ = "Unlicense"

from os import getenv

current_language = getenv("LANG")
msg = "Hello, Word"

if current_language == "pt_BR.UTF-8":
    msg = "Iae, Mundo vei"
elif current_language == "fn_FN":
    msg = "Bonjour le monde"
elif current_language == "al_AL":
    msg = "Hallo Welt"

print(msg.upper())

