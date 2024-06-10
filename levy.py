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
      if i == self.ultimaPosicao:
        return -1

  def excluir(self, valor):
    posicao = self.pesquisar(valor)
    if posicao == -1:
      return -1
    else:
      for i in range(posicao, self.ultimaPosicao):
        self.valores[i] = self.valores[i + 1]

      self.ultimaPosicao = self.ultimaPosicao - 1

vetor = VetorOrdenado(6)
vetor.imprime()

vetor.insere(3)
vetor.insere(4)
vetor.insere(5)
vetor.insere(6)
vetor.insere(4)


vetor.imprime()

