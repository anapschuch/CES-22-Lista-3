# O objetivo desse item é criar uma aplicação para um banco que
# irá executar operações de verificar saldo, tirar extrato, realizar
# transferência e sacar dinheiro.
# O histórico de operações é guardado no arquivo 'conta.txt'

import tkinter as tk
import ast


# Classe que cria a interface com o usuário e chama os
# métodos necessários
class ApplicacaoCliente(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.conta = Conta()
        self.pack()
        self.create_widgets()
        self.valor_saque = 0
        self.valor_transferencia = 0
        self.destino_transferencia = ''

    def create_widgets(self):
        self.saque_label = tk.Label(text="Entre valor para sacar: ")
        self.saque_label.pack()

        self.saque_entry = tk.Entry()
        self.saque_entry.pack()

        self.saque_button = tk.Button(self.master)
        self.saque_button["text"] = "Sacar"
        self.saque_button["command"] = self.sacar
        self.saque_button.pack()

        self.extrato = tk.Button(self)
        self.extrato["text"] = "Extrato"
        self.extrato["command"] = self.print_extrato
        self.extrato.pack()

        self.saldo = tk.Button(self)
        self.saldo["text"] = "Saldo"
        self.saldo["command"] = self.print_saldo
        self.saldo.pack()

        self.transferencia_label = tk.Label(text="Entre valor para transferencia:")
        self.transferencia_label.pack()

        self.transferencia_entry = tk.Entry()
        self.transferencia_entry.pack()

        self.transferencia_destino = tk.Label(text="Entre destino para transferência:")
        self.transferencia_destino.pack()

        self.transferencia_destino_entry = tk.Entry()
        self.transferencia_destino_entry.pack()

        self.transferencia_button = tk.Button(text="Transferir")
        self.transferencia_button["command"] = self.transferir
        self.transferencia_button.pack()

    def print_saldo(self):
        print("Saldo: ", self.conta.dados['Saldo'])

    def print_extrato(self):
        print("------- Extrato -------")
        self.conta.component_function()

    def sacar(self):
        self.valor_saque = self.saque_entry.get()
        if int(self.valor_saque) > 0:
            self.conta.change_saldo(-int(self.valor_saque))
            self.conta.append_child(Saque(self.valor_saque).component_function())
            self.conta.salvar()

    def transferir(self):
        self.valor_transferencia = int(self.transferencia_entry.get())
        self.destino_transferencia = self.transferencia_destino_entry.get()
        if self.valor_transferencia > 0:
            self.conta.change_saldo(-self.valor_transferencia)
            self.conta.append_child(
                Transferencia(self.destino_transferencia, self.valor_transferencia).component_function())
        self.conta.salvar()


# Classe genérica para definir
# as operações efetuadas
class Component(object):
    def component_function(self):
        pass


class Conta(Component):
    def __init__(self):
        self.arquivo = open('conta.txt', 'r')
        self.dados = self.arquivo.read()
        self.dados = ast.literal_eval(self.dados)
        self.movimentacoes = self.dados["Extrato"]
        self.extrato = list(self.movimentacoes)

    def append_child(self, movimentacao):
        self.extrato.append(movimentacao)

    def component_function(self):
        for i in range(0, len(self.extrato)):
            print(self.extrato[i])

    def change_saldo(self, diferenca):
        self.dados["Saldo"] += diferenca

    def salvar(self):
        self.arquivo = open('conta.txt', 'w')
        self.dados["Extrato"] = self.extrato
        self.arquivo.write(str(self.dados))
        self.arquivo.close()


class Transferencia(Component):
    def __init__(self, destino, valor):
        self.destino = destino
        self.valor = valor

    def component_function(self):
        mes = "Transferência para " + str(self.destino) + ". Valor: " + str(self.valor)
        print(mes)
        return mes


class Saque(Component):
    def __init__(self, valor):
        self.valor = int(valor)

    def component_function(self):
        mes = "Saque no valor de "
        print(mes + str(self.valor))
        return mes + str(self.valor)


root = tk.Tk()
app = ApplicacaoCliente(master=root)
app.mainloop()
