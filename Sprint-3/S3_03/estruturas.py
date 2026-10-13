class Fila:
    def __init__(self):
        self.itens = []

    def enqueue(self, valor):
        self.itens.append(valor)

    def dequeue(self):
        if not self.itens:
            return None
        return self.itens.pop(0)


class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None


class ListaEncadeada:
    def __init__(self):
        self.inicio = None

    def inserir_final(self, valor):
        novo = No(valor)
        if self.inicio is None:
            self.inicio = novo
            return
        atual = self.inicio
        while atual.proximo is not None:
            atual = atual.proximo
        atual.proximo = novo

    def remover(self, valor):
        anterior = None
        atual = self.inicio
        while atual is not None:
            if atual.valor == valor:
                if anterior is None:
                    self.inicio = atual.proximo
                else:
                    anterior.proximo = atual.proximo
                return True
            anterior = atual
            atual = atual.proximo
        return False

    def valores(self):
        resultado = []
        atual = self.inicio
        while atual is not None:
            resultado.append(atual.valor)
            atual = atual.proximo
        return resultado


fila = Fila()
fila.enqueue("Ativo 1")
fila.enqueue("Ativo 2")
print("Fila FIFO - removido:", fila.dequeue())
lista = ListaEncadeada()
for ativo in ["Notebook", "Servidor", "Roteador"]:
    lista.inserir_final(ativo)
lista.remover("Servidor")
print("Lista encadeada:", lista.valores())
print("Fila: inserir O(1); remover do início O(n) nesta implementação com lista Python.")
print("Lista encadeada: busca e remoção O(n); inserção no fim O(n) sem referência ao último nó.")
