from django.db import models

class Item(models.Model):
    item_name = models.CharField( default = None , max_length=50)
    slug = models.SlugField(default = None)
    properties = models.TextField(default = None)
    # " body:iron ; handle:wood "
    # in html , add a + botton to make 2 fields
    # when  wrote , add all to propertes

    image = models.ImageField(default='def.jpg' , blank=True)
    about = models.TextField(default = None)
    price = models.IntegerField(default = None)
    off = models.IntegerField(default = None)
    # categorie
    big_cat = models.CharField(default = None , max_length=50)
    sml_cat = models.CharField(default = None , max_length=50)

    def __str__(self):
        return self.item_name
    # comments
    # img
    # seller
    # anvae mokhtalef (color - size - etc)
