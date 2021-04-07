from django.db.models import QuerySet
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from cart.forms import CartAddProductForm

from .models import *
from .forms import *

def index(request):
    return render(request, "Главная.html")

def vipechka(request):
    VipData = menu.objects.filter(category="ВП")
    forms=CartAddProductForm
    return render(request, "Выпечка.html", {'Menu': VipData,"forms":forms})

def salat(request):
    VipData = menu.objects.filter(category="СЛ")
    forms = CartAddProductForm
    return render(request, "Салаты.html", {'Menu': VipData, "forms":forms})

def desert(request):
    VipData = menu.objects.filter(category="ДС")
    forms = CartAddProductForm
    return render(request, "Десерты.html", {'Menu': VipData, "forms":forms})

def napitki(request):
    VipData = menu.objects.filter(category="НП")
    forms = CartAddProductForm
    return render(request, "Напитки.html", {'Menu': VipData, "forms":forms})

def galler(request):
    Data = gallery.objects.all()
    return render(request, "Галерея.html", {"Data": Data})

def sobitiya(request):
    return render(request, "События.html")

def komanda(request):
    Data = team.objects.all()
    k = 0
    Buff = []
    NewData = []
    for kom in Data:
        if k == 3:
            NewData.append(Buff)
            Buff = []
            k = 0
        Buff.append(kom)
        k+=1
    if k != 0: NewData.append(Buff)
    return render(request, "Команда.html", {"Data": NewData})

def vakansii(request):
    Data = vacancy.objects.all()
    k = 0
    Buff = []
    NewData = []
    for kom in Data:
        if k == 3:
            NewData.append(Buff)
            Buff = []
            k = 0
        Buff.append(kom)
        k += 1
    if k != 0: NewData.append(Buff)
    return render(request, "Вакансии.html", {"Data": NewData})

def otzivi(request):
    form = ReviewForm()
    Data = reviews.objects.all()
    if request.method == "POST":
        NewReview = reviews(name = request.POST.get("name"), description = request.POST.get("text"), mark = request.POST.get("mark"))
        NewReview.save()
        return HttpResponseRedirect('o')
    return render(request, "Отзывы.html", {'form': form, 'data': Data})

def gde(request):
    return render(request, "Где нас найти.html")

def d_vipech(request):
    return render(request, "День выпечки.html")

def d_coffee(request):
    return render(request, "День кофе.html")

def d_r_cafe(request):
    return render(request, "День рождения кафе.html")

def d_eclair(request):
    return render(request, "День эклера.html")

def m_k(request):
    return render(request, "Мастер-класс.html")

def cart(request):
    forms = CartAddProductForm
    return render(request, "detail.html", {'forms':forms})

def product_detail(request, id):
    product = get_object_or_404(menu,
                                id=id,
                                available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'pages/templates/Выпечка.html', {'product': product,
                                                        'cart_product_form': cart_product_form})

