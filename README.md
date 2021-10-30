# Teste Técnico QA

### Testes manuais - Respostas
1. Com suas palavras, explique com detalhes sobre a pirâmide de testes.
    - A pirâmide de testes serve para representar graficamente e direcionar o time acerca do níveis e tipos de testes que serão desenvolvidos. Quanto mais perto  nível do topo da pirâmide mais caro e mais tempo demorará para testar e quando mais perto da base mais rápido e barato será para testar.
    - A pirâmide de testes é dividida geralmente em 3 partes, existem variações com mais partes, são elas:
        - Testes Unitários
            - Representam a maior parte dos testes, são mais rápidos e baratos de serem realizados
        - Testes de Serviços
            - Também chamados de testes de intregração, seu principal propósito é verificar a intregação da unidade nova ou modifica com todo o resto da aplicação. Geralmente, tem um custo moderado de tempo e dinheiro. E devem testar o que não consegue ser testado pelos teste unitários por motivos de isolamento geralmente.
        - Testes de Ponta a Ponta
            - Chamados Também de testes end-to-end(E2E) ou testes de UI, o objetivo principal aqui é verificar a usabilidade da aplicação e devesse automatizar aquilo que for somente necessário pois o custo em tempo e dinheiro é maior nesses testes. Vale ressaltar a necessidade de testes manuais mesmo após a validação dos testes ponta a ponta, pois nos testes manuais é possível avaliar coisas que a automatização não consegue.

                ![pirâmide](https://lh5.googleusercontent.com/X-68m7pb9ZTvyya78WrLIwz9331GbhAHFziKDHaW-fXdqAxCMZFjmlWx1GM0TepbuvZn9ARWvotBn05WmWsNznDjxFmkslFab7IKxh8ghhPdM4t-f380m--Hbx4gqejRkYVh1jwZ)

1. Na sua percepção, por que é importante o analista de QA participar desde o início
do desenvolvimento de uma feature?
    - Para validar o processo de criação e desenvolvimento da feature. Durante todo o processo deve ser pensada a qualidade das entregas, mesmo aquelas que não tem contato direto com o consumidor final, e o analita de QA é o profissional responsável por essa validação.

1. Considerando a imagem abaixo uma tela de um sistema WEB, levante o maior
número possível de casos de teste.
    - Preencher todos os campos corretamente, aceitar os termos e concluir o registro;
    - Preencher apenas um dos campos, aceitar os termos e concluir o registro;
    - Não preencher nenhum campo, aceitar os termos e concluir o registro;
    - Apenas apertar no botão de concluir;
    - Escrever algo no campo "Senha" e apertar o botão de visualização;
    - Escrever algo no campo "Confirmar Senha" e apertar o botão de vizualização;
    - Clicar na logo;
    - Preencher todos os campos corretamente, exceto o campo "CPF", inserir um cpf inválido;
    - Preencher todos os campos corretamente, exceto o campo "senha", inserir uma senha menor que não atende a todos os requisitos
    - Preencher todos os campos corretamente, exceto o campo "Telefone", inserir um número no formato errado de telefone.
    - Preencher todos os campos corretamente, exceto o campo "Confirmar Senha", inserir uma senha diferente da colocada no campo "Senha";
    - Preencher o campo "Nome Completo" com uma string de menos de 10 caracteres
