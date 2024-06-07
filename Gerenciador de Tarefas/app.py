import os

tarefas = []

def voltar_menu():
    input('Digite qualquer tecla para voltar ao menu princial: ')
    main()

def exibir_menu():
    print('1. Adicionar Tarefa')
    print('2. Listar Tarefas')
    print('3. Marcar Tarefa como Conluída')
    print('4. Remover Tarefa')
    print('5. Sair')

def adicionar_tarefa():
    titulo = input('\nDigite o título da sua tarefa: ')
    tarefa = {'titulo': titulo, 'concluida':False}
    tarefas.append(tarefa)
    print(f'Tarefa "{titulo}" adicionada com sucesso!\n')
    voltar_menu()

def listar_tarefas():
    print('Tarefas: \n')
    for i, tarefa in enumerate(tarefas):
        status = 'Concluída' if tarefa['concluida'] else 'Pendente'
        print(f'{i+1}. {tarefa['titulo']} - {status}')

def marcar_concluida():
    listar_tarefas()
    numero = int(input('Digite o número da tarefa que deseja marcar como concluída: '))
    if 0 < numero <= len(tarefas):
        tarefas[numero-1]['concluida'] = True
        print(f'Parabéns! A tarefa "{tarefas[numero-1]['titulo']}" foi concluída com sucesso.')
    else: print('Essa tarefa não existe.')
    voltar_menu()

def remover_tarefa():
    listar_tarefas()
    numero = int(input('Digite o número da tarefa que você gostaria de remover: '))
    if 0 < numero <= len(tarefas):
        tarefa = tarefas.pop(numero-1)
        print(f'Tarefa "{tarefa['titulo']} removida com sucesso!\n"')
    else: print('Essa tarefa não existe.')
    voltar_menu()

def main():
    os.system('cls')
    exibir_menu()
    opcao = int(input('Escolha uma opção: '))
    if opcao == 1:
        adicionar_tarefa()
    elif opcao == 2:
        listar_tarefas()
        voltar_menu()
    elif opcao == 3:
        marcar_concluida()
    elif opcao == 4:
        remover_tarefa()
    elif opcao == 5:
        print("Saindo do app")
    else:
        print("Opção inválida!")
        voltar_menu()

if __name__ == '__main__':
    main()