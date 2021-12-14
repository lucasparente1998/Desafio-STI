class Aluno:
	#Inicializando a classe aluno
	def __init__(self):
		self.matricula = None
		self.cr = 0

	#Sets 	
	def setMatricula(self,matricula):
		self.matricula = matricula
		
	def setCr(self,cr):
		self.cr = cr

	#Gets	
	def getMatricula(self):
		return self.matricula

	def getCr(self):
		return self.cr

	
