#! -*- coding: utf-8 -*-

__author__ = 'Eduardo Henrique '
__license__ = "GNU"
__version__ = "1.0.1"

import PyPDF2
import logging
import os


class Main:
    def __init__(self):
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S',
        )
        self.logger = logging.getLogger(__name__)
    
    @property
    def start(self):
        for _, _, arquivo in os.walk(r'C:\Users\teste\Pictures\PDF'):
            print(arquivo)
            #lerPdf = PyPDF2.PdfFileReader(arquivo)
            #pagina = lerPdf.getPage(1)
            #conteudo = pagina.extractText()
            #if "petrobras" in conteudo:
            #    print(f"Encontrado conteudo da petrobras no arquivo:{arquivo}\nConteudo:{conteudo}")
            #else:
            #    print(f"Não encontrei nada no arquivo:{arquivo}")

if __name__ == "__main__":
    init = Main()
    init.start