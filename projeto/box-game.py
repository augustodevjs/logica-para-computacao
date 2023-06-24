import csv
from algoritmoDPLL import *


def abrirTabelaCNF(CNF):
    with open(CNF) as arquivo:
        grid = []
        
        for linha in arquivo:
            if linha[0] != 'c' and linha[0] != 'p' and linha[0] != '%' and linha[0] != '0' and linha[0] != ' ':
                linhaInt = []
                
                linha = linha.split(' ')
                linha.pop(-1)
                
                for elemento in linha:
                    linhaInt.append(int(elemento))
                
                grid.append(linhaInt)

    return grid


def criarClausulas(arquivo):
    with open(arquivo) as csv_file:
        grid = []
        csv_reader = csv.reader(csv_file, delimiter=',')
        
        for linha in csv_reader:
            linhaCnf = []
            for atomica in linha:
                linhaCnf.append(atomica.replace(' ', ''))
            grid.append(linhaCnf)

        grid.pop(0)
    
        return grid

def solucao(arquivo):
    formulaDIMACS, numeroAtomicas, listaAtomicasNumeros = transformarEmDIMACS(arquivo)
    criarArquivosDIMACS(formulaDIMACS, numeroAtomicas)
    
    arquivoDIMACS = abrirTabelaCNF('BoxGameCNF/dados-boxgame.txt')
    resultado = DPLL(arquivoDIMACS)

    print(resultado)
    print(listaAtomicasNumeros)

    for removidos in listaAtomicasNumeros:
        test = removidos[0] in resultado
        
        if test == False:
            print(removidos[0])


def transformarEmAtomicas(resultado, listaAtomicasNumeros):
    resultadoAtomicas = []
    
    for elementos in resultado:
        for posicao in listaAtomicasNumeros:
            if elementos == posicao[0]:
                resultadoAtomicas.append(str(posicao[1]))
                
    return resultadoAtomicas


def transformarEmDIMACS(formulaCNF):
    listaDeClausulas = []
    listaNumerosEAtomicas = []
    formulaDIMACS = []
    numeroAtomicas = 0

    for clausula in formulaCNF:
        for literal in clausula:
            listaDeClausulas.append(literal)
                
    for index, clausula in enumerate(sorted(set(listaDeClausulas))):
        listaNumerosEAtomicas.append([index + 1, clausula])
        numeroAtomicas += 1 
        
    for clausula in formulaCNF:
        listaAuxiliar = []
        for literal in clausula:
            for teste in listaNumerosEAtomicas:
                if literal == teste[1]:
                    listaAuxiliar.append(teste[0])
                    
        formulaDIMACS.append(listaAuxiliar)

    return formulaDIMACS, numeroAtomicas, listaNumerosEAtomicas


def criarArquivosDIMACS(formulaDIMACS, numeroAtomicas):
    numeroClausulas = 0
    
    for clausula in formulaDIMACS:
        numeroClausulas += 1
    
    with open("BoxGameCNF/dados-boxgame.txt", "w") as arquivo:
        arquivo.writelines(f'p cnf {numeroAtomicas} {numeroClausulas}\n')

        for clausula in formulaDIMACS:
            clausula = str(clausula).replace(',', '')
            clausula = str(clausula).replace('[', '')
            clausula1 = str(clausula).replace(']', '')
            arquivo.writelines(f'{clausula1} 0\n')
    
    return


solucao(criarClausulas('BoxGameCNF/boxgame.txt'))