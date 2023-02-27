from django.contrib import admin

# Register your models here.

from .models import Service, Plan, Subscription

admin.site.register(Service)
admin.site.register(Plan)
admin.site.register(Subscription)