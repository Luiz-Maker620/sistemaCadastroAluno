import sqlite3
from contextlib import contextmanager

#Constante que indica o caminho para o diretorio do banco de dados
DB_NAME = "C:\Projetos\studentRegistrationSQL\databases\students.db"

def undo(msg:str, e, conexao):
    conexao.rollback()
    print(f"{msg}: {e}")
    raise


@contextmanager
def get_cursor():
    conexao = sqlite3.connect(DB_NAME)
    cursor = conexao.cursor()

    try:
        yield cursor
        conexao.commit()
    except sqlite3.IntegrityError as e:
        conexao.rollback()
        print(f"ocorreu um erro de integridade no banco de dados: {e}")
    except sqlite3.IntegrityError as e:
        conexao.rollback()
        print(f"ocorreu um erro de programacao: {e}")
    except sqlite3.IntegrityError as e:
        conexao.rollback()
        print(f"ocorreu um erro do s. operacional: {e}")
    except sqlite3.IntegrityError as e:
        conexao.rollback()
        print(f"ocorreu um erro de banco de dados:")
    except sqlite3.IntegrityError as e:
        conexao.rollback()
        print(f"Erro inesperado: {e}")
        raise
    finally:
        conexao.close()

def cancelar(conexao):
    conexao.close()

def create_table():
    with get_cursor() as cursor:    
     cursor.execute("""
        CREATE TABLE IF NOT EXISTS aluno( 
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                idade INTEGER
                )
        """)                    