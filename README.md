# djangodatalisting
Django data listing with filtering and paging. Docker compose 
#This application developed in ubuntu environment.

Assumptions:
1. Docker and docker-compose are already installed and properly configured.

First time application usage:
1. Open linux terminal.
2. Go to root folder where docker-compose.yml file exists.
3. Run "docker-compose build" command.
4. Run "docker-compose up" command. It starts the application. You should run a "docker-compose up" command again in case if you get some error.
5. Now open an another command terminal. Please make sure you are in root directory same as step 2.
6. Run "docker exec -it djangodatalist_web_1 bash". djangodatalist_web_1 is container name.
7. Run "python3.8 manage.py makemigrations djangolist" command.
8. Run "python3.8 manage.py migrate" command.
9. Run "python3.8 manage.py shell" command.
10. Run the following commands.
11. from djangolist.models import *
12. c_1 = Category(name="Category1")
13. c_1.save()
14. for p in range(1,100):
15.   p = Product(name= "Product {0}".format(p),category= c_1, quantity=10)
16.   p.save()
17.  Hit Enter Key again.
18.  Repeat the steps from 12 to 17 for other categories and products.
19.  Run "exit()" command.
20.  Run "exit" command.
21.  Go to first terminal opened in step 1.
22.  Run "docker-compose down" command.
23.  Run "docker-compose up" command.

If you follow these steps in sequence you should able to run this application.
