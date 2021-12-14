## Desafio 3

Você precisa calcular o CR de alunos de uma universidade. Para isto será preciso ler de um [arquivo csv](datasets/notas.csv) a lista de notas dos alunos e, de acordo com as notas e os critérios da universidade, calcular o CR de todos os alunos. Ao final do processo, será preciso mostrar na tela o CR de todos os alunos e qual a média de CR dos cursos.

### Regras
* A nota do aluno vai de zero até 100;
* Uma nota é associada a uma disciplina e a um código de curso;
* O CR é a média ponderada da nota do aluno naquela turma com a carga horária daquela turma. O cálculo é:
  * > CR = Nota(i)*CargaHoraria(i)/TotalCargaHoraria 
  * i é a i-ésima turma de um aluno
* Utilizar Orientação a Objetos para resolver o problema
* Escolha a linguagem que achar adequada

### Exemplo
Após executar a sua aplicação, o sistema deve exibir uma saída similar a:

```bash
------- O CR dos alunos é: --------
100  -  10 
101  -  11
...
116  -  26
-----------------------------------
----- Média de CR dos cursos ------
10   -  12
11   -  45
..
100  -  13
-----------------------------------
```

### Dicas
- Quais classes são necessárias para resolver este problema?
- Desenvolva sempre buscando o menor acoplamento possível entre as classes;
- Concentre-se em desenvolver uma aplicação simples em console, tentando resolver o problema principal: o cálculo do CR dos alunos e dos cursos;
- Testes automatizados e TDD darão pontos positivos;
- Se for desenvolver uma GUI, dê preferência a um framework web, como rails, spring-boot, etc.

### Resolução

Neste projeto tratamos da resolução do Desafio apresentado.

Foi utilizada a linguagem Python (3.7.9) e também as bibliotecas **Pandas**, para a leitura do arquivo csv e **Flask**, para a criação do FrameWork Web.

Para a instalação da biblioteca pandas:
```
pip install pandas
```
Para a intalação da biblioteca flask:


```
pip install flask
```

Para visualizar o que foi pedido pelo Desafio, execute no terminal o arquivo [Main.py](https://github.com/lucasparente1998/Desafio-STI/blob/main/main.py).

Para visualizar a interface gráfica desenvolvida, execute no teminal o arquivo [GUI.py](https://github.com/lucasparente1998/Desafio-STI/blob/main/GUI.py), o mesmo criará um server para visualização.
