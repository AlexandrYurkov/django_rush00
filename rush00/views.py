from django.shortcuts import render

# Create your views here.
from data.battleField import field


def ex00(request):
    return render(request, "index.html", f"{'gamefield': '{field}'}")
