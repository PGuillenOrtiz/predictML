from django.contrib import admin
from .models import Principal, Predictivo, Campo_modelo, PersonalData

# Register your models here.
admin.site.register(Principal)
admin.site.register(Predictivo)
admin.site.register(Campo_modelo)
admin.site.register(PersonalData)
