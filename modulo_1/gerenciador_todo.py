def adicionar_tarefas(tarefas, nome_tarefa):
    # estrutura nova tarefa: {"tarefa": "nome da tarefa", "completada": False}
    tarefa = {"tarefa": nome_tarefa, "completada": False}
    tarefas.append(tarefa)
    print(f"Tarefa {nome_tarefa} foi adicionada com sucesso")
    return


def ver_tarefas(tarefas):
    print("\nLista de tarefas:")
    for indice, tarefa in enumerate(tarefas, start=1):
        status = "✓" if tarefa["completada"] else " "
        nome_tarefa = tarefa["tarefa"]
        print(f"{indice}. [{status}] {nome_tarefa}")
    return


def valida_indice_ajustado(tarefas, indice_ajustado):
    if indice_ajustado >= 0 and indice_ajustado < len(tarefas):
        return True
    else:
        return False


def deletar_tarefa(tarefas, indice_tarefa):
    indice_tarefa_ajustado = int(indice_tarefa) - 1
    if valida_indice_ajustado(tarefas, indice_tarefa_ajustado):
        tarefas.pop(indice_tarefa_ajustado)
        print(f"Tarefa {indice_tarefa} deletada!")
    else:
        print("Índice de tarefa inválido.")
    return


def atualizar_nome_tarefa(tarefas, indice_tarefa, novo_nome_tarefa):
    indice_tarefa_ajustado = int(indice_tarefa) - 1
    if valida_indice_ajustado(tarefas, indice_tarefa_ajustado):
        tarefas[indice_tarefa_ajustado]["tarefa"] = novo_nome_tarefa
        print(f"Tarefa {indice_tarefa} atualizada para {novo_nome_tarefa}!")
    else:
        print("Índice de tarefa inválido.")
    return


def completar_tarefa(tarefas, indice_tarefa):
    indice_tarefa_ajustado = int(indice_tarefa) - 1
    if valida_indice_ajustado(tarefas, indice_tarefa_ajustado):
        tarefas[indice_tarefa_ajustado]["completada"] = True
        print(f"Tarefa {indice_tarefa_ajustado} marcada como completada!")
    else:
        print("Índice de tarefa inválido.")
    return


def deletar_tarefas_completadas(tarefas):
    for tarefa in tarefas:
        if tarefa["completada"]:
            tarefas.remove(tarefa)
    print("Tarefas completadas foram deletadas!")
    return


tarefas = []
while True:
    print("\nMenu do Gerenciador de Lista de tarefas:")
    print("1. Adicionar tarefa")
    print("2. Ver tarefas")
    print("3. Atualizar tarefa")
    print("4. Completar tarefa")
    print("5. Deletar tarefa")
    print("6. Deletar tarefas completadas")
    print("7. Sair")

    escolha = input("Digite sua escolha: ")

    if escolha == "1":
        nome_tarefa = input("Nome da tarefa a ser adicionada: ")
        adicionar_tarefas(tarefas, nome_tarefa)
    elif escolha == "2":
        ver_tarefas(tarefas)
    elif escolha == "3":
        ver_tarefas(tarefas)
        indice_tarefa = input("Digite o número da tarefa que deseja atualizar: ")
        novo_nome = input("Digite o novo nome da tarefa: ")
        atualizar_nome_tarefa(tarefas, indice_tarefa, novo_nome)
    elif escolha == "4":
        ver_tarefas(tarefas)
        indice_tarefa = input("Digite o número da tarefa que deseja completar: ")
        completar_tarefa(tarefas, indice_tarefa)
    elif escolha == "5":
        ver_tarefas(tarefas)
        indice_tarefa = input("Digite o número da tarefa que deseja deletar: ")
        deletar_tarefa(tarefas, indice_tarefa)
    elif escolha == "6":
        deletar_tarefas_completadas(tarefas)
        ver_tarefas(tarefas)
    elif escolha == "7":
        print("Finalizando...")
        break
    else:
        print("Opção inválida.")
