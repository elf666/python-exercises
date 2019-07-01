# 1
stworz projekt o nazwie second_project
dodaj w nim aplikację o nazwie second_app
dodaj aplikację do pliku settings.py w folderze projektu
dodaj funkcję index w views aplikacji i przy uzyciu HttpResponse wyswietl "Dzien dobry."
dodaj sciezke do funkcji index w urls.py w folderez projektu
uruchom projekt i zobacz czy dziala

# 2
dodaj plik urls.py do second_app i stworz w nim przekierowanie do funkcji
help, ktora dodaj do views. Funkcja powinna wyswietlac informacje ze jestes na stronie pomocy.
zmodyfikuj plik urls.py w folderze projektu, tak aby dla podstrony help/ przekierowywał
do pliku urls.py z first_app
przetestuj czy dziala

w second_project utworz folder templates a w nim folder second_app
dodaj sciezke do templates w settings.py uzywajac os.path.join (TEMPLATE_DIR)
dodaj utworzona sciezke do zmiennej TEMPLATES w settings.py
zmodyfikuj funkcje help w views tak, aby korzystała z render zamiast HttpResponse,
podaj jako argument template help.html
utworz plik help.html tak aby skorzystał z template taga, jaki stworzylismy w nowej funkcji view





#3

do folderu project2 dodaj folder static, a do niego foldery: images i css
sciezke do tego folderu (STATIC_DIR) dodaj do settings.py,
(tak jak wczesniej dodawales templates)

na koncu settings.py dodaj liste STATICFILES_DIRS i do niej dodaj swoj STATIC_DIR jako liste
dodaj do static/images dowolny plik obrazek.jpg i plik styl.css (h1 -> blue)

i skonfiguruj go odpowiednio do wyswietlenia obrazka
w kodzie html musimy załadowac staticfiles bezposrednio pod naglowkiem
wyswietl zdjecie i przy uzyciu css zmien styl h1
