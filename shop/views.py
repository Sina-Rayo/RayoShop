from django.shortcuts import render
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from . import models
from .models import User
from .serializers import ItemSerializer , ItemCreateSerializer , UserSerializer

categ = {
    "Mobile & Accessories": {
        "Mobile": "#",
        "Charger": "#",
        "Phone Case": "#",
        "Accessories": "#"
    },
    "Computer & Laptop": {
        "Computer Case": "#",
        "Monitor": "#",
        "Mouse & Keyboard": "#",
        "Laptop": "#",
        "Computer Desk": "#",
        "Laptop Charger": "#"
    },
    "Stationery & Books": {
        "Pen & Pencil": "#",
        "Desk Lamp": "#",
        "Backpack": "#",
        "Notebook": "#",
        "Story Book": "#"
    },
    "Home & Kitchen": {
        "Television": "#",
        "Sofa & Chair": "#",
        "Refrigerator": "#",
        "Washing Machine": "#",
        "Dining Table": "#",
        "Carpet & Rug": "#"
    },
    "Sports": {
        "Sports Ball": "#",
        "Sports Shoes": "#",
        "Sportswear": "#",
        "Flask": "#",
        "Bicycle": "#",
        "Dumbbell & Barbell": "#"
    },
    "Fashion & Clothing": {
        "T-Shirt & Shirt": "#",
        "Hoodie": "#",
        "Coat & Jacket": "#",
        "Pants": "#",
        "Shoes": "#"
    }
}


def main_shop(request):
    all_items = models.Item.objects.all()
    return render(request , 'shopmain.html' , {'categ':categ , 'items':all_items})

def big_categorie(request , slug):
    all_items = models.Item.objects.filter(big_cat = slug)
    return render(request ,'bigi.html' , {'categ':categ , "items":all_items , "pname":slug , "bc":categ[slug]})

def small_categorie(request , slug):
    all_items = models.Item.objects.filter(sml_cat = slug)
    return render(request ,'smli.html' , {'categ':categ , "items":all_items , "pname":slug})

def item_page(request , slug):
    the_item = models.Item.objects.get(slug = slug)
    return render(request , 'item_p.html' , {'categ':categ , "item" : the_item})

def create_item(request):
    if request.method == "POST":
        form = request.POST.dict()
        iname = form['iname']
        iabout = form['iabout']
        iprice = form['iprice']
        ioff = form['ioff']
        icat = form['categor']
        bcat = ""
        for b in categ:
            if icat in b:
                bcat = b

        it = models.Item(item_name=iname , slug=iname.strip() , properties ="" , about=iabout
                            ,price=iprice , off=ioff , sml_cat=icat , big_cat=bcat )
        it.save()

    return render(request , 'create_item.html' , {'categ':categ })


########  API ENDPOINTS  ########

@api_view(['GET'])
def api_main_page(request:Request):
    all_items = ItemSerializer(models.Item.objects.all() , many=True)
    return Response({'categ':categ , 'items':all_items.data} , status.HTTP_200_OK)

@api_view(['GET'])
def api_big_categorie(request:Request , slug):
    all_items = ItemSerializer(models.Item.objects.filter(big_cat=slug) , many=True)
    return Response({'big_categorie':slug, 'small_categories':categ[slug] , 'items':all_items.data} , status.HTTP_200_OK)

@api_view(['GET'])
def api_small_categorie(request:Request , slug):
    all_items = ItemSerializer(models.Item.objects.filter(sml_cat = slug) , many=True)
    return Response({'small_categorie':slug, 'items':all_items.data} , status.HTTP_200_OK)

@api_view(['GET'])
def api_item_page(request:Request , slug):
    the_item = ItemSerializer(models.Item.objects.get(slug = slug))
    return Response({'item':the_item.data} , status.HTTP_200_OK)

@api_view(['GET'])
def api_search(request:Request , slug):
    all_items = ItemSerializer(models.Item.objects.filter(item_name__icontains=slug) , many=True)
    return Response({'items':all_items.data} , status.HTTP_200_OK)

@api_view(["POST"])
@permission_classes([IsAuthenticated]) 
def api_create_item(request:Request):
    if not request.user.is_admin_or_manager():  
        return Response({"detail": "Not allowed"}, status=403)
    
    serializer = ItemCreateSerializer(data=request.data)
    if serializer.is_valid():
        iname = serializer.validated_data['name']
        islug = iname.replace(" ", "")
        try:
                models.Item.objects.get(slug=islug)
                return Response({'Item already exists'}, status=200) 
        except Exception as e:
                print(e)
                pass
        iabout = serializer.validated_data['about']
        iprice = serializer.validated_data['price']
        ioff = serializer.validated_data['off']
        icat = serializer.validated_data['categor']
        # icat = Categorie.objects.get(pk=int(ncat))
        bcat = ""
        
        for b in categ:
            if icat in b:
                bcat = b

        it = models.Item(item_name=iname , slug=islug , properties ="" , about=iabout
                            ,price=iprice , off=ioff , sml_cat=icat , big_cat=bcat )
        it.save()

        return Response({'Item has been made Successfully'}, status=200)
    return Response({'Not valid'}, status=200)


@api_view(['POST'])
def api_login(request:Request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        username = serializer.validated_data['username']
        password = serializer.validated_data['password']
    else:
        return Response({'Not valid'}, status=200)
    
    if not username or not password:
        return Response({"detail": "Username and password required"}, status=400)

    user = authenticate(username=username, password=password)
    if not user:
        return Response({"detail": "Invalid credentials"}, status=401)

    token, created = Token.objects.get_or_create(user=user)

    return Response({
        "token": token.key,
        "username": user.username,
        "role": user.role,
    })

@api_view(['POST'])
def api_signup(request:Request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        username = serializer.validated_data['username']
        password = serializer.validated_data['password']
    else:
        return Response({'Not valid'}, status=200)
    
    if not username or not password:
        return Response({"detail": "Username and password required"}, status=400)

    if User.objects.filter(username=username).exists():
        return Response({"detail": "Username already taken"}, status=400)

    user = User.objects.create_user(username=username, password=password, role="customer")
    token, created = Token.objects.get_or_create(user=user)

    return Response({
        "token": token.key,
        "username": user.username,
        "role": user.role,
    }, status=201)


# {
#     "name":"com",
#     "about":"good com",
#     "price":100,
#     "off":10,
#     "categor":"Computer Case"
# }
# Token e666a33ffce972c236ef85058d0b0bc920204789
# Token 7819ac9bc59b40fddcbf0f54cb1cdbb873f6a738