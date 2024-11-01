MaxVagas = 100
vagas = []
def exibir_vagas():
    result = MaxVagas - len(vagas)
    if result <0:
        print(f"Não há vagas disponíveis.")
    else:
        print(f"Há {result} vagas disponíveis.")
        
def estacionar_veiculo(placa):
    if len(placa) == 7:   
        if placa not in vagas:
            vagas.append(placa)
            print("Veiculo registrado.")
        else:
            print("Veiculo ja registrado.")
    else:
        print("Formato de placa incorreto. ") 

def remover_veiculo(placa):
    if placa in vagas:
        vagas.remove(placa)
        print(f"Veículo {placa} removido.")
    else:
        print("Veículo não encontrado.")
        

while True:
    menu = input("-------------------------------------------------\nDigite: \n[1] para Exibir Vagas. \n[2] para Estacionar Veiculo. \n[3] para Remover Veiculos. \n[4] para sair.\n-------------------------------------------------\n")
    if menu == "1":
        exibir_vagas()
    elif menu == "2":
        placa = input("Digite a placa do veiculo: ")
        estacionar_veiculo(placa)
    elif menu == "3":
        placa = input("Digite a placa do veiculo: ")
        remover_veiculo(placa)
    elif menu == "4":
        break
    else:
        print("Comando invalido.")