from django.contrib import admin
from .models import tintuc
# Register your models here.

class TintucAdmin(admin.ModelAdmin):
    list_display = ("TenBai", "ngaygio")



admin.site.register(tintuc, TintucAdmin)