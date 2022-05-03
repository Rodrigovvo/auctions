# Comentários ao desenvolvimento de Teste de Desenvolvimento

## Comentários inicias

#### #1 A Stack utilizada
* Backend: Python | Framework: Django | django-rest-framework
* Froentend: VueJs
* Database: Postgresql

## Comentários sobre o Back-End

Comecei o projeo pelo Back-end, criando o projeto com Django, criando banco de dados, em sequencia criando-se os models, dividi em três apps, base (Que servirá para manter aquivos base e que possam ser extendidos por outros apps), users (Que trata dos usuários do sistema, seja cliente seja empresa) e auctions ( que trata dos fretes em si, contendo as ofertas e o lances).

Criei os models. Inicialmente, criei o model da base, chamado AuditModel que contém os elementos de data de criação de data de alteração, elementos importantes para controle dos dados do sistema.

De acordo com os itens que seriam recebidos no json de criação dos itens criei os models de usuários, verificando que clientes e empresas possuiam elementos similares criei um model Person e deste model estenderam Client e Enterprise. 

Foquei na validação do documento verificando que seria possível receber documentos do tipo CPF e CNPJ. Nesse item, fiz o importe de uma biblioteca chamada validate-docbr. O uso dessa biblioteca se deve ao fato de que, em que pese ser relativamente fácil validar os dígitos finais do documento (CPF ou CNPJ) ainda estão em uso documentos no modelo antigo CIC \ CGC, nesse sentido, buscei a implementação de uma biblioteca que possa prevenir a validação destes documentos ainda que em modelo antigo.

O doc ainda terá uma alteração quando for salvo, sendo salvo somente os número em formato de string. Essa alteração visa garantir a integridade dos dados, pois, foi inserido o parâmetro unique para o doc, ou seja, visa-se garantir que todos os doc tenham a mesma formatação quando salvos. 

Para a criação dos models de auction utilizei como base os dados que seriam enviados por json. Para a criação do model Offer tive algumas escolhas para serem feitas a primeira foi a mudança dos nomes dos campos 'from' e 'to' para 'location_from' e 'location_to', em especial, a mudança evita a palavra reservada do python 'from' além de melhorar leitura do código. Outro ponto, foi a escolha por um textChoices para conter o amount_type, limitando assim as escolhas ao descrito pelo Choice e centralizando todas as definições em um único local. 

Criei uma divisão para a api separando de apps, dividindo o código entre os apps e api. 

Mantive as urls na base do sistema, na pasta backend, centralizando as informações de rotas. 

Dentro de api criei a 'v1' que trata da primeira versão da api. Dentro do 'v1', dividi entre serializers, tests, utils e views. 

Views e serializers contém um arquivo para users e um para auctions. 

Criei um serializer para client e para enterprise, que estendem de person, dentro da serializer de person fiz a 'validate_doc' que trata da validação do CPF/CNPJ. São excluídos dos serializers os componentes de AuditModel. 

Em serializers.auctions o serializer de offer teve que ter seu field (location_from) modificado de nome para from. Isso foi feito no método get_fields. Além disso, passei para o id_customer todos os dados de customer quando em resposta, pelo método to_representation. De igual modo, o id_provider também fornece todos os dados de provider quando enviada a requisição. Esclaracendo que não são exigidos os mesmos dados para requisição, devendo ser passado somente o id dos itens, como o nome já indica. Faço o envio deste modo, para evitar a necessidade do front de fazer uma requisição específica para pegar os dados do provider ou customer, já disponibilizando no momento da chamada da offer ou do bid. 

Para as views, em users, alterei o método destroy que é chamado na requisição HTTP de verbo 'delete', para que somente altere o campo 'active', fazendo-se assim um soft delete, preservando os dados. Nos querysets, estou enviando somente os itens ativos. Contudo, na view de person trouxe todos os itens, mesmo que inativos, fazendo uma rota específica para os persons ativos. 

Em views.auctions criei somente um action em OfferViewSet para que pudesse buscar os lances vinculados àquela oferta. Issose mostrou útil para a apresentação no front-end onde se há um botão nos itens de oferta de frete que redirecionam para um componente que contém todos os lances da isntância da oferta.

Foram feitos testes para garantir o funcionamento dos CRUDs dos models Offer, Bid, Client e Enterprise.

Terminando essa parte e para auxiliar no front-end criei uma pasta utils, onde modifiquei a paginação padrão do DRF, para acrescentar algumas informações que são muito úteis na paginação como a página atual e o número de páginas.



### Propostas de Melhorias Futuras

* Primeiramente, transpor alguns itens e tokens, como a SECRET_KEY e dados do banco de dados, para parâmetros de sistema,  que comprometem a segurança da aplicação.
* No mesmo sentido, ofuscar demais componentes do settings.py, possivelmente utilizando uma biblioteca, como o 'decouple'.
* Utilizar um método de autenticação de usuários, possivelmente implementado JWT, podendo ser utilizado com a biblioteca djangorestframework-simplejwt.
-> Dessa decorre a necessidade de ser criar rotas para retornar os tokens de acesso e de refresh, bem como, telas de criação/autenticação de usuários que não foram produzidas neste teste.
* Criação de uma model para endereço, substituindo o location_from e o location_to do model 'Offer' de Charfield para uma ForeignKey com o modelo de endereço.
* Aumento da abrangêcia dos teste.
  

## Comentários sobre o Front-End

Criando o projeto em VueJs, criei as views para cada modelo disponibilizado na descrição do teste, Offer, Bid, Client e Enterprise. 

Foi importado no index o css do Bootstrap para estilização e responsividade das páginas.

Cada view somente chama o componente correspondente. 

No router, fiz o carregamento das rotas utilizando o Lazy Loading, exceto o do Home, garantindo maior performace já que estes componentes são carregados quando chamados.

O componente Home, tem por pretensão ser uma simples landing page para acesso ao sistema. 

Os demais componentes Offer, Client e Enterprise, tem uma estrutura similar, um form para criação e alteração dos dados, uma table contendo os dados já cadastrados e uma paginação para auxiliar na 
navegação.

O componente Bids é chamado por um botão dentro do componente Offers, sendo apresentado em tela para o usuário todos os lances que a oferta de frete selecionada possui.

As chamadas foram todas feitas através de javascript vanila, sendo utilizado o método fetch em chamadas assíncronas.

Foi criado um componente para a paginação sendo reutilizado nos demais componentes. 

Foi criado um componente para o Modal, sendo reutilizado nos demais componentes, e chamado quando se clica no botão de exclusão. 

Foram criados componentes específicos para os inputs do tipo select que recebem do Back-End uma lista de dados cadastrados, como o caso de Customer e Provider. 
