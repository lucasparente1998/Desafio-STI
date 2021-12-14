import pandas as pd
from src.aluno import Aluno
from src.disciplina import Disciplina
from src.nota import Nota

#Lê o arquivo
doc = pd.read_csv('./base_de_dados/notas.csv')

# Retorna lista de alunos
def listaAluno():
	#Criando aluno        #Removendo matriculas repetidas
	matriculas = doc['MATRICULA'].drop_duplicates()
	lista_aluno = []
	for i in matriculas:
		aluno = Aluno()
		aluno.setMatricula(i)
		lista_aluno.append(aluno)
	return lista_aluno

# Retorna lista de disciplinas
def listaDisciplina():
	#Criando disciplina         #Removendo pelas disciplinas repetidas
	disciplinas = doc.drop_duplicates(subset = ['COD_DISCIPLINA'])
	lista_disciplina = []
	for i,row in disciplinas.iterrows():
		disciplina = Disciplina()
		#definindo os valores
		disciplina.setCodDisciplina(row['COD_DISCIPLINA'])
		disciplina.setCodCurso(row['COD_CURSO'])
		disciplina.setCargaHoraria(row['CARGA_HORARIA'])
		#adicionando a lista de disciplinas
		lista_disciplina.append(disciplina)
	return lista_disciplina

# Retorna lista de notas
def listaNota(lista_aluno,lista_disciplina):
	#criando nota 
	lista_notas = []
	for i, row in doc.iterrows():
		nota = Nota()

		for a in lista_aluno:
			if row['MATRICULA'] == a.matricula:
				aluno_aux = a

		for d in lista_disciplina:
			if row['COD_DISCIPLINA'] == d.cod_disciplina:
				disciplina_aux = d

		#definindo os valores
		nota.setAluno(aluno_aux)
		nota.setDisciplina(disciplina_aux)
		nota.setNota(row['NOTA'])

		lista_notas.append(nota)
	return lista_notas	
	

def listaCurso():
	cursos = doc['COD_CURSO'].drop_duplicates()
	lista_curso = []
	for curso in cursos:
		lista_curso.append(curso)
	return sorted(lista_curso)



