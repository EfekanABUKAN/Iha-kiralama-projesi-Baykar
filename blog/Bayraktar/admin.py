from django.contrib import admin
from .models import Bayraktar #kütüphane import edildi.
# Register your models here.
@admin.register(Bayraktar)
class BayraktarAdmin(admin.ModelAdmin):


    list_display = ["title","author","content"]
    list_display_links = ["title","author","content"]
    
    search_fields = ["title"]
    list_filter = ["title"]
    class Meta:
        model = Bayraktar

