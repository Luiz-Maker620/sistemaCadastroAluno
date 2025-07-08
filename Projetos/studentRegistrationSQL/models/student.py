#Essa classe/Objeto aluno é OO Orientado a Objeto

class Student:
    #metodo construtor da classe Aluno/Student e ele é um metodo epecial 
    def __init__(self,name,email,age,id=None):
        self.id = id
        self.name = name 
        self.email = email
        self.age = age 
        

def __repr__(self):
    return f"Student(id={self.id}, Name={self.name}, Email={self.email}, age={self.age})"
