from django.db.models import fields
from rest_framework import serializers
from .models import *

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class BranchDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = BranchData
        fields = '__all__'

class CustomerAddressDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerAddressData
        fields = '__all__'

class CustomerOfficeDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerOfficeData
        fields = '__all__'

class LoanAmountDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanAmountData
        fields = '__all__'

class ExcelFileUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExcelFileUpload
        exclude = ['updated', 'uploaded_at',]