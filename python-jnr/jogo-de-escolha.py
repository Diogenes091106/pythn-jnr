import random
import time

def iniciar_jogo():
    print("Bem-vindo(a) ao Jogo de Aventura na Floresta Mágica!")
    print("Você está prestes a entrar em uma floresta misteriosa onde encontrará criaturas estranhas, tesouros escondidos e armadilhas perigosas.")
    print("Tome suas decisões com cuidado, pois cada escolha pode ser a sua última!\n")
    time.sleep(2)
    comecar_aventura()

def comecar_aventura():
    print("Você entra na floresta e chega a uma encruzilhada.")
    time.sleep(1)
    print("1. Seguir para a esquerda, onde parece mais escuro e assustador.")
    print("2. Seguir para a direita, onde há uma leve trilha iluminada pelo sol.\n")
    
    escolha = input("Escolha o caminho (1 ou 2): ")
    if escolha == "1":
        encontro_ogro()
    elif escolha == "2":
        encontrar_tesouro()
    else:
        print("Opção inválida! Tente novamente.\n")
        comecar_aventura()

def encontro_ogro():
    print("\nVocê escolheu o caminho da esquerda e, após caminhar por alguns minutos, encontra um ogro enorme bloqueando o caminho.")
    time.sleep(1)
    print("1. Tentar fugir silenciosamente.")
    print("2. Enfrentar o ogro com sua espada.")
    
    escolha = input("Escolha sua ação (1 ou 2): ")
    if escolha == "1":
        fugir()
    elif escolha == "2":
        lutar_com_ogro()
    else:
        print("Opção inválida! Tente novamente.\n")
        encontro_ogro()

def fugir():
    print("\nVocê tenta fugir silenciosamente, mas pisa em um galho seco, e o ogro te vê!")
    time.sleep(1)
    if random.choice([True, False]):
        print("Por sorte, o ogro é lento e você consegue escapar com vida!\n")
        encontrar_tesouro()
    else:
        print("O ogro te alcança e... bem, parece que a aventura terminou aqui para você.\nGame Over.")
        reiniciar()

def lutar_com_ogro():
    print("\nVocê decide enfrentar o ogro com bravura!")
    time.sleep(1)
    if random.randint(1, 10) > 5:
        print("Você derrota o ogro em uma batalha épica! Parabéns!\n")
        encontrar_tesouro()
    else:
        print("O ogro é muito forte, e você não consegue vencê-lo...\nGame Over.")
        reiniciar()

def encontrar_tesouro():
    print("\nVocê segue pelo caminho e encontra um baú antigo escondido entre as árvores.")
    time.sleep(1)
    print("1. Abrir o baú.")
    print("2. Ignorar o baú e seguir adiante.")
    
    escolha = input("Escolha sua ação (1 ou 2): ")
    if escolha == "1":
        abrir_bau()
    elif escolha == "2":
        caminho_final()
    else:
        print("Opção inválida! Tente novamente.\n")
        encontrar_tesouro()

def abrir_bau():
    print("\nVocê abre o baú e encontra...")
    time.sleep(2)
    if random.choice([True, False]):
        print("Um tesouro brilhante! Parabéns, você ficou rico e completou a aventura com sucesso!")
    else:
        print("Uma armadilha! Você caiu em um buraco escondido e... Game Over.")
    reiniciar()

def caminho_final():
    print("\nVocê escolhe seguir adiante e sai da floresta em segurança.")
    time.sleep(1)
    print("Parabéns, você completou a aventura e saiu da floresta são e salvo!\n")
    reiniciar()

def reiniciar():
    escolha = input("Deseja jogar novamente? (s/n): ").lower()
    if escolha == 's':
        iniciar_jogo()
    else:
        print("Obrigado por jogar! Até a próxima aventura!")

if __name__ == "__main__":
    iniciar_jogo()
