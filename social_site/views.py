from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.db.models import Q

from .models import Nutzer, Istfan, Beziehung, Brillentraeger, Uebtaus
from .forms import SearchForm

# Create your views here.
def index(request):
    user_list = Nutzer.objects.all()[:10]
    context = {'user_list':user_list}
    return render(request, 'social_site/main.html', context)

def search(request, page):
    search_str = request.GET['str']
    res = Nutzer.objects.filter(Q(anzeigename__icontains=search_str) | Q(n_name__icontains=search_str))
    if len(res) <= 20:
        page = 0
        context = {'res_list': res, 'page':page, 'search_str':search_str}
    else:
        context = {'res_list': res[(page-1)*20:page*20], 'page':page, 'search_str':search_str}
    
    return render(request, 'social_site/search_results.html', context)

def user(request, user_id):
    result = get_object_or_404(Nutzer, id=user_id)
    try:
        brillentraeger = Brillentraeger.objects.get(id=user_id)
    except:
        brillentraeger = None

    fan_ids = list(Istfan.objects.all().filter(id2=user_id).values_list("id1", flat=True))
    fans = Nutzer.objects.filter(id__in=fan_ids)

    beziehungen = Beziehung.objects.filter(id1=user_id)
    dates = beziehungen.filter(art="Date")
    date_users = Nutzer.objects.filter(id__in=list(dates.values_list("id2",flat=True)))

    ehen = beziehungen.filter(art="Ehe")
    ehen_users = Nutzer.objects.filter(id__in=list(ehen.values_list("id2",flat=True)))

    hobbies = Uebtaus.objects.filter(nutzerid=user_id)

    context = {'user': result, 'fans':fans, 'ehen': ehen_users, 'dates':date_users, 'brillentraeger':brillentraeger, 
    'hobbies': hobbies}
    return render(request, 'social_site/userpage.html', context)

