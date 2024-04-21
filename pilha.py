class Pilha: # Define uma classe Pilha
	def __init__(self, max): # Construtor da classe pilha que recebe o tamanho máximo da pilha como parâmetro
		self.max = max # Define o tamanho máximo da pilha
		self.n = 0 # Inicializa o contador de elementos da pilha
		self.vet = [] # Cria a lista vazia 

def pilha_cria(n): 
	p = Pilha(n) # Cria nova instância da Pilha com tamanho máximo n
	p.n = 0 # Inicializa o contador de elementos na pilha
	return p # Retorna a nova pilha criada

def pilha_vazia(p): 
	return p.n == 0 # Retorna se a pilha está vazia (número de elementos igual a 0)

def pilha_push(p, v): # Método para inserir elementos na pilha
	if p.n == p.max: # Verifica se a pilha está cheia (número de elementos coincide com o tamanho máximo definido previamente)
		print("Push error: Pilha está cheia!") # Imprime a mensagem de erro
		return False # Retorna false se a pilha estiver cheia
	p.vet.insert(p.n, v) # Insere o elemento v na posição p.n da lista
	p.n = p.n + 1 # Incremente o contador de elementos após adicionar elemento na lista

def pilha_pop(p): # Método para remover elementos na pilha
	if pilha_vazia(p): # Verifica se a pilha está vazia utilizando o método pilha_vazia
		print("Pop error: Pilha está vazia") # Imprime erro se a lista estiver vazia
		return False # Retorna False se a lista estiver vazia
	v = p.vet[p.n - 1] # Pega o elemento no topo da pilha
	p.n = p.n - 1 # Decrementa o contador de elementos
	return v # Retorna o elemento removido

def pilha_tamanho(p): 
    return p.n # Retorna o número de elementos na pilha

def pilha_topo(p): # Método para pegar o elemento do topo da pilha
    if not pilha_vazia(p): # Verifica se a pilha não está vazia
        return p.vet[p.n - 1] # Pega o elemento que está no topo da pilha
    else:
        return None # Se a pilha estiver vazia, retorna None