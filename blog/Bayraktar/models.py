from django.db import models


# Create your models here.

class Bayraktar(models.Model):
    author = models.ForeignKey("auth.User",on_delete =models.CASCADE,verbose_name ="Kullanıcı")
    title = models.CharField(max_length = 50,verbose_name ="Ucak Bilgileri") # secenekler türkceye cevirildi.
    content = models.TextField(verbose_name ="Agırlık")
    created_date = models.DateTimeField(auto_now_add=True,verbose_name ="Tarih")
    def __str__(self):
        return self.title
