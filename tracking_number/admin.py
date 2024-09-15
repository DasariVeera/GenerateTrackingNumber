from django.contrib import admin

from .models import TrackingNumberModel


@admin.register(TrackingNumberModel)
class TrackingNumberModelAdmin(admin.ModelAdmin):
    list_display = ('customer_id', 'origin_country_id', 'destination_country_id', 'created_at')
