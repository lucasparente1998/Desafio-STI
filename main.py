from src.leArquivo import listaAluno,listaDisciplina,listaNota,listaCurso
from src.funcoes import calculaCr,calculaMediaCurso,imprimeCrAlunos,imprimeCrMedioCurso

#Criando as listas de alunos, disciplinas, notas e curso
lista_aluno = listaAluno()
lista_disciplina = listaDisciplina()
lista_nota = listaNota(lista_aluno,lista_disciplina)
lista_curso = listaCurso()


#Imprime Cr de cada aluno
lista_GUI = imprimeCrAlunos(lista_aluno,lista_nota,lista_disciplina)


#Imprime Cr medio do curso
lista_GUI_curso = imprimeCrMedioCurso(lista_curso,lista_nota,lista_disciplina)











