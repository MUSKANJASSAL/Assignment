from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *

class UserAuthentication(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context=('request', request))
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response(token.key)

class VehicleList(APIView):
    #  GET, PUT, POST, DELETE
    def get(self, request):

        model = Vehicle.objects.all()
        serializer = VehicleSerializer(model, many=True)
        return Response(serializer.data)

    #   New object
    def post(self, request):
        serializer = VehicleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class URLDetail1(APIView):
    #  GET, PUT, POST, DELETE
    def get_vehicle(self, id):
        try:
            model = Vehicle.objects.get(id=id)
            return model
        except Vehicle.DoesNotExist:
            # return Response(f' Car with id {id} is not found in database', status=status.HTTP_404_NOT_FOUND)
            return

    def get(self, request, id):
        if not self.get_vehicle(id):
            Response(f' Vehicle with id {id} is not found in database', status=status.HTTP_404_NOT_FOUND)
        serializer = VehicleSerializer(self.get_vehicle(id))
        return Response(serializer.data)

    def put(self, request, id):
        if not self.get_vehicle(id):
            Response(f' Vehicle with id {id} is not found in database', status=status.HTTP_404_NOT_FOUND)
        serializer = VehicleSerializer(self.get_vehicle(id), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        if not self.get_vehicle(id):
            Response(f' Vehicle with id {id} is not found in database', status=status.HTTP_404_NOT_FOUND)
        model = self.get_vehicle(id)
        model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# List of all Cars

class CarList(APIView):
    #  GET, PUT, POST, DELETE
    def get(self, request):

        model = Cars.objects.all()
        serializer = CarsSerializer(model, many=True)
        return Response(serializer.data)

    #   New object
    def post(self, request):

        serializer = CarsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#   Different URL
class URLDetail2(APIView):
    #  GET, PUT, POST, DELETE
    def get_car(self, id):
        try:
            model = Cars.objects.get(id=id)
            return model
        except Cars.DoesNotExist:
            # return Response(f' Car with id {id} is not found in database', status=status.HTTP_404_NOT_FOUND)
            return

    def get(self, request, id):
        if not self.get_car(id):
            Response(f' Car with id {id} is not found in database', status=status.HTTP_404_NOT_FOUND)
        serializer = CarsSerializer(self.get_car(id))
        return Response(serializer.data)

    def put(self, request, id):
        if not self.get_car(id):
            Response(f' Car with id {id} is not found in database', status=status.HTTP_404_NOT_FOUND)
        serializer = CarsSerializer(self.get_car(id), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        if not self.get_car(id):
            Response(f' Car with id {id} is not found in database', status=status.HTTP_404_NOT_FOUND)
        model = self.get_car(id)
        model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
