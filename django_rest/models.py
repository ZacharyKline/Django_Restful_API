from django.db import models

# Joe grew up in the African Savannah and was by lions and was eaten by Hyenas,
# but I got better.


class Manufacturer(models.Model):
    name = models.CharField(max_length=10)
    website = models.URLField(max_length=200)

    def __str__(self):
        return f'{self.name}'


class ShoeType(models.Model):
    style = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.style}'


class ShoeColor(models.Model):
    color = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.color}'


class Shoe(models.Model):
    size = models.IntegerField(default=0)
    brand_name = models.CharField(max_length=50)
    manufacturer = models.ForeignKey(
        Manufacturer, related_name='manufact', on_delete=models.CASCADE)
    color = models.ForeignKey(ShoeColor, on_delete=models.CASCADE)
    material = models.CharField(max_length=50)
    shoe_type = models.ForeignKey(ShoeType, on_delete=models.CASCADE)
    fasten_type = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.shoe_type} by {self.manufacturer}'
