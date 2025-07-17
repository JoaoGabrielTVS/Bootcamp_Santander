class Pedido:
    def __init__(self):
        self.itens = []  
    
    def adicionar_preco(self, preco):
      self.itens.append(preco)
    
    def retornar_preco(self):
        return sum(self.itens)
    
    # TODO: Crie um método chamado adicionar_item que recebe um preço e adiciona à lista de itens:
    
        # TODO: Adicione o preço do item à lista:
          

    # TODO: Crie um método chamado calcular_total que retorna a soma de todos os preços da lista:
    
        # TODO: Retorne a soma de todos os preços
        

quantidade_pedidos = int(input().strip())

pedido = Pedido()

for _ in range(quantidade_pedidos):
    entrada = input().strip()
    nome, preco = entrada.rsplit(" ", 1)
    pedido.adicionar_preco(float(preco))
    #TODO: Chame o método adicionar_item corretamente: 
print(f"{pedido.retornar_preco():.2f}")
# TODO: Exiba o total formatado com duas casas decimais: