opcao1 = []
opcao2 = []
opcao3 = []

def voto ():
    opcao = input("Escolha uma opção: \n[1] Opção 1 \n[2] Opção 2 \n[3] Opção 3\n")
    if opcao == "1":
        opcao1.append(("voto", len(opcao1)+1))
        print("Opção 1 votada.")
    if opcao == "2":
        opcao2.append(("voto", len(opcao2)+1))
        print("Opção 2 votada.")      
    if opcao == "3":
        opcao3.append(("voto", len(opcao3)+1))
        print("Opção 3 votada.")

while True:
    menu = input("Digite [1] para votar ou Digite [2] para resultado: ")
    if menu == "1":
        voto()
    elif menu == "2":
        print(f"Opção 1 tem {len(opcao1)} votos.")
        print(f"Opção 2 tem {len(opcao2)} votos.")
        print(f"Opção 3 tem {len(opcao3)} votos.")
        break
    else:
        print("Opção invalida.")
