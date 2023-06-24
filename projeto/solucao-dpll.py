from algoritmoDPLL import *


def abrirTabelaCNF(CNF):
    # Abre o caminho do arquivo
    with open(CNF) as arquivo:
        grid = []
        cnfInf = []

        # pega cada linha do arquivo
        for linha in arquivo:
            # pega a linha que começa com p que no caso é a segunda linha
            if linha[0] == 'p':
                linha = linha.split(' ')

                # pega a quantidade de atômicas e cláusulas e guarda dentro da array "cnfInf".
                cnfInf.append(int(linha[2]))
                cnfInf.append(int(linha[3]))

            # basicamente pega as clásulas com as formulas
            if linha[0] != 'c' and linha[0] != 'p' and linha[0] != '%' and linha[0] != '0' and linha[0] != ' ':
                linhaInt = []
                
                linha = linha.split(' ') # cria o array separado por ' '
                linha.pop(-1) # remove o "0" de dentro da array

                # fica dessa forma por exemplo: ['-1', '3']
                
                for elemento in linha:
                    linhaInt.append(int(elemento))
                
                # basicamente faz um append em cada linha e coloca dentro da array grid.
                grid.append(linhaInt)
            
        # cnfInf -- retorna a quantidade de atômicas e cláusulas.
        # grid --  retorna uma array de cláusulas.
        return [grid, cnfInf]
    
    
def criarArquivosDIMACS(inf, resultado):
    # Cria cada arquivo cnf pela quantidade de atômicas e cláusulas dentro da pasta soluções de TestesDIMACSCNF
    with open(f"TestesDIMACSCNF/Solucoes/cnf-{inf[0]}-{inf[1]}.cnf", "w") as arquivo:
        if resultado == False:
            # Se não for satisfátivel vai aparacer no arquivo esse texto
            arquivo.writelines('UNSATISFIABLE')
        else:
            # Se for satisfátivel vai aparacer no arquivo esse texto com os valores que deixam a expressão satisfátivel.
            inf = ''
            for elemento in resultado:
                inf = inf + f'{elemento} '
            arquivo.writelines(f'{inf}0')

    
def solucao(arquivo):
        arquivoDIMACS, inf = abrirTabelaCNF(arquivo)
        # essa função vai retornar a lógica pra dizer se satisfativel ou não, se não for vai retornar falso e se for satisfátivel vai retornar o valor que deixam a formula satisfativel
        resultado = DPLL(arquivoDIMACS) 
        
        # essa função vai criar os arquivos para cada exemplo da cnf
        criarArquivosDIMACS(inf, resultado)

# FORMULAS INSATISFATÍVEIS
solucao('TestesDIMACSCNF/Fórmulas Insatisfatíveis/cnf-02-04.cnf')

# FORMULAS SATISFATÍVEIS
solucao('TestesDIMACSCNF/Fórmulas Satisfatíveis/cnf-03-02.cnf')
solucao('TestesDIMACSCNF/Fórmulas Satisfatíveis/cnf-03-04.cnf')

