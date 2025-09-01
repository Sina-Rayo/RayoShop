from django.shortcuts import render , HttpResponse
from . import models

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