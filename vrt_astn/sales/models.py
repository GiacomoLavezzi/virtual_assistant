from django.db import models

# Create your models here.

#macro
class Category(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name
    
#specs
class Brand(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

class Proportions(models.Model):
    ratio = models.CharField(max_length=16)

    def __str__(self):
        return self.ratio

class Resolution(models.Model):
    resolution = models.CharField(max_length=32)

    def __str__(self):
        return self.resolution

class Refresh_Rate(models.Model):
    hertz = models.FloatField()

    def __str__(self):
        return f"{self.hertz} Hz"
    
class Port(models.Model):
    name = models.CharField(max_length=16)

    def __str__(self):
        return self.name
    
class Spec(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name
    
class Architecture(models.Model):
    description = models.CharField(max_length=16)

    def __str__(self):
        return self.description
    
class Platform(models.Model):
    name = models.CharField(max_length=16)

    def __str__(self):
        return self.name
    
class Socket(models.Model):
    type = models.CharField(max_length=16)

    def __str__(self):
        return self.type 
    
class Cores(models.Model):
    number = models.IntegerField()

    def __str__(self):
        return f"{self.number} cores"

#products
class Monitor(models.Model):
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, related_name="monitors")
    name = models.CharField(max_length=64)
    serial = models.CharField(max_length=32)
    brand = models.ForeignKey(Brand, on_delete=models.DO_NOTHING, related_name="monitors")
    power = models.FloatField()
    size = models.FloatField()
    proportions = models.ForeignKey(Proportions, on_delete=models.DO_NOTHING, related_name="monitors")
    resolution = models.ForeignKey(Resolution, on_delete=models.DO_NOTHING, related_name="monitors")
    refresh_rate = models.ForeignKey(Refresh_Rate, on_delete=models.DO_NOTHING, related_name="monitors")
    response_time = models.FloatField()
    ports = models.ManyToManyField(Port, related_name="monitors")
    specs = models.ManyToManyField(Spec, related_name="monitors")

    def __str__(self):
        return f"[{self.brand}] {self.name}"

class Cpu(models.Model):
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, related_name="cpus")
    name = models.CharField(max_length=64)
    serial = models.CharField(max_length=32)
    brand = models.ForeignKey(Brand, on_delete=models.DO_NOTHING, related_name="cpus")
    frequency = models.FloatField()
    architecture = models.ForeignKey(Architecture, on_delete=models.DO_NOTHING, related_name="cpus")
    platform = models.ManyToManyField(Platform, related_name="cpus")
    socket = models.ForeignKey(Socket, on_delete=models.DO_NOTHING, related_name="cpus")
    power = models.FloatField()
    cores = models.ForeignKey(Cores, on_delete=models.DO_NOTHING, related_name="cpus")
    cache = models.FloatField()
    specs = models.ManyToManyField(Spec, related_name="cpus")

    def __str__(self):
        return f"[{self.brand}] {self.name}"