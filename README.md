library_management/
│
├── library/
│   ├── __init__.py
│   ├── book.py
│   ├── decorator.py
│   └── loan.py
│
├── tests/
│   ├── __init__.py
│   └── test_decorator.py
│
└── README.md

###########################################

# Sistema de Gestão de Biblioteca

Este projeto implementa um sistema básico de gerenciamento de biblioteca, permitindo o cadastro de livros e o controle de empréstimos, utilizando o padrão de projeto **Decorator**.

## Padrão de Projeto Utilizado: Decorator

O padrão **Decorator** foi aplicado para estender a funcionalidade da classe `Book`, permitindo adicionar "etiquetas" (como "Best-seller", "Novo", etc.) aos livros, sem modificar diretamente a classe original.

## Como executar os testes

Para rodar os testes unitários, execute:

```bash
python -m unittest discover -s tests


### Explicação

- O padrão **Decorator** foi utilizado para estender a funcionalidade da classe `Book`, permitindo que novos comportamentos sejam adicionados (como etiquetas de destaque) sem modificar a estrutura interna da classe `Book`.
- Os testes unitários garantem que o comportamento esperado do `Decorator` está funcionando corretamente.

