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

def pozdrav(request):

    meno = request.GET.get("meno", "") # .get najde parameter meno, ak nie je zadaný, použije sa prázdny reťazec

    return render(request, 'ulohy/pozdrav.html', {"meno": meno})

def sucet(request):
    vysledok = None
    if request.method == "POST":
        a = int(request.POST.get("a", 0))
        b = int(request.POST.get("b", 0))
        vysledok = a + b
        
    return render(request, 'ulohy/sucet.html', {"vysledok": vysledok})

def kalkulacka(request):
    vysledok = None
    if request.method == "POST":
        a = int(request.POST.get("a", 0))
        b = int(request.POST.get("b", 0))
        operacia = request.POST.get("operacia", "+")

        if operacia == "+":
            vysledok = a + b
        elif operacia == "-":
            vysledok = a - b
        elif operacia == "*":
            vysledok = a * b
        elif operacia == "/":
            if b != 0:
                vysledok = a / b
            else:
                vysledok = "err"
        
    return render(request, 'ulohy/kalkulacka.html', {"vysledok": vysledok})

def obdlznik(request):
    vysledky = None
    if request.method == "POST":
        a = float(request.POST.get("a", 0))
        b = float(request.POST.get("b", 0))
        s = a * b
        o = 2 * (a + b)
        if a <= 0 or b <= 0:
            return render(request, 'ulohy/obdlznik.html', {"error": "Strany musia byť kladné čísla!"})
        vysledky = {
            "obvod": o,
            "obsah": s
        }
        
    return render(request, 'ulohy/obdlznik.html', {"vysledky": vysledky})

def vek(request):
    vek = None
    if request.method == "POST":
        rok = int(request.POST.get("rok_narodenia", 0))
        mesiac = int(request.POST.get("mesiac_narodenia", 0))
        den = int(request.POST.get("den_narodenia", 0))

        if den < 1 or den > 31 or mesiac < 1 or mesiac > 12:              
            return render(request, 'ulohy/vek.html', {"error": "Neplatný dátum!"})

        datum = daytime.date(rok, mesiac, den)
        dnes = daytime.date.today()

        
        
        vek = dnes.year - datum.year
        if (dnes.month, dnes.day) < (datum.month, datum.day):
            vek -= 1

        if vek < 0:
            return render(request, 'ulohy/vek.html', {"error": "Zadaný dátum je v budúcnosti."})

    return render(request, 'ulohy/vek.html', {"vek": vek})