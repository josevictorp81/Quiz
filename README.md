# Quiz
É uma API que permite que usuários criem quizzes contendo várias questões e suas opções de resposta. Cada quiz deve perntencer a uma categoria, cada questão deve pertencer a um quiz e assim por diante.

OBS: caso o usuário queira criar um quiz para uma categoria que ainda não existe, o mesmo pode criar uma categoria e depois criar o quiz.

## Endpoints
Lista de quais operações o usuário pode fazer em cada endpoint:
--- ---

Categoria 

- Criar e listar as categorias.
```
/api/category/
```

Quiz 
- Criar um quiz, listar todos, filtrar todos os quiz por categoria, listar quiz pelo nome, atualizar e deletar um quiz pelo ID.
```
/api/quiz/
/api/quiz/?category__name=nome_categoria
/api/quiz/?title=nome_quiz
/api/quiz/id_quiz/
```

Questão 
- Criar uma questão, listar todas as questões de um quiz, listar uma questão aleatória de um quiz, atualizar e deletar questão pelo ID.
```
/api/question/
/api/question/nome_quiz/ 
/api/question/nome_quiz/random/
/api/question/id_question/
```

Resposta
- Criar respsota, atualizar e deletar resposta pelo ID.
```
/api/answer/
/api/answer/id/ 

Para ver com mais detalhes os schemas de entrada de cada endpoint acesse `/docs/`.
```

## Bibliotecas
- [Django](https://www.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [drf-yasg](https://drf-yasg.readthedocs.io/en/stable/)