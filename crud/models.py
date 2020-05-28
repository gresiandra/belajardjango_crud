from django.db import models

# Create your models here.

class smartphoneModel(models.Model):
    Nama = models.CharField(max_length=50)

    vendor = (
        ('Samsung','Samsung'),
        ('iPhone','iPhone'),
        ('Xiaomi','Xiaomi'),
        ('Huawei','Huawei'),
        ('Oppo','Oppo'),
        ('Realme','Realme'),
    )
    Brand = models.CharField(max_length=20, choices=vendor)

    TahunRilis = models.IntegerField()

    def __str__(self):
        return "{}. {}".format(self.id, self.Nama)
