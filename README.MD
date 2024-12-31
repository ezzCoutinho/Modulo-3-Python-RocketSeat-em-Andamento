dia 26/12
https://www.notion.so/Python-dia-26-12-168bc5c3824d80a5a79fe35448c7bdda
Hoje terminamos o projeto de luta por turno, e inciamos API com FLASK;
Aprendemos que dar é possível nos instanciarmos um classe por um atributo de outra classe, e assim ter acessos fáceis como a herança, aprendemos também a fazer decremento de uma forma simples, com atributos de uma classe. Aprendemos um novo módulo padrão do python, que é o random, que nos possibilita gerar várias formas de elementos aleatórios.
Nos vimos também um tipo de package, so que do python:
requirements.txt, onde instalamos/listamos todos os módulos de terceiros.
API;
É uma troca de informações e recursos entre um software a outra, sendo assim essencial. A troca de informações se da por meio de regras que a torna possível. Flask é uma lib de terceiros que é muito poderosa e fácil de se usar Benefícios;
Simplicidade;
Escalabilidade;
Flexibilidade;
aplicações do flask, parte do name, que é a mesma coisa do "__main__". Tendo os seus propiós métodos.
Endpoints, são strings que devem retornar em caso de exito de uma response HTTP(app.route("/")
Api Rest, pré determina conceitos de regras, onde essas regras tendem a ser respeitadas, para que não haja nenhum tipo error. Quando todas as regras são respeitadas, ela se torna um Api Restfull. Vimos todas as requisições:
get;
post;
put;
delete;
path;
e todos os códigos HTTP 100-599, e suas variações de respostas.

dia 27/12
https://www.notion.so/Python-dia-27-12-169bc5c3824d802ab241e00a9ae75de1
fazendo testes com APIS, e suas requests, vimos hoje a documentação do swagger;
é uma ferramenta voltada a criação de API'S; eles nos permite criar aquivos YAML ou JSON de forma intuitiva,
podendo começar uma API em equipe e facilitando o uso e entendimento da equipe na criação da API.
swagger gera uma visualização amigável da documentação, permitindo que stakeholders ou a equipe entendam os 
endpoints.

dia 28/12
https://www.notion.so/Python-dia-28-12-16abc5c3824d80f398f4dced08d19a7e
Hoje aprendemos mais sobre as REQUISIÇÕES de rede.
Postman, é a mesma coisa do swagger, no sentido de poder criar as requests e
vê-las:
coleções;
environments: onde colocamos uma {{baseUrl}}, fica mais fácil de manipular, do que 
colocar a mão, e pode ser alterada facilmente de um servidor para outro.
 Vimos também o CRUD
C = CREATE post 
R = READ get 
U = UPDATE put
D = DELETE delete
Vimos também que podemos colocar mais de uma requisição em uma única rota,
criação com métodos flask; jsonify, que cria um dicionario.
request é usada para acessar os dados enviados pelo cliente em solicitações 
HTTP, podendo até enviar solicitações atuais, como parâmetros, requisições, 
cookies entre outros... 
Podemos ter mais de um get, um get para todos os dados informados. ou get 
seletivos, como apenas o id, ou até mesmo uma outra chave...
path == é a mesma coisa da string permitindo usar traços em parâmetros de url.
UUID == permite usar hashs, criados aleatoriamente ou não, como parâmetro de url.

dia 30/12
https://www.notion.so/Python-dia-30-12-16cbc5c3824d801fab69f6d8a80e6a5a
Hoje, aprendemos a requisição delete, onde conseguimos filtrar, por id e apagar, e implementamos um método de pesquisa, caso se encaixe na procura única, que é o BREAK, quando ele achar, ele para. Podemos usar também o return...

dia 31/12 
https://www.notion.so/Python-dia-31-12-16dbc5c3824d80009875d546d69e26f6
Hoje vimos, sobre o pytest, que é um framework do python, que faz testes automatizados.
Vimos também o requests que trabalha em conjunto com pytest, nele nos conseguimos
passar a requisição juntamente com o parâmetro URL. Podendo ser convertido json e ser
conferido logo mais com o assert
assert é uma condicional, onde podemos passar o response.status_url, para verificação
de igual, ou fazer verificação com chaves de um tipo .json.
