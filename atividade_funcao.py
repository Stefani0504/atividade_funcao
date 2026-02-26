'''

🧠 Atividade Prática – Sistema de calculadora da empresa Devoc Technology | Dia 11/02
 
🎯 Objetivo da Atividade
 
Praticar a criação de funções com parâmetros e retorno utilizando operações matemáticas.
 
📋 Cenário
 
A empresa Devoc Technology está desenvolvendo um sistema simples de calculadora para uso interno dos funcionários do setor financeiro.
 
O sistema precisa realizar as principais operações matemáticas básicas:
Soma
Subtração
Multiplicação
Divisão
Você foi contratado(a) como desenvolvedor(a) júnior para criar as funções responsáveis por essas operações.
 
🔧 O que você deve fazer
 
Criar as seguintes funções:
somar(n1, n2)
subtrair(n1, n2)
multiplicar(n1, n2)
dividir(n1, n2)
Cada função deve:
Receber dois números como parâmetro
Retornar o resultado da operação
Criar duas variáveis com valores numéricos
Chamar cada função
Exibir os resultados no console
 
💻 Exemplo de saída esperada
Soma: 25
Subtração: 5
Multiplicação: 150
Divisão: 2
 
💡 DICA IMPORTANTE 
 
Use return dentro das funções e utilize print() fora delas para mostrar os resultados.
 
✅ Critérios para a atividade estar correta
Criar todas as funções solicitadas
Utilizar parâmetros corretamente
Utilizar return
Chamar as funções corretamente
Exibir os resultados no console'''


def soma(n1, n2):

    return n1 + n2

resultado_soma = soma(18, 8)
print (resultado_soma)

def subtracao(n1, n2):
    return n1 - n2

resultado_subtracao = subtracao(25, 5)
print (resultado_subtracao)

def divisao(n1, n2):
    return n1 / n2

resultado_divisao = divisao(13, 6)
print (resultado_divisao)

def multiplicacao(n1, n2):

    return n1 * n2

resultado_multiplicacao = multiplicacao(12, 2)
print (resultado_multiplicacao)
