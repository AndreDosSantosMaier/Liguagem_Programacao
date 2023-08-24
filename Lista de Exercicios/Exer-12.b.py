""" Faça 4 listas:
A. Filmes
B. Jogos
C. Livros
D. Esporte
a. Adicione no mínimo 2 itens em cada lista.
b. Crie uma lista das 4 listas criadas acima.
c. Acesse (mostrar) algum item da lista livros.
d. Remova um item da lista esporte.
 """
filmes = []
jogos = []
livros = []
esporte = []
filmes.append("titanic")
filmes.append("titanico")
jogos.append("super mario")
jogos.append("Sonic")
livros.append("livro legal")
livros.append("livro chato")
esporte.append("futebol")
esporte.append("futebol americano")
megalista =filmes+jogos+livros+esporte
print(megalista)
print(livros[1]) 
del(esporte[1])

