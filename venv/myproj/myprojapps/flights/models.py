from django.db import models
class Flight(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    flight_number = models.CharField(max_length=10)
    destination = models.CharField(max_length=100)
    departure_time = models.DateTimeField() 
    status = models.CharField(max_length=50) 
    def __str__(self):
        return f"{self.flight_number} - {self.destination}"

class Passenger(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    passport_number = models.CharField(max_length=20, unique=True) 
    flight = models.ForeignKey(Flight, on_delete=models. CASCADE)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
class Airplane(models.Model):
    model = models.CharField(max_length=50)
    capacity = models.IntegerField()
    airline = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.model} ({self.airline})"