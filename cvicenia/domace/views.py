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

def du3_teplota(request):
    vysledok = None

    if request.method == "POST":
        teplota = float(request.POST.get("teplota"))
        smer = request.POST.get("smer")

        if smer == "c_f":
            vysledok = round(teplota * 9 / 5 + 32, 1)
            jednotka = "°F"
        else:
            vysledok = round((teplota - 32) * 5 / 9, 1)
            jednotka = "°C"

    else:
        jednotka = ""

    return render(request, "domace/du3_teplota.html", {
        "vysledok": vysledok,
        "jednotka": jednotka,
    })