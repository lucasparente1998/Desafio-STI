class Disciplina:
	#Inicialização da classe disciplina
	def __init__(self):
		self.cod_disciplina = None
		self.cod_curso = None
		self.carga_horaria = None

	#Sets
	def setCodDisciplina(self,cod_disciplina):
		self.cod_disciplina = cod_disciplina

	def setCodCurso(self,cod_curso):
		self.cod_curso = cod_curso

	def setCargaHoraria(self,carga_horaria):
		self.carga_horaria = carga_horaria

	#Gets
	def getCodDisciplina(self):
		return self.cod_disciplina

	def getCodCurso(self):
		return self.cod_curso

	def getCargaHoraria(self):
		return self.carga_horaria

	