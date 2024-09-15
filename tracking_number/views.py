import time
from rest_framework import status
from django.db import OperationalError
from rest_framework.response import Response

from rest_framework.views import APIView
from .serializers import TrackingNumberModelSerializer, NewTrackingNumberSerializer


class TrackingNumberAPIView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            required_tracking_details = ['customer_id', 'customer_name', 'customer_slug', 'origin_country_id', 'destination_country_id', 'weight']
            tracking_number_data = {key: request.query_params.get(key, '') for key in required_tracking_details}
            serializer = NewTrackingNumberSerializer(data=tracking_number_data)
            if serializer.is_valid():
                try:
                    serializer.save()
                    tracking_details = TrackingNumberModelSerializer(serializer.instance).data
                    return Response(tracking_details, status=status.HTTP_201_CREATED)
                except OperationalError as ex:
                    retry_database_operation(serializer)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            return Response({'Error': str(ex)}, status=status.HTTP_400_BAD_REQUEST)


def retry_database_operation(serializer, retries=3, delay=0.1):
    attempt = 0
    while attempt < retries:
        try:
            serializer.save()
            return
        except OperationalError as e:
            if "database is locked" in str(e):
                attempt += 1
                time.sleep(delay)

                if attempt == retries:
                    raise e
            else:
                raise e
