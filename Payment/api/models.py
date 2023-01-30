from django.db import models

# Create your models here.

class Payment(models.Model):
	name = models.CharField(max_length=50)
	surname = models.CharField(max_length=50)
	card_number = models.CharField(max_length=40)
	card_cvv = models.PositiveIntegerField()
	total_value = models.FloatField()
	extra_description = models.CharField(max_length=50, null=True)
	comission_value = models.FloatField()
