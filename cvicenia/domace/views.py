from django.shortcuts import render

def domace(request):
    ulohy = {
        "uloha 1": "dokoncit referat",
        "uloha 2": "naucit sa na test",
        "uloha 3": "uloha matematika",
    }
return render(request,)