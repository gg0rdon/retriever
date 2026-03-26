# retriever
It make it very clear I love golden retrievers and I like working in python so find to to be a very obvious name for my own issue tracker.

## Prerequisites
 - python3.14+
 - psql (PostgreSQL) 18.1+
 - SQLAlchemy 2.0+
 - uvicron 0.42+
 - python-dotenv 1.2+
 - psycopg2-binary 2.9+
so far ...

## Get started

Clone the repo

```bash
#httip
git clone https://github.com/gg0rdon/retriever.git

#ssh
git clone git@github.com:gg0rdon/retriever.git

#github cli
gh repo clone gg0rdon/retriever
```


setup a virtual environment
```bash
python3.14 -m venv venv
```
fetch the requirements
```bash
pip install -r requirements.txt
```
setup .env
```.env
HOST=<your_host>
PORT=<your_port>
DATABASE=<your_database>
USER=<a_user>
PASSWORD=<a_user_pawwword>
DATABASE_URL="postgresql://${USER}:${PASSWORD}@${HOST}:${PORT}/${DATABASE}"
```

## Database

I am using PostgreSQL which works very well with sqlalchemy so first you need to setup a database
Second you need the tables and I currently only have two

```sql

create table issues (todo);
create table comments (todo)

```


## Run it

I am using uvicorn since its very convenient and comes with swagger :)

```bash
uvicorn main:app --reload
```

enter
localhost:8000/docs for info
