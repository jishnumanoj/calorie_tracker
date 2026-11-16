from django.db import models

# Create your models here.
from accounts.models import User

class FoodLog(models.Model):

    title = models.CharField(max_length=200,null=True)

    MEAL_TYPE_CHOICES = [
        ("breakfast","Breakfast"),
        ("lunch","Lunch"),
        ("snack","Snack"),
        ("dinner","Dinner")
    ]

    meal_type = models.CharField(max_length=20,choices=MEAL_TYPE_CHOICES,default="food")

    quantity = models.CharField(max_length=200)

    calorie = models.FloatField()

    owner = models.ForeignKey(User,on_delete=models.CASCADE)

    food_image = models.ImageField(upload_to="food",null=True)

    created_at = models.DateTimeField(auto_now_add=True)


