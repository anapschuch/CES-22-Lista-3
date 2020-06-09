# O objetivo dessa questão é utilizar o Design Pattern State
# para modelar o exemplo de revisão de documento
# O documento poderá estar no estado Draft, Moderation e Published


class State:
    def render(self):
        pass

    def publish(self, user):
        pass


class Draft:
    def render(self):
        print("Documento já está no primeiro estágio")
        return Draft()

    def publish(self, user):
        if user.is_admin:
            print("Documento publicado")
            return Published()
        else:
            print("Documento em moderação")
            return Moderation()


class Moderation:
    def render(self):
        print("Documento retornou ao estado Draft")
        return Draft()

    def publish(self, user):
        if user.is_admin:
            print("Documento publicado pelo admin")
            return Published()
        else:
            print("Somente admin pode aprovar a publicação")
            return Moderation()


class Published:
    def render(self):
        print("Publicação expirada. Documento voltou ao estado Draft")
        return Draft()

    def publish(self, user):
        print("Erro! Documento já está publicado!")
        return Published()


class Document:
    state = None

    def __init__(self):
        self.state = Draft()

    def change_state(self, new_state):
        self.state = new_state

    def render(self):
        self.change_state(self.state.render())

    def publish(self, user):
        new_state = self.state.publish(user)
        self.change_state(new_state)


class User:
    def __init__(self, is_admin):
        self.is_admin = is_admin


# Teste para verificar se as mudanças de estado do
# arquivo estão funcionando

usuario = User(False)
documento = Document()

documento.render()
# terminal: Documento já está no primeiro estágio

documento.publish(usuario)
# terminal: Documento em moderação

admin = User(True)
documento.publish(admin)
# terminal: Documento publicado pelo admin

documento.render()
# terminal: Publicação expirada. Documento voltou ao estado Draft
