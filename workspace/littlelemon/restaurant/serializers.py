from rest_framework import serializers
from .models import MenuItem, Booking

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['id','Title','Price','Inventory']
        extra_kwargs = {
            'price': {'min_value': 2},
            'inventory':{'min_value':0}
        }
        
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id','Name', 'BookingDate']
