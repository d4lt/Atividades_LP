turmas = int(input("Quantidade de turmas: "))
alunos = int(input("Quantidade de alunos: "))

alunos_turma = alunos//turmas

print(f"A quantidade media de alunos por turma será: {alunos_turma}")
if alunos_turma > 40:
    print("As turmas terão mais de 40 alunos!")

