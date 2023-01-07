from django.db import models

# Create your models here.

class ContactDetails(models.Model):
    name       = models.CharField(max_length=255)
    phone      = models.CharField(max_length=255, unique=True)
    mail       = models.EmailField(unique=True)
    message    = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    status     = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Devise(models.Model):
    name          = models.CharField(max_length=255)
    setial_no     = models.CharField(max_length=255, unique=True)
    devise_id     = models.CharField(max_length=255, unique=True) #devise id or user name
    chipset_no    = models.CharField(max_length=255, unique=True)
    email         = models.EmailField()
    phone         = models.CharField(max_length=255)
    address1      = models.CharField(max_length=255)
    address2      = models.CharField(max_length=255)
    purchase_date = models.DateField()
    time_of_sale  = models.TimeField()
    warrenty      = models.DateField()
    amount_paid   = models.FloatField()
    balance_amount= models.FloatField(default=0)
    created_at    = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name + ' ' + self.devise_id

class DeviseApis(models.Model):
    device                = models.ForeignKey(to='Devise', on_delete=models.CASCADE)
    area_name             = models.CharField(max_length=255)
    devise_id             = models.CharField(max_length=255)
    serial_no             = models.CharField(max_length=255)
    electrical_conduction = models.FloatField(default=0.0)
    nitrogen              = models.FloatField(default=0.0)
    phosphorous           = models.FloatField(default=0.0)
    potassium             = models.FloatField(default=0.0)
    calcium               = models.FloatField(default=0.0)
    magnesium             = models.FloatField(default=0.0)
    sulphur               = models.FloatField(default=0.0)
    zinc                  = models.FloatField(default=0.0)
    manganese             = models.FloatField(default=0.0)
    iron                  = models.FloatField(default=0.0)
    copper                = models.FloatField(default=0.0)
    boron                 = models.FloatField(default=0.0)
    molybdenum            = models.FloatField(default=0.0)
    chlorine              = models.FloatField(default=0.0)
    nickel                = models.FloatField(default=0.0)
    organic_carboa        = models.FloatField(default=0.0)
    created_at            = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.device.name + ' ' + self.area_name


class DeviseLocation(models.Model):
    devise     = models.ForeignKey(to='Devise', on_delete=models.CASCADE, unique=True)
    latitude   = models.FloatField(default=0)
    longitude  = models.FloatField(default=0)
    status     = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.devise.name

class APICountThreshold(models.Model):
    devise = models.ForeignKey(to='Devise', on_delete=models.CASCADE, unique=True)
    red    = models.IntegerField()
    orange = models.IntegerField()
    blue   = models.IntegerField()
    green  = models.IntegerField()

    def __str__(self):
        return self.devise.name
