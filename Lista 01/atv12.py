''' 12. Peça ao usuário a quantidade de turmas e a quantidade total de alunos. Informe a
média de alunos por turma, mas avise se alguma turma tiver mais de 40 alunos.'''
turmas = int(input('Quantidade de turmas: '))
total_de_alunos = int(input('Quantidade total de alunos: '))
media_por_turma = total_de_alunos // turmas
print(f'Teremos {media_por_turma} alunos por turma.')

if media_por_turma > 40:
    print('AVISO: Teremos uma turma com mais de 40 alunos.')