"""Hello World Multi Linguas.

Dependendo da lingua configurada no ambiente o programa exibe a mensagem
correspondente.

Tenha a variável LANG devidamente configurada ex:
    export LANG=pt_BR

Execução:
    python3 hello.py
"""

from os import getenv

currente_language = getenv("LANG")

msg = "Helloy word"

if currente_language == "pt_BR.UTF-8":
    msg = "Olá, Mundo!"

print(msg)