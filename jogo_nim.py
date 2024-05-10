# Ola isso eh um teste git de 10 de maio d 2024

def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))

        
    #Verificando quem começa
    if n % (m + 1) == 0:
        vezJogador = True
        print("\nVocê começa!")

    else:
        vezJogador = False
        print("\nComputador começa!")


    #Enquanto a quantidade de peças for válidas (maior que 0)
    while n > 0:

        #Condição da vez do jogador e da vez do computador    
        if vezJogador:
            suaJogada = usuario_escolhe_jogada(n, m)
            print(f"Você tirou {suaJogada} peças")
            n = n - suaJogada
            
        else:
            jogadaComputador = computador_escolhe_jogada(n, m)
            print(f"\nO computador tirou {jogadaComputador} peças")
            n = n - jogadaComputador
        vezJogador = not vezJogador

        #Mostrador de quantidade de peças no tabuleiro quando tem 1 peça ou mais
        if n == 1:
            print (f"Agora resta apenas uma peça no tabuleiro.")
        else:
            print(f"Agora restam {n} peças no tabuleiro")


    if n <= 0:
        print("\nFim do jogo! O computador ganhou!")

        
        
def usuario_escolhe_jogada(n, m):
    jogada = int(input("\nQuantas peças você vai tirar? "))

    while not (jogada >= 1 and jogada <= m and jogada <= n):
        print("\nOops! Jogada inválida! Tente de novo.")
        jogada = int(input("\nQuantas peças você vai tirar? "))
         
    return jogada



def computador_escolhe_jogada(n, m):
    tirarPecas = n % (m + 1)

    if tirarPecas >= 1 and tirarPecas <= m:
        return tirarPecas
    
    else:
        return m




def bem_vindo():
    print("Bem-vindo ao jogo do NIM! Escolha: ")

    partidaCond = int(input("1 - para jogar uma partida isolada\n2 - para jogar um campeonato 2: "))

    contador = 0

    if partidaCond == 2:
        while contador < 3:
            contador += 1
            print(f"\n*** Rodada {contador} ****")   
            partida()

        print("\n**** Final do campeonato! ****")
        print("Placar: Você 0 X 3 Computador")
        #levando em consideração que um campeonato tem 3 rodadas e o computador sempre vai ganhar

    else:
       partida()


bem_vindo()
