class Foo:
    def __init__(self, x=None):
        self._x = x

    # Getter
    @property
    def x(self):
        return self._x or 0  # Retorna 0 se _x for None ou 0

    # Setter
    @x.setter
    def x(self, value):
        if value is not None:
            self._x = value
        else:
            print("Erro: valor de 'x' não pode ser None.")

    # Deleter
    @x.deleter
    def x(self):
        self._x = None  # Pode remover o valor de _x, ou atribuir None

# Teste da classe Foo
foo = Foo(10)
print(foo.x)  # Saída: 10

foo.x = 10
print(foo.x)  # Saída: 10

del foo.x
print(foo.x)  # Saída: 0 (porque foi deletado e o valor padrão é 0)

