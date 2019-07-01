# 1
stworz projekt o nazwie second_project
dodaj w nim aplikację o nazwie second_app
dodaj aplikację do pliku settings.py w folderze projektu
dodaj funkcję index w views aplikacji i przy uzyciu HttpResponse wyswietl "Dzien dobry."
dodaj sciezke do funkcji index w urls.py w folderez projektu
uruchom projekt i zobacz czy dziala





# 2
zmodyfikuj plik urls.py w folderze projektu, tak aby dla podstrony sklep/ przekierowywał
do pliku urls.py z second_app (uzywajac include)

dodaj plik urls.py do second_app i stworz w nim przekierowanie do funkcji z view
ktora wyswietli podstronę sklep

do views w second_app dodajcie funkcje wyswietlajaca podstrone sklep

przetestuj czy dziala









w second_project utworz folder templates a w nim folder second_app
dodaj sciezke do templates w settings.py uzywajac os.path.join (TEMPLATE_DIR)
dodaj utworzona sciezke do zmiennej TEMPLATES w settings.py
zmodyfikuj funkcje help w views tak, aby korzystała z render zamiast HttpResponse,
podaj jako argument template help.html
utworz plik help.html tak aby skorzystał z template taga, jaki stworzylismy w nowej funkcji view
