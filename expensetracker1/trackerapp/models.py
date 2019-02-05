from django.db import models

# Create your models here.

class Customer(models.Model):
    cid = models.AutoField(primary_key = True)
    emailid = models.EmailField(max_length=254,null=False,unique=True)
    psswd = models.CharField(max_length=100,null=False )
    firstname = models.CharField(max_length=50,null=False )
    lastname = models.CharField(max_length=50, null=True )

class Wallet(models.Model):
    models.ForeignKey('Customer',on_delete=models.CASCADE,)
    wid = models.IntegerField(unique=True, null=False)
    wname = models.CharField(max_length=100,null=False )
    wamount = models.FloatField(null=False)

class Transaction(models.Model):
    CREDIT = 'Credit'
    DEBUT = 'Debut'
    TRANS_TYPE = ((CREDIT,'Cr'),(DEBUT,'Dr'))
    transaction = models.ForeignKey('Wallet', on_delete=models.CASCADE,)
    transtype =  models.CharField(max_length=10,
        choices=TRANS_TYPE,
        )
    amount = models.FloatField(null=False)
    transtime = models.DateTimeField(null=False)
