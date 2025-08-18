from django.shortcuts import render , HttpResponse
from . import models

categ = {
        "موبایل و تجهیزات" : {
            "موبایل" : "#",
            "شارژر" : "#",
            "قاب موبایل" : "#",
            "تجهیزات جانبی" : "#"
        },
        "کامپیوتر و لپ تاپ" :{
            "کیس کامپیوتر" : "#",
            "مانیتور" : "#",
            "موس و کیبورد" : "#",
            "لپ تاپ" : "#",
            "میز کامپیوتر" : "#",
            "شارژر لپ تاپ" : "#"
        },
        "لوازم تحریر و کتاب" :{
            "خودکار و مداد" : "#",
            "چراغ مطالعه" : "#",
            "کوله پشتی" : "#",
            "دفتر" : "#",
            "کتاب داستان" : "#"
        },
        "خانه و آشپزخانه" :{
            "تلویزیون" : "#",
            "مبل و صندلی" : "#",
            "یخچال" : "#",
            "ماشین لباس شویی" : "#",
            "میز غذاخوری" : "#",
            "فرش و موکت" : "#"
        },
        "ورزشی" :{
            "توپ ورزشی" : "#",
            "کفش ورزشی" : "#",
            "لباس ورزشی" : "#",
            "فلاسک" : "#",
            "دوچرخه" : "#",
            "دمبل و هالتر" : "#"
        },
        "مد و پوشاک" :{
            "تیشرت و پیراهن" : "#",
            "هودی" : "#",
            "کت و کاپشن" : "#",
            "شلوار" : "#",
            "کفش" : "#"
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