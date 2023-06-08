from django.contrib import admin
from django.contrib.admin.models import LogEntry
from .models import Orders, Stores, Menus
admin.site.register(LogEntry)
admin.site.register(Orders)
admin.site.register(Stores)
admin.site.register(Menus)
