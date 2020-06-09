# Objetivo: implementar a q1 com Design Pattern Fábrica


from abc import abstractmethod


class Transporte:
    """ Interface para definir os métodos necessários em
     todos os meios de transporte"""

    @abstractmethod
    def mover_veiculo(self):
        pass

    @abstractmethod
    def fazer_manutencao(self):
        pass


class Caminhao(Transporte):
    """Classe para caminhões"""

    def mover_veiculo(self):
        print("Caminhao moveu para frente")

    def fazer_manutencao(self):
        print("Parametros do caminhão verificados e corrigidos")


class Automovel(Transporte):
    """Classe para os automóveis"""

    def mover_veiculo(self):
        print("Automóvel moveu para frente")

    def fazer_manutencao(self):
        print("Manutenção do automóvel concluída")


class EscolherTransporte:
    """Classe que define Transporte"""

    @staticmethod
    def criar_transporte(is_caminhao):
        if is_caminhao:
            return Caminhao()
        else:
            return Automovel()


#Criar um caminhao
transporte = EscolherTransporte.criar_transporte(True)
transporte.mover_veiculo()
# terminal: Caminhao moveu para frente

transporte.fazer_manutencao()
# terminal: Parametros do caminhão verificados e corrigidos

print()
#Criar um automovel
transporte2 = EscolherTransporte.criar_transporte(False)
transporte2.mover_veiculo()
# terminal: Automóvel moveu para frente

transporte2.fazer_manutencao()
# terminal: Manutenção do automóvel concluída