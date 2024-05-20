# Hangman Game (Jogo da Forca) 
# Programação Orientada a Objetos

# Import
import random

# Board (tabuleiro)
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']


# Classe
class Hangman:

     print("----------Hangman----------")

	# Método Construtor
     def __init__(self):
          self.listaPalavras = ["bianca", "morango", "yourlove", "pitoco", "lucas"]               
          self.palavra = random.choice(self.listaPalavras)               
          self.chances = 6
          self.erradas = []
          self.certas = []
          self.descobrir = ["_" for letra in self.palavra]

	# Método para adivinhar a letra
     def adivLetra(self):
          while self.chances > 0:
               hangm.imprimiboard()
               print(" ".join(self.descobrir))
               print("\nChances restantes: ",  self.chances)
               print("\nLetras corretas: ", " ".join(self.certas))
               print("Erros: ",  " ".join(self.erradas))

               if "_" not in self.descobrir:
                    hangm.venceu()
                    break

               tenta = input("Digite uma letra:  ").lower()

               if tenta in self.palavra:
                    index = 0
                    self.certas.append(tenta)
                    for i in self.palavra:
                         if tenta == i:
                              self.descobrir[index] = i
                         index += 1
               else:
                    self.chances -= 1
                    self.erradas.append(tenta)
          if self.chances == 0:
               hangm.imprimiboard()
               print(" ".join(self.descobrir))
               print("\nChances restantes: ",  self.chances)
               print("Erros: ",  " ".join(self.erradas))
               hangm.fimJogo()
	# Método para verificar se o jogo terminou
     def fimJogo(self):
               print("Você perdeu, a palavra era: ", self.palavra)

	# Método para verificar se o jogador venceu
     def venceu(self):
          print("Parabéns você ganhou. A palavra era: ", self.palavra)
	# Método para não mostrar a letra no board
		
	# Método para checar o status do game e imprimir o board na tela
     def imprimiboard(self):
          if self.chances == 6:
               print(board[0])
          elif self.chances == 5:
               print(board[1])
          elif self.chances == 4:
               print(board[2])
          elif self.chances == 3:
               print(board[3])
          elif self.chances == 2:
               print(board[4])
          elif self.chances == 1:
               print(board[5])
          else:
               print(board[6])

hangm= Hangman()
hangm.adivLetra()