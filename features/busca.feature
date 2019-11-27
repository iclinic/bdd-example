# language: pt

Funcionalidade: Busca de repositório

Cenário: Validação dos campos de login
    Dado que entrei no site do "GitHub"
    Quando procurar por "iclinic/bdd-example"
    Então o repositório será encontrado
