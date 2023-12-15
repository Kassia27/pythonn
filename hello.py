#!/usr/bin/env python3

"""
Hello Wold Multi Linguas.

Dependendo da lingua configurada no ambiente o programa exibe a messagem correspondente.

Como usar:

Tenha a variavel LANG devidamente configurada ex:

      export LANG=pt_BR

Execução:

      python3 hello.py
      ou 
      ./hello.py

"""


language = os.get_env("LANG","en_US")

msg = "Hello,World!"

if language == "pt_BR":
    msg = "Ola Mundo!"
elif language == "in_IT"
   msg = "Caio,Mondo!"

print (msg)