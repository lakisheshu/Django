from django.shortcuts import render
from .models import Destination
import random,json
# Create your views here.

def travell(request):
     # def travello():
     # dest=["Mumbai","Bangalore","Chennai"]
     # discrption=["The city Don't sleep",'The city with full of traffic',"The city high  sunny "]
     # destinations=[]
     # # for i in range(len(dest)):
     # destination=Destination()
     # destination.name="Mumbai"
     # destination.img='destination_1.jpg'
     # destination.disc= "The city Don't sleep"
     # destination.offer=True
     # destination.price=random.randint(600,700)

     dests=Destination.objects.all()
     return render(request, 'index.html',{ "dests":dests })


# k=travello()
# l=k["data"]
# print(k['data']['place0']['Name'])