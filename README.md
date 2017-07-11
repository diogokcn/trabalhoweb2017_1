# trabalhoweb2017_1

#  Uso local
### Linux

Passo 1: Clonar projeto
```bash
git clone https://github.com/diogokcn/trabalhoweb2017_1.git
cd trabalhoweb2017_1
```
Passo 2: Instalar Django e depedências
```bash
pip install django==1.8.5 whitenoise==2.0 
```
Passo 3: Instalar pacotes para Django
```bash
pip install django-filter 
pip install django-contrib-comments
```
Passo 4: Ativar ambiente virtual
```bash
source virtualenv/bin/activate
```
Passo 5: Adicionar modelos ao banco de dados local
```bash
cd _site/
python manage.py makemigrations
python manage.py migrate
```
Passo 6: Inicial servidor
```bash
python manage.py runserver
```
Passo 7: Acessar site
```bash
http://127.0.0.1:8000/
```
# Documentação
## Descrição  
	O trabalho trata-se de um catálogo online de camisetas, DVDs, Jogos e Livros com cadastro de usuários. 
	Neste sistema o usuário pode adicionar um item, visualizar itens que outros usuários criaram e submeter 
	um comentário na seção de detalhes de um determinado item. 
	O usuário pode editar e excluir somente elementos criados por ele.

## Tecnologia  
	Framework Django.

## Entidades (CRUD)
* __Usuário:__ nome, e-mail e senha  

* __Camiseta:__ marca, tamanho, cor, tecido, preço, usuário  

* __DVD:__ título, gênero, ano, duração, preço, usuário  

* __Jogo:__ título, estúdio, distribuidor, gênero, ano, preço, usuário  

* __Livro:__ título, ano, editora, autor(a), número de páginas, formato, preço, usuário  

## Funcionalidades
* __Seção de Comentários:__ apenas um usuário logado pode comentar na página de detalhes de um determinado item  

* __Pesquisa:__ qualquer pessoa pode pesquisar por determinado item na página de pesquisa  

## Internacionalização
* __Português Brasileiro__
* __Inglês__

## Estrutura
	A estrutura usada para o projeto foi MTV (Model,Template, View).

