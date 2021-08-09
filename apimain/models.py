from django.db import models
from django.db.models.deletion import DO_NOTHING

# Create your models here.
class Customer(models.Model):
    customerName = models.CharField(max_length=100)
    fatherName = models.CharField(max_length=100)
    phoneNumber = models.CharField(max_length=10)
    dob = models.DateField()
    loanAccountNumber = models.CharField(max_length=100)
    
    def __str__(self):
        return self.customerName

class BranchData(models.Model):
    zoneName = models.CharField(max_length=100)
    regionName = models.CharField(max_length=100)
    areaName = models.CharField(max_length=100)
    branchName = models.CharField(max_length=100)
    branchCode = models.CharField(max_length=100)

    def __str__(self):
        return self.branchCode

class CustomerAddressData(models.Model):
    customer = models.ForeignKey(Customer,on_delete=DO_NOTHING)
    pincode = models.CharField(max_length=100)
    landmark = models.CharField(max_length=100)   
    address1 = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100)
    address3 = models.CharField(max_length=100)

    def __str__(self):
        return self.customer.customerName

class CustomerOfficeData(models.Model):
    customer = models.ForeignKey(Customer,on_delete=DO_NOTHING)
    pincode = models.CharField(max_length=100)
    landmark = models.CharField(max_length=100)
    address1 = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100)
    address3 = models.CharField(max_length=100)

    def __str__(self):
        return self.customer.customerName


class LoanAmountData(models.Model):
    customer = models.ForeignKey(Customer,on_delete=DO_NOTHING)
    agreementDate = models.DateField()
    LRN = models.IntegerField()
    tenor = models.IntegerField()
    advEMI = models.IntegerField()
    mob = models.IntegerField()

    def __str__(self):
        return self.customer.customerName

class ExcelFileUpload(models.Model):
    file = models.FileField(upload_to='excel/')
    TABLE = [('CUSTOMER','CUSTOMER'),('CUSTOMER_ADDRESS','CUSTOMER_ADDRESS'),('CUSTOMER_OFFICE','CUSTOMER_OFFICE'),('LOAN_AMOUNT','LOAN_AMOUNT'),('BRANCH_DATA','BRANCH_DATA')]
    table = models.CharField(max_length=100,choices=TABLE)
    updated = models.BooleanField(default=False)
    uploaded_at = models.DateTimeField(auto_now_add=True)
