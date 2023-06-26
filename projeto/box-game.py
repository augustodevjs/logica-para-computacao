import csv
from algoritmoDPLL import *

def transformarEmDIMACS(formulaCNF):
    # armazena as cláusulas da formulaCNF EX: ['q1', 'q2', 'q3]
    listaDeClausulas = [] 
    # armazena a lista de numero de atômicas
    # EX: [[1, 'q1'], [2, 'q2'], [3, 'q3'], [4, 'q4'], [5, 'r1'], [6, 'r2']
    listaNumerosEAtomicas = []
    # armazena a formulaDIMACS em valores inteiros transformada a partir do arquivo
    formulaDIMACS = []
    # armazena os numeros de atômicas da formulaCFN
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
    
    print('FormulaDIMACS:',formulaDIMACS)
    print('NumeroAtomicas:', numeroAtomicas)
    print('ListaNumerosEAtomicas:',listaNumerosEAtomicas)

    return formulaDIMACS, numeroAtomicas, listaNumerosEAtomicas


def criarArquivosDIMACS(formulaDIMACS, numeroAtomicas):
    # armazena o numero de clausulas que vai ser usado para
    # colocar no arquivo de dados-boxgame.txt
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


# essa função vai pegar todos os dados de boxgame.txt e colocar dentro de uma 
# lista, removendo a primeira linha, ou seja, vai pegar somente as cláusulas.
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
    
    resultado = DPLL(formulaDIMACS)

    resultRemovidos = []

    for removidos in listaAtomicasNumeros:
        test = removidos[0] in resultado

        if test == False:
            resultRemovidos.append(removidos[0])

    return resultRemovidos

print(solucao(criarClausulas('BoxGameCNF/boxgame.txt')))