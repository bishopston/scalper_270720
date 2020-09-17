from django.db import models

class OptionSymbol(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class OptionAsset(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Option(models.Model):
    optionsymbol = models.CharField(max_length=15, default='_')
    date = models.DateTimeField()
    asset = models.CharField(max_length=10)
    optiontype = models.CharField(max_length=4)
    strike = models.FloatField()
    expmonthyear = models.DateField()
    closing_price = models.FloatField()
    change = models.FloatField()
    volume = models.IntegerField()
    max = models.FloatField()
    min = models.FloatField()
    trades = models.IntegerField()
    fixing_price = models.FloatField()
    open_interest = models.IntegerField()

    def __str__(self):
	    return self.optionsymbol

class Future(models.Model):
    futuresymbol = models.CharField(max_length=15, default='_')
    date = models.DateTimeField()
    asset = models.CharField(max_length=10)
    expmonthyear = models.DateField()
    closing_price = models.FloatField()
    change = models.FloatField()
    volume = models.IntegerField()
    max = models.FloatField()
    min = models.FloatField()
    trades = models.IntegerField()
    fixing_price = models.FloatField()
    open_interest = models.IntegerField()

    def __str__(self):
	    return self.futuresymbol

class Stock(models.Model):
    symbol = models.CharField(max_length=15, default='_')
    date = models.DateTimeField()
    high = models.FloatField()
    low = models.FloatField()
    open = models.FloatField()
    close = models.FloatField()
    volume = models.FloatField()

    def __str__(self):
	    return self.symbol