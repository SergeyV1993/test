from django.db import models

class Cars(models.Model):
    name = models.CharField(max_length=128)
    number = models.CharField(max_length=128)
    max_weight = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    current_weight = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    overweight = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.overweight = 0.0
        self.overweight = (self.current_weight / self.max_weight) * 100 - 100
        super().save(*args, **kwargs)

