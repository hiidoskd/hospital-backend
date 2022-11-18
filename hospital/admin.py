from django.contrib import admin
from .models import DiseaseType, Disease, Country, Discover, User, PublicServant, Record, Specialize, Doctor

# Register your models here.

admin.site.register(DiseaseType)
admin.site.register(Country)
admin.site.register(Disease)
admin.site.register(Discover)
admin.site.register(User)
admin.site.register(PublicServant)
admin.site.register(Doctor)
admin.site.register(Specialize)
admin.site.register(Record)