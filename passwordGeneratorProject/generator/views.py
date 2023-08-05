from django.shortcuts import render
import string
import random

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def generatePassword(length, includeUpperCase, includeDigits, includePunctuation):
    characters = string.ascii_lowercase
    if includeUpperCase:
        characters += string.ascii_uppercase
    if includeDigits:
        characters += string.digits
    if includePunctuation:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for i in range(length))
    return password

def password(request):
    lenght = int(request.POST['length'])
    big = request.POST.get('big')
    numbers = request.POST.get('numbers')
    specials = request.POST.get('specials')

    password = generatePassword(lenght, big, numbers, specials)
    return render(request, 'password.html', {'length': password})







