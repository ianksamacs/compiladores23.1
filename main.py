#author: Ianc Samac, Luis Eduardo

import os
import glob

def get_arquivos(caminho_pasta):
    return glob.glob(os.path.join(caminho_pasta, '*.txt'))

# Lê cada arquivo e adiciona seu conteúdo a uma lista
    conteudos_arquivos = []
def export(file, result):
    file = file.replace('.txt', '-saida.txt')
    with open(file, 'w') as f:
        f.write(result)

def analisar(file):
    conteudo_arquivo = ""
    with open(file, 'r') as f:
        conteudo_arquivo = f.read()
    if conteudo_arquivo == "":
        return export(file, "")
    else:
        return export(file, conteudo_arquivo)

def main():
    for x in get_arquivos("files/"):
        analisar(x)

if __name__ == '__main__':
    main()
