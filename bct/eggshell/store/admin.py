from django.contrib import admin
from .models import Admin

# Register your models here.
class userAdmin(admin.ModelAdmin):
    list_display=('name','price','quantity')
admin.site.register(Admin,userAdmin)
