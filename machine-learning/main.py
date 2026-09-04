
class Person:
    def __init__(self,nom,age,ville="Antananarivo"):
        self.nom = nom
        self.age = age
        self.ville = ville
        
    def se_presenter(self):
        print(f"Je suis {self.nom}")
        print(f"J'ai {self.age} ans")
        print(f"J'habite à {self.ville}")
        
    def __str__(self):
        return f"{self.nom} habite à {self.ville} il est né en {2026 - self.age}"
        
class DevOps(Person):
    def __init__(self,language,exp,nom,age,ville):
        super().__init__(nom,age,ville)
        self.lang = language
        self.exp = exp
        
    def greeting(self):
        print(f"Je suis {self.nom} , j'ai {self.age} \n J'habite à {self.ville}")
        print(f"Je metrise {self.lang} ,j'ai {self.exp} ans d'experience !")
        
dev1 = DevOps("Python",3,"NarzoHacker",25,"New york")
dev1.greeting()