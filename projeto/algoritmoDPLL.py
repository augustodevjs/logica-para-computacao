from copy import deepcopy

def DPLL(formulaCNF):
    # fórmulaCNF é uma lista de cláusulas, onde cada cláusula é uma lista
    # de literais
    
    # Interpretação é uma lista que contém uma atribuição parcial de valores
    # verdadeiros/falso às variáveis da fórmula.
    return DPLLCheck(formulaCNF, interpretacao = [])


def DPLLCheck(formulaCNF, interpretacao):
    # cria uma copia da formulaCNF para garantir a integridade dos dados
    copiaCNF = deepcopy(formulaCNF)
    # simplifica a fórmula CNF substituindo todas as cláusulas unitárias
    # e atualiza a interpretação com os valores verdadeiro/falso deduzidos. 
    # Isso é feito até que não haja mais cláusulas unitárias na fórmula.
    copiaCNF, interpretacao = propagacaoDeUnidade(copiaCNF, interpretacao)

    # verifica se a fórmula CNF está vazia, o que significa que todas as 
    # cláusulas foram satisfeitas. Após isso, retorna a interpretação
    # ordernada
    if copiaCNF == []: 
        return sorted(interpretacao)
    
    # Verifica se há uma cláusula vazia na fórmula CNF, o que significa que a 
    # intepretação atual é insatisfátivel. Após isso, retorna false.
    if [] in copiaCNF: 
        return False
    
    # percorre cada literal em cada cláusula da fórmula CNF e retorna a última 
    # variável atômica encontrada nessa fórmula, se houver alguma. Caso 
    # contrário, se não houver variáveis atômicas, a função não retorna nada.
    atomica = pegarAtomica(copiaCNF)

    # Cria duas novas fórmulas CNF modificadas, S1 e S2, adicionando uma nova 
    # cláusula contendo a variável atômica e sua negação, respectivamente.
    
    S1 = copiaCNF + [[atomica]]
    S2 = copiaCNF + [[atomica * -1]]

    # Chama recursivamente a função DPLLCheck passando S1 e a interpretação 
    # atual. Se o resultado dessa chamada recursiva for diferente de False, ou 
    # seja, uma interpretação satisfatível foi encontrada, retorna esse 
    # resultado.
    
    resultado = DPLLCheck(S1, interpretacao)

    # Se o resultado de DPLLCheck(S1, interpretacao) for False, chama 
    # recursivamente a função DPLLCheck passando S2 e a interpretação atual. 
    # Nesse caso, essa segunda chamada recursiva irá explorar a outra escolha 
    # possível para a variável atômica.

    # O algoritmo DPLL continua a fazer essas escolhas recursivas até 
    # encontrar uma interpretação satisfatível ou determinar que a fórmula é 
    # insatisfatível. A função retorna False se a fórmula é insatisfatível ou 
    # a interpretação ordenada se for satisfatível.
    
    return resultado if resultado != False else DPLLCheck(S2, interpretacao)

def pegarAtomica(formulaCNF):
    # lista vazia para armazenar as variáveis atômicas.
    listaAtomicas = []
    
    # percorre cada cláusula na fórmula
    for clausula in formulaCNF:
        # percorre cada literal dentro de uma cláusula
        for literal in clausula:
            # verifica se o literal é positivo. Se for positivo, significa
            # que é uma variável atômica, então esse literal é adicionado
            # à lista 
            if literal > 0: 
                listaAtomicas.append(literal)
    # Após o término dos loops, o código executa list(set(listaAtomicas)) != []. Aqui, set(listaAtomicas) cria um conjunto dos elementos em 
    # listaAtomicas, removendo quaisquer duplicatas. Em seguida, list(...) 
    # converte o conjunto de volta em uma lista. O código verifica se essa 
    # lista não é vazia
    if list(set(listaAtomicas)) != []: 
        # retorna a última variável atômica encontrada na fórmula CNF.
        return listaAtomicas.pop()    
  

# Essa função realiza a propagação das atribuições unitárias na fórmula CNF.
def propagacaoDeUnidade(formulaCNF, interpretacao):
    # Enquanto houver cláusulas unitárias na formula CNF
    while existeClausulaUnitaria(formulaCNF):
        # Obtem o literal unitário
        literal = unidadeLiteral(formulaCNF)
        # Adiciona o literal a interpretação
        interpretacao = interpretacao + [literal]
        # remove as clásulas que contêm o literal da fórmula CNF
        formulaCNF = removerClausulasComLiteral(formulaCNF, literal)
        # remove o complemento do literal das cláusulas da fórmula CNF
        formulaCNF = removerComplementoDoLiteral(formulaCNF, literal)
    
    # Retorna o cnf e a interpretação
    return formulaCNF, interpretacao


# percorre as cláusulas da formula e retorna o primeiro literal
# de uma claúsula unitária encontrada.
def unidadeLiteral(formulaCNF):
    for clausula in formulaCNF:
        if len(clausula) == 1: 
            return clausula[0]
        

# essa função verifica se existe alguma cláusula unitária, ou seja, uma 
# cláusula com apenas um literal. Se existir retorna True se não retorna False.
def existeClausulaUnitaria(formulaCNF):
    for clausula in formulaCNF:
        if len(clausula) == 1: 
            return True
    
    return False
        
# remove todas as cláusulas quem contêm o literal especificado.
def removerClausulasComLiteral(formulaCNF, literal):
    # Lista vazia para armazenar as cláusulas sem o literal.
    novaFormulaCNF = []

    for clausula in formulaCNF:
        # verifica se o literal não está presente na cláusula
        if literal not in clausula:
            # se o literal não estiver presente na cláusula, siginifica que
            # essa cláusula não contém o literal que deve ser removido, 
            # ai eu adiciono essa cláusula a lista 'novaFormulaCNF'
            novaFormulaCNF.append(clausula)

    # retorna as cláusulas originais da fórmulas CNF, exceto aquelas que 
    # continham o literal especificado
    return novaFormulaCNF

# remove cláusulas que contenham o complemento do literal especificado
def removerComplementoDoLiteral(formulaCNF, literal):
    for clausula in formulaCNF:
        # verifica se o complemento do literal está presente na cláusula atual.
        # O operador '*' é usado para multiplicar o 'literal' por -1, a fim de
        # obter o seu complemento.
        if (literal * -1) in clausula: 
            # se o complemento do literal estiver presente na cláusula, ele é
            # removido.
            clausula.remove(literal * -1)
    # retorna a lista sem os complementos do literal      
    return formulaCNF
