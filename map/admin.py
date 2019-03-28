from django.contrib import admin
from map.models import UserProfileInfo , Parameters , SIR

# Registering following Models to admin site

admin.site.register(UserProfileInfo)
admin.site.register(Parameters)
admin.site.register(SIR)

