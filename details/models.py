from django.db import models

# Create your models here.
class Vehicle(models.Model):
    vehicle_type = models.CharField(max_length=50)
    size = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    vehicle = models.CharField(max_length=50)
    # autopilot = models.BooleanField(default=True)
    transmission = models.IntegerField()

    def __str__(self):
        return f"{self.vehicle_type}"

class Cars(models.Model):
    # Characters
    # id = models.CharField(max_length=10, null=True, blank=True)
    id = models.CharField(max_length=10, unique=True, primary_key=True)  # HQ0001
    # id = models.CharField(max_length=10, unique=True)  # HQ0001
    name = models.CharField(max_length=100)  # BMW
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    model = models.CharField(max_length=100)
    # age = models.IntegerField(default=18)
    engine_no = models.CharField(max_length=70)
    color = models.CharField(max_length=50)
    fuel_type = models.CharField(max_length=100)
    # Optional Field
    def upload_img(self, filename):
        path = "details/images/{}".format(filename)
        return path

    image = models.ImageField(upload_to=upload_img, null=True, blank=True)

    def __str__(self):
        return f"{self.name} - {self.model}"
