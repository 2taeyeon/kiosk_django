from django.db import models

# Question -> 음료 종류(아메리카종류, 라떼, 차, 에이드)
# Choice -> 세부 음료 종류


class Drink(models.Model):
    drink_category = models.CharField(max_length=50)

    def __str__(self):
        return self.drink_category


class DrinkChoice(models.Model):
    drink = models.ForeignKey(Drink, on_delete=models.CASCADE)
    drink_list = models.CharField(max_length=50)

    def __str__(self):
        return self.drink_list
