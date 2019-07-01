from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import ShopItem
from first_app.forms import FirstForm

# def home(request):
#     return HttpResponse("<h1>HELLO WORLD!</h1>")

def home(request):
    context_dict = {'user_name1':'Tomek', 'user_name2':'Gosia'}
    return render(request, 'first_app/home.html', context=context_dict)

def help(request):
    return render(request, 'first_app/help.html')

def contact(request):
    return HttpResponse('<h1>Our technicians are out of office.</h1>')

def shop(request):
    items_list = ShopItem.objects.order_by('item_name')
    context_dict = {'items': items_list}
    return render(request, 'first_app/shop.html', context=context_dict)

def first_form(request):
    form = FirstForm()

    if request.method == 'POST':
        form = FirstForm(request.POST)

        if form.is_valid():
            print('***\nSmething was submitted to the First Form!')
            print(f"Name: {form.cleaned_data['name']}")
            print(f"Email: {form.cleaned_data['email']}")
            print(f"Message: {form.cleaned_data['message']}")

    context_dict = {'form': form}
    return render(request, 'first_app/form.html', context=context_dict)
