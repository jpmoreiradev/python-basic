import numpy as np

class VetorOrdenado():
  def __init__(self, capacidade):
    self.capacidade = capacidade
    self.ultimaPosicao = -1
    self.valores = np.empty(self.capacidade, dtype=int)

  def imprime(self):
    if self.ultimaPosicao == -1:
      print('O vetor está vazio')
    else:
      for i in range(self.ultimaPosicao + 1):
        print(i, ' - ', self.valores[i])

  def insere(self, valor):
    if self.ultimaPosicao == self.capacidade - 1:
      print('Capacidade máxima atingida')
      return

    posicao = 0
    for i in range(self.ultimaPosicao + 1):
      posicao = i
      if self.valores[i] > valor:
        break
      if i == self.ultimaPosicao:
        posicao = i + 1

    x = self.ultimaPosicao
    while x >= posicao:
      self.valores[x + 1] = self.valores[x]
      x = x - 1
    self.valores[posicao] = valor
    self.ultimaPosicao = self.ultimaPosicao + 1

  def pesquisar(self, valor):
    for i in range(self.ultimaPosicao + 1):
      if self.valores[i] > valor:
        return -1
      if self.valores[i] == valor:
        return i


