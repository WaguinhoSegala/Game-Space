from tkinter import Tk, simpledialog

nomeestrela = Tk()
nomeestrela.withdraw()

def pedir_nome_estrela():
    nome = simpledialog.askstring("Nome da Estrela", "Digite o nome da estrela (deixe vazio se desconhecida):")
    return nome if nome else "desconhecido"

def salvar_marcacoes(estrelas):
    try:
        with open("marcacoes.txt", "w") as arquivo:
            for pos, nome in estrelas.items():
                arquivo.write(f"{pos[0]},{pos[1]},{nome}\n")
        print("Marcações salvas com sucesso.")
    except Exception as e:
        print(f"Erro ao salvar marcações: {e}")

def carregar_marcacoes():
    estrelas = {}
    try:
        with open("marcacoes.txt", "r") as arquivo:
            for linha in arquivo:
                x, y, nome = linha.strip().split(',')
                estrelas[(int(x), int(y))] = nome
        print("Marcações carregadas com sucesso.")
    except Exception as e:
        print(f"Erro ao carregar marcações: {e}")
    return estrelas

def excluir_marcacoes():
    print("Todas as marcações foram excluídas.")