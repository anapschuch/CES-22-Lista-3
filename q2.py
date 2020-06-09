# Utilizando o exemplo de CoffeShop com padrão Decorador,
# vamos criar um exemplo que constroi pizzas.


class IngredientePizza:
    def getDescricao(self):
        return self.__class__.__name__

    def getCustoTotal(self):
        return self.__class__.custo


class Massa(IngredientePizza):
    custo = 0.0


class Decorador(IngredientePizza):
    def __init__(self, ingrediente_pizza: IngredientePizza):
        self.componente = ingrediente_pizza

    def getCustoTotal(self):
        return self.componente.getCustoTotal() + IngredientePizza.getCustoTotal(self)

    def getDescricao(self):
        return self.componente.getDescricao() + " " + IngredientePizza.getDescricao(self)


class Queijo(Decorador):
    custo = 3.0

    def __init__(self, ingrediente_pizza):
        super().__init__(ingrediente_pizza)


class Presunto(Decorador):
    custo = 2.0

    def __init__(self, ingrediente_pizza):
        super().__init__(ingrediente_pizza)


class Tomate(Decorador):
    custo = 1.5

    def __init__(self, ingrediente_pizza):
        super().__init__(ingrediente_pizza)


# Testando uma pizza com presunto, tomate e queijo:
pizza = Presunto(Queijo(Tomate(Massa())))
print(pizza.getDescricao() + ": R$ ", str(pizza.getCustoTotal()))
# terminal: Massa Tomate Queijo Presunto: R$  6.5

# Testando uma pizza de queijo:
pizza2 = Queijo(Massa())
print(pizza2.getDescricao() + ": R$ ", str(pizza2.getCustoTotal()))
# terminal: Massa Queijo: R$  3.0
