def voto ():
    opcao = input("Escolha uma opção: \n[1] Opção 1 \n[2] Opção 2 \n[3] Opção 3\n")
    if opcao == "1":
        print("Opção 1 votada.")
    if opcao == "2":
        print("Opção 2 votada.")
    if opcao == "3":
        print("Opção 3 votada.")

while True:
    menu = input("Digite [1] para votar ou Digite [2] para sair: ")
    if menu == "1":
        voto()
    elif menu == "2":
        break
    else:
        print("Opção invalida.")
        