def calculaCr(aluno,lista_nota,lista_disciplina):
	soma_carga_horaria = 0
	soma_notas = 0
	#Percorre cada nota na lista de nota 
	for notas in lista_nota:
		#Compara o Aluno recebido como parâmetro com o Aluno que está atrelado a classe nota
		if aluno == notas.aluno:
			#Percorre cada disciplina na lista de disciplinas
			for disciplina in lista_disciplina:
				#Compara a Disciplina com a Disciplina que está atrelado a classe nota 
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
	#Percorre cada nota em lista de nota
	for notas in lista_nota:
		#Verifica se o Curso recebido como parâmetro e igual ao Curso que está atrelado a classe nota
		if curso == notas.disciplina.cod_curso:
			alunos = alunos + 1
			soma_curso_cr = soma_curso_cr + notas.aluno.cr
	return round(soma_curso_cr/alunos)	

def imprimeCrAlunos(lista_aluno,lista_nota,lista_disciplina):
	print('------- O CR dos alunos é: -------')

	
	#Criando uma lista GUI que será ultilizada para criação do FrameWork
	lista_GUI = []
	#Percorre cada Aluno na lista aluno
	for aluno in lista_aluno:
		#Chamando a função calculaCr para cada aluno da lista_aluno
		cr = calculaCr(aluno,lista_nota,lista_disciplina)
		aluno.setCr(cr)
		print(f'{aluno.matricula} - {aluno.cr}')
		lista_GUI.append((aluno.matricula,aluno.cr))
	print('----------------------------------')
	#Retorna a lista GUI que será utilizada para criação do FrameWork
	return lista_GUI


def imprimeCrMedioCurso(lista_curso,lista_nota,lista_disciplina):
	#Criando uma lista GUI curso que será usada para criação do FrameWork
	lista_GUI_curso = []
	print('----- Média de CR dos cursos -----')
	for curso in lista_curso:
		#Chamando a função calculaMediaCurso para calcular a media de cada curso
		media_curso = calculaMediaCurso(curso,lista_nota,lista_disciplina)
		print(f'{curso}  - {media_curso}')
		lista_GUI_curso.append((curso,media_curso))
	print('----------------------------------')
	#Retorna a lista GUI curso que será utilizada para criação do FrameWork
	return lista_GUI_curso



