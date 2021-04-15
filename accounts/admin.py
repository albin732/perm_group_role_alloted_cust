from django.contrib import admin
from .models import DetailModel

# Register your models here.


class AdmDetail(admin.ModelAdmin):
    list_display = ('user', 'user_type')


admin.site.register(DetailModel, AdmDetail)
