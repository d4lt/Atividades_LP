import json

def save_tarefas(tarefas):
    for tarefa in tarefas:
        nome_tarefa = list(tarefa.keys())[0]
        tarefa[nome_tarefa]['data'] = tarefa[nome_tarefa]['data'].strftime('%d-%m-%Y')
    
    try:
        with open('tarefas.json', 'w') as file:
            json.dump(tarefas, file, indent=4)
    except Exception as e:
        print("Erro ao salvar tarefas:", e)