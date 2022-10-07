Starting from lab3 folder:
1. Build docker container for dba: 
cd dba
docker build -t my_db .

2. Build docker container for db: 
cd ../db
docker build -t my_db .

3. Build docker container for django:
cd ..
docker build -t my_django .

3. Run docker containers for dba, db, and django & create docker network:
docker network create mynetwork
docker run --name mydba --network mynetwork -p 8081:80 -d my_dba
docker run --name mydb --network mynetwork  -itd -p 5432:5432 my_db
docker run -it -p 8000:8000 --network mynetwork -v $(pwd)/app:/app my_django /bin/bash

4. Start django project
django-admin startproject app

5. Migrate & run server
python app/manage.py migrate 
python app/manage.py runserver 0.0.0.0:8000