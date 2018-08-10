from django.contrib import admin

from .models import Currency, State, Trim, VModel, Manufacturer, Vehicle

admin.site.register(Currency)
admin.site.register(State)
admin.site.register(Trim)
admin.site.register(VModel)
admin.site.register(Manufacturer)
admin.site.register(Vehicle)
