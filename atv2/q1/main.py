import datetime
import save_tarefas

tarefas = []

def show_tasks(enumerated=False):
    if not tarefas:
        print("Nenhuma tarefa cadastrada.\n")
    else:
        tarefas.sort( key=lambda x: list(x.values())[0]['data'] )
        
        print()
        for index, tarefa in enumerate(tarefas):
            nome_tarefa = list(tarefa.keys())[0]
            
            if enumerated:
                print(f"{index+1} {nome_tarefa}")
            else:
                data_tarefa = tarefa[nome_tarefa]['data']
                print(f"• {data_tarefa.strftime('%d-%m-%Y')} {nome_tarefa}")


def adicionar_tarefa(name, description, date):
    day, month, year = map(int, date.split())
    try:
        date = datetime.date(year, month, day)     
    except:
        raise Exception("Wrong date formatting")
    
    tarefa = { name: { 'descricao': description, 'data': date } }
    tarefas.append(tarefa)

def expand_tarefa(tarefa_index):
    tarefa = tarefas[tarefa_index]
    nome_tarefa = list(tarefa.keys())[0]
    description_tarefa = tarefa[nome_tarefa]['descricao']
    data_tarefa = tarefa[nome_tarefa]['data']
    
    print(f'\n{nome_tarefa}')
    print(f'Prazo: {data_tarefa}\n')
    print(f"{description_tarefa}\n")
    

def main():
    
    print("\nBem-vindo ao gerenciador de tarefas!\n")
    while True:
        
        if tarefas:
            print("Suas tarefas:")
            show_tasks()
        print("\n[1] Ver tarefa")
        print("[2] Adicionar tarefa")
        print("[3] Marcar tarefa como concluída")
        opcao = input("Escolha uma opção (ou 'sair' para sair): ").strip().lower()
        
        if opcao == '1':
            if tarefas:
                show_tasks(enumerated=True)
                while True:
                    tarefa_index = int(input("Qual tarefa deseja ver? (digite o número): "))
                    if tarefa_index > 0 and tarefa_index <= len(tarefas):
                        expand_tarefa(tarefa_index-1)
                        input("\nPressione Enter para continuar...\n")
                        break
                    else:
                        print("Por favor, escolha um número válido.")
            else:
                print("Nenhuma tarefa cadastrada.\n")
            
        
        if opcao == '2':  
            nome_tarefa = input("\n→ Nome da tarefa:\n").strip()
            descricao_tarefa = input("\n→ Descrição da tarefa:\n").strip()
            while True:
                good_date_format = True
                data_tarefa = input("→ Prazo da tarefa (ex.: 11 09 2007):\n").strip()
                try:
                    adicionar_tarefa(nome_tarefa, descricao_tarefa, data_tarefa)
                except:
                    print("Por favor escreva a data corretamente.")
                    good_date_format = False
                    
                if good_date_format:
                    break

            print("Tarefa adicionada.\n\n")
            
        if opcao == '3':
            if tarefas:
                show_tasks(enumerated=True)
                while True:
                    tarefa_index = int(input("Qual tarefa deseja marcar como concluída? (digite o número): "))
                    if tarefa_index > 0 and tarefa_index <= len(tarefas):
                        tarefas.pop(tarefa_index-1)
                        break
                    else:
                        print("Por favor, escolha um número válido.")
            else:
                print("Nenhuma tarefa cadastrada.\n")
        
        if opcao == 'sair':
            print("\nVolte sempre :)")
            save_tarefas.save_tarefas(tarefas)
            break
        
    

if __name__ == '__main__':
    main()