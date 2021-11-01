# language: pt

Funcionalidade: Automatização Ecommerce

Cenário: Automatizar o fluxo de compra de um ecommerce
    Dado que entrei no site do "maganize luiza"
    Quando digitar "relogio" na barra de busca
        E clicar em "lupa"
        E clicar no primeiro item
        E clicar em aceitar Cookies
        E clicar em "adicionar na sacola"
    Então o produto foi adicionado na sacola