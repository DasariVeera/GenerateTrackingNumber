import re
import string
import random

from rest_framework import serializers
from .models import TrackingNumberModel


class TrackingNumberModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrackingNumberModel
        fields = ['tracking_number', 'customer_id', 'origin_country_id', 'destination_country_id', 'created_at']


class NewTrackingNumberSerializer(serializers.ModelSerializer):
    origin_country_id = serializers.CharField(
        max_length=2,
        error_messages={
            'max_length': "The order’s Origin country code must be 2 characters (ISO 3166-1 alpha-2 format)",
            'blank': 'Origin country code is required.'
        }
    )
    destination_country_id = serializers.CharField(
        max_length=2,
        error_messages={
            'max_length': "The order’s Destination country code must be 2 characters (ISO 3166-1 alpha-2 format)",
            'blank': 'Destination country code is required.'
        }
    )

    class Meta:
        model = TrackingNumberModel
        fields = [
            'origin_country_id', 'destination_country_id', 'weight', 'customer_id',
            'customer_name', 'customer_slug', 'created_at'
        ]

    def validate_weight(self, value):
        """Ensure that weight is a positive value."""
        if value <= 0:
            raise serializers.ValidationError("Weight must be a positive number in kilograms, up to three decimal places.")
        return value

    def validate_customer_slug(self, value):
        if not re.match(r'^[a-z]+(-[a-z]+)*$', value):
            raise serializers.ValidationError("The customer’s name must be in slug-case/kebab-case")
        return value

    def create(self, validated_data):
        for i in range(10):
            tracking_number = self.get_unique_tracking_number()
            if not TrackingNumberModel.objects.select_for_update().filter(tracking_number=tracking_number).exists():
                validated_data['tracking_number'] = tracking_number
                return super().create(validated_data)
        raise serializers.ValidationError("Unable to generate a unique tracking number.")

    def get_unique_tracking_number(self):
        return (self.validated_data['origin_country_id'] + self.validated_data['destination_country_id']).upper() + \
            ''.join(random.choices(string.ascii_uppercase + string.digits, k=12))
