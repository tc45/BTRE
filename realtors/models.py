from django.db import models


class Realtor(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(max_length=200, upload_to='photos/%Y/%m/%d/', help_text="Realtor Photo", blank=True)
    description = models.TextField(blank=True)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    is_mvp = models.BooleanField(default=False)
    hire_date = models.DateTimeField()

    def __str__(self):
        return self.name