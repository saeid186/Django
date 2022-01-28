To Create and run this project after pull project

Please change directory to oss-django :
#cd oss-django

Then create static file with run command :
#python manage.py collectstatic

After that please create nginx container with two commands below :
#docker-compose run nginx
#docker-compose up
