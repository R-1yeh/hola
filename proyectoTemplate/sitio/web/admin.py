from django.contrib import admin

# Register your models here.


# web/admin.py
from django.contrib import admin
from .models import Donation

@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'amount', 'date')  # Campos a mostrar en la lista
    list_filter = ('date',)  # Filtros en la barra lateral
    search_fields = ('name', 'email')  # Búsqueda por nombre y email
    ordering = ('-date',)  # Ordenar por fecha, descendente

# También puedes registrar el modelo de esta manera:
# admin.site.register(Donation, DonationAdmin)
from django.contrib import admin
from .models import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title',  'description', 'image', 'date')  # Campos a mostrar en la lista
    list_filter = ('title',)  # Filtros en la barra lateral
    search_fields = ('title',)  # Búsqueda por nombre y email
    ordering = ['-date',]  # Asegúrate de que 'created_at' exista en tu modelo