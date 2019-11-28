# language: pt

Funcionalidade: Busca de repositório

Cenário: Validação dos campos de login
    Dado que entrei no site do "GitHub"
    Quando digitar "iclinic/bdd-example" na barra de busca
        E clicar em "All GitHub"
    Então o repositório será encontrado
