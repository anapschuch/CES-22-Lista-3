# Simulador de estradas: desenvolvimento de uma classe
# de veículos, com subclasses para diferentes tipos (caminhões,
# automóveis, ...). Cada veículo poderá ter motorização elétrica,
# híbrida e motor de combustão.


from abc import abstractmethod


class Motorizacao:
    """Interface para os tipos de motorizacao"""

    @abstractmethod
    def verificar_consumo(self):
        pass


class Eletrica(Motorizacao):
    """Classe que implementa a motorização elétrica"""

    def verificar_consumo(self):
        print("Consumo da motorização elétrica")


class Hibrida(Motorizacao):
    """Classe que implementa a motorização híbrida"""

    def verificar_consumo(self):
        print("Consumo da motorização híbrida")


class Combustao(Motorizacao):
    """Classe que implementa a motorização a combustão"""

    def verificar_consumo(self):
        print("Consumo da motorização a combustão")


class Transporte:
    """ Interface para definir os métodos necessários em
     todos os meios de transporte"""

    def __init__(self, tipo_motor: Motorizacao):
        self.motorizacao = tipo_motor

    @abstractmethod
    def mover_veiculo(self):
        pass

    @abstractmethod
    def fazer_manutencao(self):
        pass


class Caminhao(Transporte):
    """Classe para caminhões"""

    def __init__(self, tipo_motor: Motorizacao):
        super().__init__(tipo_motor)

    def mover_veiculo(self):
        print("Caminhao moveu para frente")

    def fazer_manutencao(self):
        print("Parametros do caminhão verificados e corrigidos")


class Automovel(Transporte):
    """Classe para os automóveis"""

    def __init__(self, tipo_motor: Motorizacao):
        super().__init__(tipo_motor)

    def mover_veiculo(self):
        print("Automóvel moveu para frente")

    def fazer_manutencao(self):
        print("Manutenção do automóvel concluída")


# Testando um caminhão com motorização elétrica

transporte = Caminhao(Eletrica())
transporte.mover_veiculo()
# terminal: Caminhao moveu para frente

transporte.motorizacao.verificar_consumo()
# terminal: Consumo da motorização elétrica
