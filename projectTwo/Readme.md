step 1:
pip install Django

create project :-

django-admin startproject project_name

if you run project:- 
python manage.py runserver


create vertual enviroment:-

python -m venv  venv_name


create app:-
django-admin startpp appname 


project:-

django-admin startproject project_name

django-admin startapp App_name

Step1 :Configure app name in Settings.py INSTALLED APPS
Step2: Create template folder and Configure in Settings.py under TEMPLATES
        - Add any html files
Step3: Create Static folder and configure in settings.py STATIC
        - STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
Step4: Load Static files in template
        - {% load static %}
        - <link rel="stylesheet" href="{% static 'css/home.css' %}">

step5:- after go throw views and create functions
def index(request):
    return render(request, 'index.html')
step6:-and go through url create path

path('', index, name='index'),

runserver
python manage.py runserver


project3:-


django-admin startproject djangoproject3
django-admin startapp app

write models in models.py file and register models in admin

python manage.py createsuperuserE
python manage.py makemigrations
python manage.py migrate
python manage.py runserver


login to /admin with your credentials



