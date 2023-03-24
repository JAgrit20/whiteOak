

from django.contrib import admin
from .models import Payment_details

class RatingAdmin(admin.ModelAdmin):
    readonly_fields = ('date_time',)

admin.site.register(Payment_details,RatingAdmin)

# Register your models here.
