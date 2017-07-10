# trabalhoweb2017_1
Trabalho para disciplina Desenvolvimento de Software para a Web, turma A.

Este trabalho utiliza o framework Django¹ no desenvolvimento de um site de catálogo de camisetas, dvds, jogos eletrônicos e livros.

¹ https://www.djangoproject.com/

##  Uso local
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
