from rest_framework import serializers
from details.models import Cars
from details.models import Vehicle

class CarsSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(required=False)
    class Meta:
        model = Cars
        fields = '__all__'
        # fields = ('name', 'model')

class VehicleSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(required=False)
    class Meta:
        model = Vehicle
        fields = '__all__'
        # fields = ('name', 'model')