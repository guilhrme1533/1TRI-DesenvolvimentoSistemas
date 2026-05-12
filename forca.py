def gerar_arquivos():
    temas = {
        "animais": ["abelha", "abutre", "albatroz", "alce", "alpaca", "anaconda", "anta", "aranha", "arara", "asno", "avestruz", "baleia", "barata", "bisao", "bode", "boi", "borboleta", "bufalo", "burro", "cabra", "cachorro", "camaleao", "camelo", "camundongo", "canario", "capivara", "caracol", "caranguejo", "carneiro", "cavalo", "cegonha", "chita", "coala", "cobra", "coelho", "coruja", "corvo", "cupim", "doninha", "egua", "elefante", "esquilo", "estrela", "faisao", "falcao", "foca", "formiga", "gafanhoto", "galinha", "ganso"],
        "frutas": ["abacate", "abacaxi", "acerola", "ameixa", "amora", "banana", "cacau", "caju", "caqui", "carambola", "cereja", "coco", "cupuacu", "damasco", "figo", "framboesa", "goiaba", "graviola", "groselha", "guarana", "jaca", "jambo", "jabuticaba", "kiwi", "laranja", "limao", "litchi", "maca", "mamao", "manga", "mangaba", "maracuja", "melancia", "melao", "mirtilo", "morango", "nectarina", "nespera", "pera", "pessego", "pitanga", "pitaya", "roma", "siriguela", "tangerina", "tâmara", "toranja", "umbú", "uva", "uvalha"],
        "objetos": ["abajur", "agulha", "algema", "alicate", "almofada", "ampulheta", "antena", "anzol", "apagador", "apito", "aquário", "armário", "balança", "balde", "banco", "bandeira", "banqueta", "baralho", "batedeira", "batom", "beliche", "berço", "bicicleta", "binóculo", "bisturi", "bocal", "bússola", "cabide", "cadeira", "caderno", "cajado", "calculadora", "calice", "cama", "caneca", "caneta", "canivete", "capacete", "carimbo", "cartão", "carteira", "celular", "chave", "chicote", "chinelo", "cinzeiro", "clipe", "colchão", "colher", "copo"]
    }
    
    for tema, palavras in temas.items():
        with open(f"{tema}.txt", "w", encoding="utf-8") as arquivo:
            for palavra in palavras:
                arquivo.write(palavra + "\n")

gerar_arquivos()
import random

def jogar_forca():
    print("\n--- JOGO DA FORCA ---")
    print("(1) Animais | (2) Frutas | (3) Objetos")
    opcao = input("Escolha o tema: ")
    
    mapa_temas = {"1": "animais.txt", "2": "frutas.txt", "3": "objetos.txt"}
    arquivo_nome = mapa_temas.get(opcao, "animais.txt")

    # Sorteio da palavra
    palavras = []
    with open(arquivo_nome, "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            palavras.append(linha.strip().upper())
    
    palavra_secreta = random.choice(palavras)
    letras_acertadas = ["_" for _ in palavra_secreta]
    
    enforcou = False
    acertou = False
    erros = 0
    limite_erros = 6

    print(f"Palavra: {' '.join(letras_acertadas)}")

    while not enforcou and not acertou:
        chute = input("\nQual letra? ").strip().upper()

        if chute in palavra_secreta:
            index = 0
            for letra in palavra_secreta:
                if chute == letra:
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1
            print(f"Ops, você errou! Faltam {limite_erros - erros} tentativas.")

        enforcou = erros == limite_erros
        acertou = "_" not in letras_acertadas
        
        print(" ".join(letras_acertadas))

    if acertou:
        print("Parabéns, você ganhou!")
    else:
        print(f"Puxa, você foi enforcado! A palavra era {palavra_secreta}.")

def jogar_adivinhacao():
    print("\n--- JOGO DE ADIVINHAÇÃO ---")
    numero_secreto = random.randint(1, 100)
    tentativas = 0
    
    while True:
        tentativas += 1
        chute = int(input("Chute um número entre 1 e 100: "))
        
        if chute == numero_secreto:
            print(f"Acertou em {tentativas} tentativas!")
            break
        elif chute > numero_secreto:
            print("O número secreto é menor.")
        else:
            print("O número secreto é maior.")

# MENU PRINCIPAL (Laço Infinito)
while True:
    print("\n" + "="*20)
    print("  MENU DE JOGOS  ")
    print("="*20)
    print("(1) Forca")
    print("(2) Adivinhação")
    print("(3) Sair")
    
    escolha = input("O que deseja jogar? ")

    if escolha == "1":
        jogar_forca()
    elif escolha == "2":
        jogar_adivinhacao()
    elif escolha == "3":
        print("Saindo do programa... Até logo!")
        break
    else:
        print("Opção inválida!")