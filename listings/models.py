from django.db import models
from datetime import datetime
from realtors.models import Realtor

class Listing(models.Model):
    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=40)
    zip = models.CharField(max_length=15)
    description = models.TextField(null=True, blank=True)
    price = models.IntegerField(null=True)
    bedrooms = models.IntegerField(null=True)
    bathrooms = models.DecimalField(max_digits=2, decimal_places=1, null=True)
    garage = models.IntegerField(default=0, null=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)
    sqft = models.IntegerField(null=True)
    lot_size = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    is_published = models.BooleanField(default=True, verbose_name="Published")
    photo_main = models.ImageField(max_length=200, blank=False, null=True, upload_to='photos/%Y/%m/%d/', help_text="Main Photo")
    photo_1 = models.ImageField(max_length=200, blank=True, null=True, upload_to='photos/%Y/%m/%d/', help_text="Photo 1")
    photo_2 = models.ImageField(max_length=200, blank=True, null=True, upload_to='photos/%Y/%m/%d/', help_text="Photo 2")
    photo_3 = models.ImageField(max_length=200, blank=True, null=True, upload_to='photos/%Y/%m/%d/', help_text="Photo 3")
    photo_4 = models.ImageField(max_length=200, blank=True, null=True, upload_to='photos/%Y/%m/%d/', help_text="Photo 4")
    photo_5 = models.ImageField(max_length=200, blank=True, null=True, upload_to='photos/%Y/%m/%d/', help_text="Photo 5")
    photo_6 = models.ImageField(max_length=200, blank=True, null=True, upload_to='photos/%Y/%m/%d/', help_text="Photo 6")

    def __str__(self):
        return self.title
