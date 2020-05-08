from django.shortcuts import render
from django.http import HttpResponse
import random



def index(request):
    return render(request, 'generator/index.html' )


def password(request):

    characters = list('abcdefghijklmnopqrstuvwxyz')
    lenght = int(request.GET.get('Length'))

    if request.GET.get('Uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('SepcialCharacters'):
        characters.extend(list('!@#$%^&*'))


    if request.GET.get('Numbers'):
        characters.extend(list('0123456789'))
    
    thePassword = ''

    for x in range(lenght):
        thePassword += random.choice(characters)


    return render(request, 'generator/password.html', {"password":thePassword})


def about(request):
    return render (request, 'generator/about.html')

