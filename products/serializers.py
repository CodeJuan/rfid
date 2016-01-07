from rest_framework import serializers
from products.models import CheckIn


class CheckinSerializer(serializers.ModelSerializer):

    class Meta:
        model = CheckIn
        fields = ('RFID', 'AntennaID', 'User', 'Shop', 'Weight')