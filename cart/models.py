from django.db import models
from django.db.models.signals import post_save


# Create your models here.
class CartData(models.Model):
    id = models.AutoField(primary_key=True)
    product_id = models.IntegerField()
    product_name = models.CharField(max_length=100)
    product_quantity = models.IntegerField(default=1)

    class Meta:
        verbose_name = "Cart List"  # django admin page name change


class ProductPrice(models.Model):
    price_id = models.OneToOneField(CartData, on_delete=models.CASCADE, related_name="lol")
    price = models.FloatField(default=44)

    def __str__(self):
        return str(self.price)

    class Meta:
        verbose_name = "Price List"


class PostSave(models.Model):
    entry = models.CharField(max_length=100, default="default")
    created = models.DateTimeField(auto_now_add=True)


def demo_post_save(sender, **kwargs):
    PostSave.objects.create()


post_save.connect(demo_post_save, sender=CartData) # function and then model
