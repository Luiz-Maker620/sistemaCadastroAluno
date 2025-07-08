import dao.student_dao as dao
from models.student import Student

def validate_data(Student):

    if Student.age >= 130:
        print("Erro Idade Incorreta")
        return False

       
    if Student.age < 18:
        print("Aceitamos matriculas apenas para alunos maiores de idade")
        return False
    
    return True

def create_record(name:str,email:str,age:int):
    student = Student(name,email,age)
    #Validação dos dados e regras negocio
    #usuario informou  @ no e-mail
    #informou idade > 130
    
    if validate_data(student):
        dao.insert_student(student)
    
def display_record():
    return dao.get_all_students()

def update_record(new_name:str,new_email:str,new_age:int,id:int):
    student = Student(new_name,new_email,new_age,id)
    
    if validate_data(student):
        dao.update_student(student)