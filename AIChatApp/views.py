from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def front_page(request):
    return render(request, 'home.html')


def ong_page(request):
    ongs=[
        {
            "nr_angajati":"53",
            "poza":"https://ngo.md/media/cache/app_organisation_small_image/media/avatar/63ce8585696ee_IMG-a31b5ff18712f2c78c2696d592bc45da-V.jpg",
            "numele" : "Centrul Regional pentru Inițiative Sociale și Dezvoltare Durabilă ",
            "locatia": "Florești, Floresti, Str.Crinilor 36",
        } for i in range(20)
        
    ]
    return render(request, 'ong.html',{"ongs":ongs})

def about_us(request):
    return render(request, 'about_us.html')