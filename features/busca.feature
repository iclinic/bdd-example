# language: pt

Funcionalidade: Barra de busca

Cenário: Busca por repositório no GitHub
    Dado que entrei no site do "GitHub"
    Quando digitar "iclinic/bdd-example" na barra de busca
        E clicar em "All GitHub"
    Então o repositório será encontrado
