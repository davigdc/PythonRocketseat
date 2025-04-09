def adicionar_contato(agenda, nome_contato, telefone_contato, email_contato):
    # estrutura do contato: {"nome": "nome do contato, "telefone": "número de teleforne", "email": "email do contato", "favorito": False}
    contato = {
        "nome": nome_contato,
        "telefone": telefone_contato,
        "email": email_contato,
        "favorito": False,
    }
    agenda.append(contato)
    print(f"Contato {nome_contato} adicionado com sucesso!")
    return


def ver_agenda(agenda, apenas_favoritos=False):
    print("\nLista de contatos:")
    for indice, contato in enumerate(agenda, start=1):
        favorito = "✓" if contato["favorito"] else " "
        nome_contato = contato["nome"]
        telefone_contato = contato["telefone"]
        email_contato = contato["email"]
        resposta = f"{indice}. [{favorito}] - {nome_contato} - {telefone_contato} - {email_contato}"
        if apenas_favoritos:
            if contato["favorito"]:
                print(resposta)
        else:
            print(resposta)
    return


def valida_indice_ajustado(agenda, indice_ajustado):
    if indice_ajustado >= 0 and indice_ajustado < len(agenda):
        return True
    else:
        return False


def atualizar_contato(agenda, indice_contato):
    indice_contato_ajustado = int(indice_contato) - 1
    if valida_indice_ajustado(agenda, indice_contato_ajustado):
        print(
            "Qual campo deste contato desejas atualizar?\n1. Nome\n2. Telefone\n3. Email"
        )
        escolha = input("Digite sua escolha: ")
        if escolha == "1":
            opcao = "nome"
        elif escolha == "2":
            opcao = "telefone"
        elif escolha == "3":
            opcao = "email"
        else:
            print("Opção inválida.")
            return

        novo_valor = input("Digite o novo valor: ")
        agenda[indice_contato_ajustado][opcao] = novo_valor
        print(f"Contato {indice_contato} atualizado!")
    else:
        print("Índice de tarefa inválido.")
    return


def favoritar_contato(agenda, indice_contato):
    indice_contato_ajustado = int(indice_contato) - 1
    if valida_indice_ajustado(agenda, indice_contato_ajustado):
        agenda[indice_contato_ajustado]["favorito"] = (
            True if not agenda[indice_contato_ajustado]["favorito"] else False
        )
        print(f"Contato atualizado!")
    else:
        print("Índice de tarefa inválido.")
    return


def deletar_contato(agenda, indice_contato):
    indice_contato_ajustado = int(indice_contato) - 1
    if valida_indice_ajustado(agenda, indice_contato_ajustado):
        agenda.pop(indice_contato_ajustado)
        print("Contato removido!")
    else:
        print("Índice de tarefa inválido.")
    return


agenda = []
while True:
    print("\nMenu do Gerenciador de Agenda:")
    print("1. Adicionar contato")
    print("2. Ver contatos")
    print("3. Atualizar contato")
    print("4. Marcar/Desmarcar contato como favorito")
    print("5. Ver contatos favoritos")
    print("6. Deletar contato")
    print("7. Sair")

    escolha = input("Digite sua escolha: ")

    if escolha == "1":
        nome_contato = input("Nome do contato: ")
        telefone_contato = input("Telefone do contato: ")
        email_contato = input("Email do contato: ")
        adicionar_contato(agenda, nome_contato, telefone_contato, email_contato)
    elif escolha == "2":
        ver_agenda(agenda)
    elif escolha == "3":
        ver_agenda(agenda)
        indice_contato = input("Digite o número do contato que deseja atualizar: ")
        atualizar_contato(agenda, indice_contato)
    elif escolha == "4":
        ver_agenda(agenda)
        indice_contato = input(
            "Digite o número do contato para marcar/desmarcar como favorito: "
        )
        favoritar_contato(agenda, indice_contato)
    elif escolha == "5":
        ver_agenda(agenda, True)
    elif escolha == "6":
        ver_agenda(agenda)
        indice_contato = input("Digite o número do contato para apagar: ")
        deletar_contato(agenda, indice_contato)
    elif escolha == "7":
        print("Finalizando...")
        break
    else:
        print("Opção inválida.")
