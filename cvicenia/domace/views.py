from django.shortcuts import render

def domace(request):
    ulohy = {
        "uloha 1": "dokoncit referat",
        "uloha 2": "naucit sa na test",
        "uloha 3": "uloha matematika",
    }

    return render(request, 'domace.html', {'ulohy': ulohy})

def du2_vizitka(request):
    udaje = {
        "meno": "Matiáš",
        "trieda": "3.AT",
        "vek": 17,
        "predmety": [
            "Programovanie",
            "Matematika",
            "Telesna výchova",
        ],
    }

    return render(request, "du2_vizitka.html", udaje)