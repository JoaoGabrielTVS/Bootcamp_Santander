# Dicionário para agrupar participantes por tema
eventos = {}

# Entrada do número de participantes
n = int(input().strip())

# TODO: Crie um loop para armazenar participantes e seus temas:
for i in range(n):
  nome = input().replace(","," ").strip().split()

  if nome[1] not in list(eventos.keys()): 
    eventos.update({nome[1]:[nome[0]]})
  else:
    nomes_na_lista =  list(eventos.get(nome[1]))
    nomes_na_lista.append(nome[0])
    eventos.update({nome[1]:nomes_na_lista})

    
    



# Exibe os grupos organizados
for tema, participantes in eventos.items():
    print(f"{tema}: {', '.join(participantes)}")