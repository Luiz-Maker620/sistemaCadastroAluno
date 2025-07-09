import sys 
from pathlib import Path 

current_file = Path(__file__)
#pega o caminho do arquivo atual no caso de main.py

project_root = Path(__file__).parent.parent

#adiciona a raiz do projeto no path do python 
sys.path.append(str(project_root))




from db.connection import connect_db, close_db
from services.student_service import StudentService

def show_menu():
    print("\n======== Sistema de Cadastro de Alunos ====")

    print("1. Cadastrar Aluno")
    print("2. Listar Aluno")
    print("5. Sair")

    print("=============================================")


def main():
    connect_db()

    service = StudentService()

    while True:
        show_menu()

        opcao = input("Escolha a opcao:")

        if opcao == "1":
            name = input("Informe o nome do Aluno:")
            age = int(input("Informe a Idade do Aluno:"))
            email = input("Informe Email:")
            service.register_student(name,age,email)
            print("Aluno Cadastrado com Sucesso!!!")
            
        elif opcao == "5":
            print("Saindo do sistema")
            break
        else:
            print("Opcao Invalida")

    close_db()

if __name__ == "__main__":
    main()