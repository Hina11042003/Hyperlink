from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import profile

@admin.register(profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display  = ['full_name', 'email', 'gender', 'dob']  # columns to show
    search_fields = ['full_name', 'email']                    # search bar
    list_filter   = ['gender', 'agree']                       # filter sidebar