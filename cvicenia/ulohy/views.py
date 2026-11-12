from django.shortcuts import render
from django.http import HttpResponse

def ulohy(request):
    return render(request, "ulohy.html")


def ahoj(request):
    return HttpResponse("Ahoj svet!")


def o_mne(request):
    kontext = {
        "meno": "Matias",
        "vek": 17,
        "zaluby": ["skola", "matematika", "hokej"],
    }
    return render(request, "ulohy/o_mne.html", kontext)


def rozvrh(request):
    hodiny = [
        {"cislo": 1, "predmet": "Programovanie"},
        {"cislo": 2, "predmet": "Programovanie"},
        {"cislo": 3, "predmet": "Programovanie"},
        {"cislo": 4, "predmet": "Anglický jazyk"},
        {"cislo": 5, "predmet": "Internet vecí"},
        {"cislo": 6, "predmet": "Internet vecí"},
    ]

    return render(
        request,
        "ulohy/rozvrh.html",
        {"den": "Piatok", "hodiny": hodiny}
    )