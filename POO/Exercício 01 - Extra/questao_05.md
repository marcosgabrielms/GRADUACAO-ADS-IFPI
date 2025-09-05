* **Aluno:** Representa o estudante matriculado, com atributos como nome, matrícula, curso e notas.
* **Professor:** Modela o docente, com atributos como nome, departamento e as turmas que leciona.
* **Disciplina:** É a matéria em si (ex: "Programação Orientada a Objetos"), com atributos como código, ementa e carga horária.
* **Turma:** Representa uma oferta específica de uma disciplina em um período letivo, associando um professor, uma lista de alunos, horários e uma sala.
* **Curso:** Modela o curso superior (ex: "Análise e Desenvolvimento de Sistemas"), contendo o conjunto de disciplinas necessárias para a formação.
* **Avaliação:** Pode ser um objeto para representar uma prova ou trabalho, com atributos como nome, data e a nota de cada aluno.
* **Matrícula:** Objeto que formaliza o vínculo entre um `Aluno` e uma `Turma` específica.