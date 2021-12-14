from flask import Flask, render_template # Importa a biblioteca
from main import lista_GUI,lista_GUI_curso

app = Flask(__name__) # Inicializa a aplicação

@app.route('/') # Cria uma rota
def main():
  return render_template('index.html', alunos = lista_GUI, cursos = lista_GUI_curso)

if __name__ == '__main__':
  app.run(debug=True) # Executa a aplicação