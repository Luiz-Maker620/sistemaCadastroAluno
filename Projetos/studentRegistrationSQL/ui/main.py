import sys
import os

PROJECT_DIR = "c:\\Projetos\\studentRegistrationSQL\\" 

sys.path.append(os.path.abspath(PROJECT_DIR))

from db.connection import create_table 
import services.student_services as service

def show_students():
    students = service.display_record()

    for student in students:
        print(f"{student.id}, {student.name}, {student.email}, {student.age}")

#Menu principal
def main_menu() -> str:
    print("\n Sistema de Cadastro de Alunos")
    print("1. Cadastrar Aluno")
    print("2. lista de Aluno ")
    print("3. Atualizar Aluno")
    print("4. Excluir Aluno")
    print("5. Sair")

    opcao = input("escolha uma opcao:")
    return opcao


if __name__ == "__main__":
    create_table()
        
    while True:
        opcao = main_menu()
        if opcao == "1":
            name = input("Name:")
            email = input("E-mail:")
            age = int(input("idade:"))
            
            service.create_record(name,email,age)              
        
        elif opcao == "2":    
            show_students()
        
        elif opcao == "3":
            id = int(input("informe o ID do aluno q vc quer atualizar:"))
            name = input("Novo Nome:")
            email = input("Novo Email:")
            age = int(input("Nova Idade:"))
            service.update_record(name,email,age,id)
        
        elif opcao == "4":
             id = input("informe o ID que deseja deletar:")  
       
       
        elif opcao == "5":  
            break
        else:
            print("Opcao Invalida") 
            
print(" Sistema da Cadastro da Aluno")
        