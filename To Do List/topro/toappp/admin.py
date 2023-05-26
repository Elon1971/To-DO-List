from django.contrib import admin
from .models import to_do_list
from .forms import to_do_Form

@admin.register(to_do_list)
class admin(admin.ModelAdmin):
    form = to_do_Form
    list_display = ('Sr_No', 'name', 'category', 'description', 'date')
    list_filter = ('Sr_No', 'name', 'category', 'description', 'date')



