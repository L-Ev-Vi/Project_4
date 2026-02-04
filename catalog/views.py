from pydoc import HTMLDoc

from django.shortcuts import render


def index(request) -> HTMLDoc:
    return render(request, 'catalog/index.html')


def contacts(request):
    if request.method == 'POST':
        return render(request, 'catalog/message.html')
    return render(request, 'catalog/contacts.html')


    # if request.method == 'POST':
    #     name = request.POST.get('name')
    #     email = request.POST.get('email')
    #     message = request.POST.get('message')
# print(f'You have new message from {name}({email}): {message}')
