while True:
    print("\n1-Adicionar 2-Listar 0-Sair")
    op = input("Escolha: ")

    if op == "1":
        tarefa = input("Digite a tarefa: ")
        with open("tarefas.txt", "a") as f:
            f.write(tarefa + "\n")

    elif op == "2":
        with open("tarefas.txt", "r") as f:
            tarefas = f.readlines()
            for i, t in enumerate(tarefas, 1):
                print(i, "-", t.strip())

    elif op == "0":
        break