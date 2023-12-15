#!/usr/bin/env python3

"""Hello Wold Multi Linguas.

Dependendo da lingua configurada no ambiente o programa exibe a messagem correspondente.

Como usar:

Tenha a variavel LANG devidamente configurada ex:

      export LANG=pt_BR

Execução:

      python3 hello.py
      ou 
      ./hello.py 

"""
__version__ = "0.0.1"
__author__ = "Rita Calixto"
__license__ = "Unlicense"

import os

language = os.getenv("LANG", "en_US")[:5]

msg = "Hello,World!"

if language == "pt_BR":
    msg = "Ola Mundo!"
elif language == "it_IT":
   msg = "Ciao,Mondo!"
elif language == "es_SP":
   msg = "Hola, Mundo!"

print (msg)