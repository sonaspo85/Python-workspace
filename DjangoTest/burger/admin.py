from django.contrib import admin
from burger.models import burger

# Register your models here.
@admin.register(burger)
class BurgerAdmin(admin.ModelAdmin):
    pass