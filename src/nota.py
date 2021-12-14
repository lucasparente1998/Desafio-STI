class Nota:
	def __init__(self):
		self.aluno = None
		self.disciplina = None
		self.nota = None

	#Sets

	def setAluno(self,aluno):
		self.aluno = aluno

	def setDisciplina(self,disciplina):
		self.disciplina = disciplina

	def setNota(self,nota):
		self.nota = nota

	#Gets

	def getAluno(self):
		return self.aluno

	def getDisciplina(self):
		return self.disciplina

	def getNota(self):
		return self.nota