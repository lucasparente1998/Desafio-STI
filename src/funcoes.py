def calculaCr(aluno,lista_nota,lista_disciplina):
	soma_carga_horaria = 0
	soma_notas = 0
	for notas in lista_nota:
		if aluno == notas.aluno:
			for disciplina in lista_disciplina:
				if disciplina == notas.disciplina:
					#Fazendo a somatoria da carga horaria geral
					soma_carga_horaria = soma_carga_horaria + disciplina.carga_horaria
					#Fazendo o calculo Nota(i)*CargaHoraria(i)
					soma_notas = soma_notas + (notas.nota * disciplina.carga_horaria)
					#Calculando cr 
					cr = soma_notas/soma_carga_horaria

	return round(cr)	

def calculaMediaCurso(curso,lista_nota,lista_disciplina):
	alunos = 0
	soma_curso_cr = 0
	
	for notas in lista_nota:
		if curso == notas.disciplina.cod_curso:
			alunos = alunos + 1
			soma_curso_cr = soma_curso_cr + notas.aluno.cr
	return round(soma_curso_cr/alunos)	

def imprimeCrAlunos(lista_aluno,lista_nota,lista_disciplina):
	print('------- O CR dos alunos é: -------')

	#Chamando a função calculaCr para cada aluno da lista_aluno
	#Criando uma lista para ser usado no GUI
	lista_GUI = []
	for aluno in lista_aluno:
		cr = calculaCr(aluno,lista_nota,lista_disciplina)
		aluno.setCr(cr)
		print(f'{aluno.matricula} - {aluno.cr}')
		lista_GUI.append((aluno.matricula,aluno.cr))
	print('----------------------------------')
	return lista_GUI


def imprimeCrMedioCurso(lista_curso,lista_nota,lista_disciplina):
	lista_GUI_curso = []
	print('----- Média de CR dos cursos -----')
	for curso in lista_curso:
		media_curso = calculaMediaCurso(curso,lista_nota,lista_disciplina)
		print(f'{curso}  - {media_curso}')
		lista_GUI_curso.append((curso,media_curso))
	print('----------------------------------')
	return lista_GUI_curso



