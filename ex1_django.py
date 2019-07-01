stworz projekt o nazwie project2
dodaj w nim aplikację o nazwie second_app
dodaj aplikację do pliku settings.py w folderze projektu
dodaj funkcję home w views aplikacji i przy uzyciu HttpResponse wyswietl "Dzien dobry."
dodaj sciezke do funkcji home w urls.py w folderez projektu
uruchom projekt i zobacz czy dziala


django-admin startproject <nazwa projektu> # stworzenie projektu
django-admin startapp <nazwa aplikacji> # stworzenie aplikacji (W FOLDERZE PROJEKTU!)
python manage.py runserver # postawienie serwera








1. django-admin startproject project-name # stworzenie nowego projektu
2. python manage.py startapp app-name # stworzenie nowej aplikacji (będąc w folderze projektu)
3. dodanie aplikacji do settings.py w folderze projektu
4. dodanie najprostszego HttpResponse do vievws (w aplikacji)
from django.http import HttpResponse
def index(request):
    return HttpResponse("Wytam świecie")
5. dodanie sciezki do funkcji z views w urls.py (projektu)
from app-name import vievws
path('', views.index, name='index')
6. python manage.py runserver # uruchomienie serwera
