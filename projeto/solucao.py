import time
from algoritmoDPLL import *


def abrirTabelaCNF(CNF):
    with open(CNF) as arquivo:
        grid = []
        cnfInf = []
        
        for linha in arquivo:
            if linha[0] == 'p':
                linha = linha.split(' ')

                cnfInf.append(int(linha[2]))
                cnfInf.append(int(linha[3]))

            if linha[0] != 'c' and linha[0] != 'p' and linha[0] != '%' and linha[0] != '0' and linha[0] != ' ':
                linhaInt = []
                
                linha = linha.split(' ')
                linha.pop(-1)
                
                for elemento in linha:
                    linhaInt.append(int(elemento))
                
                grid.append(linhaInt)

        return [grid, cnfInf]
    
    
def criarArquivosDIMACS(inf, resultado):
    with open(f"TestesDIMACSCNF/Solucoes/cnf-{inf[0]}-{inf[1]}.cnf", "w") as arquivo:
        if resultado == False:
            arquivo.writelines('UNSATISFIABLE')
        else:
            inf = ''
            for elemento in resultado:
                inf = inf + f'{elemento} '
            arquivo.writelines(f'{inf}0')

    
def solucao(arquivo):
        arquivoDIMACS, inf = abrirTabelaCNF(arquivo)
        resultado = DPLL(arquivoDIMACS)
        
        if (resultado == False): 
            print('UNSATISFATIBLE\n')
        else:
            print(f'RESULTADO SATISFATiVEL: {resultado}\n')
        
        criarArquivosDIMACS(inf, resultado)

start_time = time.time()

# FORMULAS INSATISFATÍVEIS
solucao('TestesDIMACSCNF/Fórmulas Insatisfatíveis/cnf-02-04.cnf')

# FORMULAS SATISFATÍVEIS
solucao('TestesDIMACSCNF/Fórmulas Satisfatíveis/cnf-03-02.cnf')
solucao('TestesDIMACSCNF/Fórmulas Satisfatíveis/cnf-03-04.cnf')

end_time = time.time()
