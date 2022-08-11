from django.shortcuts import render
from django.views import View
from .models import *

class SezonView(View):
    def get(self, request):
        dav = Davlat.objects.all()
        data = {
            "davlatlar": dav
        }
        return render(request,"season.html",data)

class StatsView(View):
    def get(self, request):
        dav = Davlat.objects.all()
        data = {
            "davlatlar": dav
        }
        return render(request,"stats.html",data)

class ClubsView(View):
    def get(self, request):
        clubs = Club.objects.all()
        davlats = Davlat.objects.all()
        data = {
            "davlatlar": davlats,
            "clublar": clubs
        }
        return render(request,"clubs.html",data)

class TransferView(View):
    def get(self, request):
        dav= Davlat.objects.all()
        transfer = Transfer.objects.all()
        data = {
            "davlatlar": dav,
            "transferlar": transfer
        }
        return render(request,"transfer.html",data)

class UrinishView(View):
    def get(self, request):
        dav = Davlat.objects.all()
        data = {
            "davlatlar": dav
        }
        return render(request,"tryouts.html",data)

class AboutView(View):
    def get(self, request):
        davlats = Davlat.objects.all()
        data = {
            "davlatlar": davlats
        }
        return render(request,"about.html",data)

class AsosiyView(View):
    def get(self, request):
        davlats = Davlat.objects.all()
        data = {
            "davlatlar": davlats
        }
        return render(request,"index.html",data)

class ClubView(View):
    def get(self, request):
        davlats = Davlat.objects.all()
        data = {
            "davlatlar": davlats
        }
        return render(request,"club.html",data)

class OxirgiView(View):
    def get(self, request):
        dav = Davlat.objects.all()
        trans = Transfer.objects.filter(mavsum="2022/2023")
        print(trans)
        data = {
            "davlatlar": dav,
            "transferlar": trans
        }
        return render(request,"latest-transfers.html",data)

class PlayersView(View):
    def get(self, request):
        players = Player.objects.all()
        dav = Davlat.objects.all()
        data = {
            "davlatlar": dav,
            "playerlar": players
        }
        return render(request,"players.html",data)

class RecordsView(View):
    def get(self, request):
        dav = Davlat.objects.all()
        transfer = Transfer.objects.filter(narx__gte=60)
        data = {
            "davlatlar": dav,
            "transferlar": transfer
        }
        return render(request,"records.html",data)

