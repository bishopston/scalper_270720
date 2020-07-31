from django.db import models

class OptionSymbol(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class Option(models.Model):
    optionsymbol = models.CharField(max_length=15, default='_')
    date = models.DateTimeField()
    asset = models.CharField(max_length=10)
    optiontype = models.CharField(max_length=4)
    strike = models.DecimalField(max_digits = 11, decimal_places=2, default = 0.00)
    expmonthyear = models.DateField()
    closing_price = models.DecimalField(max_digits = 11, decimal_places=3)
    change = models.DecimalField(max_digits = 11, decimal_places=3)
    volume = models.IntegerField()
    max = models.DecimalField(max_digits = 11, decimal_places=3)
    min = models.DecimalField(max_digits = 11, decimal_places=3)
    trades = models.IntegerField()
    fixing_price = models.DecimalField(max_digits = 11, decimal_places=3)
    open_interest = models.IntegerField()

    def __str__(self):
	    return self.asset
