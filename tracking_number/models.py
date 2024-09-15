from django.db import models


class TrackingNumberModel(models.Model):
    customer_id = models.UUIDField()
    customer_name = models.CharField(max_length=255)
    customer_slug = models.SlugField(max_length=255)
    tracking_number = models.CharField(max_length=16, unique=True)
    origin_country_id = models.CharField(max_length=2)
    destination_country_id = models.CharField(max_length=2)
    weight = models.DecimalField(max_digits=7, decimal_places=3)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [models.Index(fields=['tracking_number'])]
