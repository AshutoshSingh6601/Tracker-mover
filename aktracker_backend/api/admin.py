from django.contrib import admin
from .models import Client, Partner 

# Register your models here.

class ClientAdmin(admin.ModelAdmin):
    list_display = ['city', 'name', 'contact', 'moveFrom', 'moveTo']
admin.site.register(Client, ClientAdmin)


class PartnerAdmin(admin.ModelAdmin):
    list_display = ['name', 'contact', 'image', 'city', 'rantal', 'seeUs']
admin.site.register(Partner, PartnerAdmin)

