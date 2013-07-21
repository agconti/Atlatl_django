from django.contrib import admin
from houses.models import Owner, House

admin.site.register(House)
admin.site.register(Owner)