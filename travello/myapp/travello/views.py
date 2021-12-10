from django.shortcuts import render

from travello.models import Destination
from .models import Destination

# Create your views here.


def index(request):
    dest1=Destination()
    dest1.name='Bali'
    dest1.desc = "Bali, land of the gods"
    dest1.img="destination_1.jpg"
    dest1.price= 715
    dest1.offer=False

    dest2 = Destination()
    dest2.name = 'Indonesia'
    dest2.desc = '"Wonderful Indonesia" and what do you think about it?'
    dest2.img = "destination_2.jpg"
    dest2.price = 500
    dest2.offer = True

    dest3 = Destination()
    dest3.name = 'San Francisco'
    dest3.desc = "Everybody's Favorite City,"
    dest3.img = "destination_3.jpg"
    dest3.price = 679
    dest3.offer = False

    dest4 = Destination()
    dest4.name = 'Paris'
    dest4.desc = "The City of lights."
    dest4.img = "destination_4.jpg"
    dest4.price = 615
    dest4.offer = False

    dest5 = Destination()
    dest5.name = 'Rome'
    dest5.desc = "Rome and You"
    dest5.img = "why.jpg"
    dest5.price = 685
    dest5.offer = False

    dests=[dest1,dest2,dest3,dest4,dest5]

    return render(request,'index.html',{"dests": dests})
