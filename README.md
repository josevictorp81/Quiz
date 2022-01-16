# Quiz
É uma API que permite que usuários criam questionários com várias questões e suas opções de resposta, onde cada questionário deve perntencer a uma categoria.

OBS: caso o usuário queira criar um questionário para uma categoria que ainda não existe, o mesmo pode criar uma categoria e depois criar o questionário.

## Endpoints

| endpoints| operações |
| -- | -- |
| /api/category/ | listar |
| /api/category/ | criar  |
| -- | -- |
| /api/quiz/ | criar |
| /api/quiz/ | listar todos os quizzes |
| api/quiz/?category__name=nome_categoria | listar todos os quizzes por categoria |
| /api/quiz/?title=nome_quiz | filtrar quiz pelo nome |
| /api/quiz/id_quiz/ | atualizar |
| /api/quiz/id_quiz/ | deletar   |
| -- | -- |
| /api/question/ | criar |
| /api/question/nome_quiz | listar todas as questões de um quiz |
| /api/question/nome_quiz/random | lista uma questão aleatória do quiz |
| /api/question/id_question/ | atualizar |
| /api/question/id_question/ | deletar |
| -- | -- |
| /api/answer/ | criar |
| /api/answer/id/ | atualizar |
| /api/answer/id/ | deletar |

## Modelos de entrada
Os modelos abaixo mostram as entradas esperadas nos endpoints.

Criar Categoria:
```json
{"name": "nome da categoria"}
```

Criar Quiz:
```
{"title": "nome do quiz", "category": id_categoria}
```

Atualizar Quiz:
```
{"title": "nome do quiz"}
```

Criar Questão e Atualizar Questão:
```
{"quiz": id_quiz,  "title": "descrição"}
```

Criar Resposta e Atualizar Resposta:
```
{"question": id_questao, "answer_text": "resposta", "is_right": false}
```

Contudo, você também pode visualizar os modelos com mais detalhes acessando o caminho `/docs/`.

## Bibliotecas
- [Django](https://www.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [drf-yasg](https://drf-yasg.readthedocs.io/en/stable/)