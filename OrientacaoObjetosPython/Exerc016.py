# superclasse
class Super:
    def hello(self):
        print("Olá, sou a superclasse!")
# subclasse
class Sub (Super):
    def hello(self):
        print("Olá, sou a subclasse!")
# Subsubclasse
class Subsub (Sub):
    # todos com método de mesmo nome hello
    def hello(self):
        print("Olá, sou a subsubclasse!")

# instaciams o objeto da Susub
teste = Subsub()
# Assim, ele vai mostrar o da classe instanciada acima no caso Subsub 
teste.hello()
