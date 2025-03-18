from django.db import models


class ItemStock(models.Model):
    item = models.ForeignKey('Item', on_delete=models.CASCADE)
    location = models.ForeignKey('Location', on_delete=models.CASCADE)
    stock = models.IntegerField()

    class Meta:
        unique_together = ('item', 'location')

    def __str__(self):
        return f'{self.item.name} at {self.location.name} has {self.stock} units'
