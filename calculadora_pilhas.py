from pilha import * # Importa as funções de pilha.py

class Calculadora: # Define a nova classe Calculadora
    def __init__(self, max): # Construtor da classe, recebe o parâmetro max referente ao tamanho máximo das pilhas
        # Cria as pilhas de operadores e operandos: 
        self.operadores = Pilha(max)
        self.operandos = Pilha(max)
        
def precedencia(operador): # Função para determinar a precedência entre os operadores
    if operador in ['+', '-']: # Se operador for '+' ou '-', retorna 1
        return 1
    if operador in ['*', '/']: # Se operador for '*' ou '/', retorna 2
        return 2
    return 0 # Se o operador não for nenhum dos anteriores, recebe 0

def calcula_operadores(operador, v1, v2): # Determina a operação matemática a ser realizada por tal operador:
    if operador == '+':
        return v1 + v2   
    if operador == '-':
        return v1 - v2
    if operador == '*':
        return v1 * v2
    if operador == '/':
        if v2 == 0:
            raise ValueError("Erro: Divisão por zero!") # Se o segundo valor na divisão for 0, o código lança um erro de divisão por zero. Ex: 3 / 0 = Erro: Divisão por zero
        else:
            resultado = v1 / v2
            if resultado.is_integer(): # Se a divisão resulta em um número inteiro, retornará um número inteiro. Ou seja, '10 / 5' não retornará '2.0' e sim '2'
                return int(resultado)
            else:
                return resultado # Se a divisão resulta em um número não inteiro, retorna um número de ponto flutuante (float - Ex: 2.5)
            
def calcula_expressao(calculadora, expressao): # Calcula os valores inseridos na expressão pelo usuário: 
    num = "" # Variável com string vazia. Usada para construir números de vários dígitos na expressão.
    for char in expressao: # Laço para percorrer cada caractere na expressão

        if char.isdigit(): # Verifica se o caracterer for dígito
            num += char # Adiciona o caractere na variável num

        else: # Se o caractere não for dígito, este bloco de código é executado:
            if num != "": # Se num não estiver vazio, o valor é convertido em inteiro e empilhado na pilha de operandos.
                pilha_push(calculadora.operandos, int(num))
                num = "" # Redefine a variável num para uma string vazia

            if char in ['+', '-', '*', '/']: # Verifica se o caractere é um operador: 
                # Enquanto a pilha de operadores não estiver vazia e a precedência do operador atual for menor ou igual à precedência do operador 
                # no topo da pilha, o código a seguir é executado
                while (not pilha_vazia(calculadora.operadores) and precedencia(char) <= precedencia(pilha_topo(calculadora.operadores))):                        
                    operador = pilha_pop(calculadora.operadores) # O operador no topo da pilha de operadores é desempilhado e armazenado na variável 'operador'
                    v2 = pilha_pop(calculadora.operandos) #  O operando no topo da pilha de operandos é desempilhado e armazenado na variável 'v2'
                    v1 = pilha_pop(calculadora.operandos) # O operando no topo da pilha de operandos é desempilhado e armazenado na variável 'v1'
                    resultado = calcula_operadores(operador, v1, v2) # Realiza a operação matemática específica do operador e armazena o resultado na variável 'resultado'
                    pilha_push(calculadora.operandos, resultado) # O resultado é empilhado na pilha de operandos
                pilha_push(calculadora.operadores, char) # O operador atual é empilhado na pilha de operadores

            elif char == '(': # Se o caractere for '(' ele é empilhado na pilha dos operadores:
                pilha_push(calculadora.operadores, char)

            elif char == ')': # Se o caractere for ')', executa:
                # Enquanto a pilha de operadores não estiver vazia e o operador no topo da pilha não for '(', executa:
                while not pilha_vazia(calculadora.operadores) and pilha_topo(calculadora.operadores) != '(':
                    operador = pilha_pop(calculadora.operadores) #  O operador no topo da pilha de operadores é desempilhado e armazenado na variável operador
                    v2 = pilha_pop(calculadora.operandos) # O operando no topo da pilha de operandos é desempilhado e armazenado na variável 'v2'
                    v1 = pilha_pop(calculadora.operandos) # O operando no topo da pilha de operandos é desempilhado e armazenado na variável 'v1'
                    resultado = calcula_operadores(operador, v1, v2) # Realiza a operação matemática específica do operador e armazena o resultado na variável 'resultado'
                    pilha_push(calculadora.operandos, resultado) # O resultado é empilhado na pilha de operandos
                # Se a pilha de operadores não estiver vazia e o operador no topo da pilha for ‘(’, o operador é desempilhado:     
                if not pilha_vazia(calculadora.operadores) and pilha_topo(calculadora.operadores) == '(': 
                    pilha_pop(calculadora.operadores)

    if num != "": # Se num não estiver vazio, o valor é convertido em inteiro e empilhado na pilha de operandos
        pilha_push(calculadora.operandos, int(num))

    #  Enquanto a pilha de operadores não estiver vazia, executa:
    while not pilha_vazia(calculadora.operadores):
        operador = pilha_pop(calculadora.operadores) # O operador no topo da pilha de operadores é desempilhado e armazenado na variável operador
        v2 = pilha_pop(calculadora.operandos) # O operando no topo da pilha de operandos é desempilhado e armazenado na variável 'v2'
        v1 = pilha_pop(calculadora.operandos) # O operando no topo da pilha de operandos é desempilhado e armazenado na variável 'v1'
        resultado = calcula_operadores(operador, v1, v2) # Realiza a operação matemática específica do operador e armazena o resultado na variável 'resultado'
        pilha_push(calculadora.operandos, resultado) # O resultado é empilhado na pilha de operandos

    return pilha_pop(calculadora.operandos) # O valor no topo da pilha de operandos é desempilhado e retornado, resultado final da expressão!

def main():
    max = 100 # Tamanho máximo fixo definido para cada pilha
    calculadora = Calculadora(max)
    while True: # Cria um loop infinito
        expressao = input("Digite a expressão matemática (ou 'sair' para sair): ") # Solicita a expressão matemática a ser calculada
        if expressao.lower() == 'sair': # Se o usuário digitar 'sair', executa o break que interrompe o loop
            break

        # Chama a função calcula_expressao que recebe a calculadora e a expressão
        # fornecida pelo usuário como parâmetros e armazena o resultado na variável 'resultado'
        resultado = calcula_expressao(calculadora, expressao) 
        print(f"O resultado da expressão {expressao} é {resultado}") # Imprime o valor armazenado na variável 'resultado'

if __name__ == "__main__":
    main()


