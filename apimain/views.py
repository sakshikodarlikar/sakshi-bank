from django.shortcuts import render
from rest_framework.views import APIView
from .models import *
from .serializers import *
import pandas as pd
from rest_framework.response import Response
import uuid
from rest_framework import status
from django.conf import settings
import openpyxl
from rest_framework import viewsets
# Create your views here.

from django.views.decorators.csrf import csrf_exempt   

def add_to_database():
    files = ExcelFileUpload.objects.filter(updated=False)
    for file in files:
        try:
            df = pd.read_excel(f"{settings.BASE_DIR}/{file.file}")
            count = df.shape[0]
            if file.table == 'CUSTOMER':
                for i in range(0,count):
                    customerName = df.iat[i, 1]
                    fatherName = df.iat[i, 2]
                    phoneNumber = df.iat[i, 3]
                    dob = df.iat[i, 4]
                    loanAccountNumber = df.iat[i, 5]
                    customer = Customer.objects.create(customerName=customerName,fatherName=fatherName,phoneNumber=phoneNumber,dob=dob,loanAccountNumber=loanAccountNumber)
                    customer.save() 
            elif file.table == 'CUSTOMER_ADDRESS':
                for i in range(0,count):
                    
                    pincode = df.iat[i, 1]
                    landmark = df.iat[i, 2]
                    address1 = df.iat[i, 3]
                    address2 = df.iat[i, 4]
                    address3 = df.iat[i, 5]
                    customer = df.iat[i, 6]
                    customer = Customer.objects.get(pk=customer)
                    address_data = CustomerAddressData.objects.create(customer=customer,pincode=pincode,landmark=landmark,address1=address1,address2=address2,address3=address3)
                    address_data.save()
            elif file.table == 'CUSTOMER_OFFICE':
                for i in range(0,count):
                    pincode = df.iat[i, 1]
                    landmark = df.iat[i, 2]
                    address1 = df.iat[i, 3]
                    address2 = df.iat[i, 4]
                    address3 = df.iat[i, 5]
                    customer = df.iat[i, 6]
                    customer = Customer.objects.get(pk=customer)
                    address_data = CustomerOfficeData.objects.create(customer=customer,pincode=pincode,landmark=landmark,address1=address1,address2=address2,address3=address3)
                    address_data.save()
            elif file.table == 'LOAN_AMOUNT':
                for i in range(0,count):
                    agreementDate = df.iat[i, 1]
                    LRN = df.iat[i, 2]
                    tenor = df.iat[i, 3]
                    advEMI = df.iat[i, 4]
                    mob = df.iat[i, 5]
                    customer = df.iat[i, 6]
                    customer = Customer.objects.get(pk=customer)
                    loan_data = LoanAmountData.objects.create(customer=customer,agreementDate=agreementDate,LRN=LRN,tenor=tenor,advEMI=advEMI,mob=mob)
                    loan_data.save()
            elif file.table == 'BRANCH_DATA':
                for i in range(0,count):
                    zoneName = df.iat[i, 1]
                    regionName = df.iat[i, 2]
                    areaName = df.iat[i, 3]
                    branchName = df.iat[i, 4]
                    branchCode = df.iat[i, 5]
                    branch_data = BranchData.objects.create(zoneName=zoneName,regionName=regionName,areaName=areaName,branchName=branchName,branchCode=branchCode)
                    branch_data.save()
        except Exception as e:
            print(e)
        file.updated = True
        file.save()

# Customer Data
class ExportImportCustomer(APIView):
    
    def get(self,request):
        add_to_database()
        customer = Customer.objects.all()
        serializer = CustomerSerializer(customer, many=True)
        df = pd.DataFrame(serializer.data)
        print(df)
        df.to_excel(f"public/static/excel/customer{uuid.uuid4()}.xlsx", encoding="UTF-8",index=False)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def post(self,request):
        add_to_database()
        excel_upload = ExcelFileUpload.objects.create(file=request.FILES['file'])
        df = pd.read_excel(f"{settings.BASE_DIR}/{excel_upload.file}") 
        count = df.shape[0]
        for i in range(0,count):
            customerName = df.iat[i, 1]
            fatherName = df.iat[i, 2]
            phoneNumber = df.iat[i, 3]
            dob = df.iat[i, 4]
            loanAccountNumber = df.iat[i, 5]
            customer = Customer.objects.create(customerName=customerName,fatherName=fatherName,phoneNumber=phoneNumber,dob=dob,loanAccountNumber=loanAccountNumber)
            customer.save()
        branch_data = Customer.objects.all()
        serializer = CustomerSerializer(branch_data, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# Branch Data
class ExportImportBranchData(APIView):

    def get(self, request, format=None):
        add_to_database()
        branch_data = BranchData.objects.all()
        serializer = BranchDataSerializer(branch_data, many=True)
        df = pd.DataFrame(serializer.data)
        df.to_excel(f"public/static/excel/branch_data{uuid.uuid4()}.xlsx", encoding="UTF-8",index=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        excel_upload = ExcelFileUpload.objects.create(file=request.FILES['file'])
        df = pd.read_excel(f"{settings.BASE_DIR}/{excel_upload.file}") 
        count = df.shape[0]
        for i in range(0,count):
            zoneName = df.iat[i, 1]
            regionName = df.iat[i, 2]
            areaName = df.iat[i, 3]
            branchName = df.iat[i, 4]
            branchCode = df.iat[i, 5]
            branch_data = BranchData.objects.create(zoneName=zoneName,regionName=regionName,areaName=areaName,branchName=branchName,branchCode=branchCode)
            branch_data.save()
        branch_data =  BranchData.objects.all() 
        serializer = BranchDataSerializer(branch_data, many=True)       
        return Response(serializer.data, status=status.HTTP_201_CREATED)



# Customer Address Data
class ExportImportCustomerAddressData(APIView):

    def get(self, request):
        add_to_database()
        customer_address_data = CustomerAddressData.objects.all()
        serializer = CustomerAddressDataSerializer(customer_address_data, many=True)
        df = pd.DataFrame(serializer.data)
        df.to_excel(f"public/static/excel/customer_address_data{uuid.uuid4()}.xlsx", encoding="UTF-8",index=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        add_to_database()
        excel_upload = ExcelFileUpload.objects.create(file=request.FILES['file'])
        df = pd.read_excel(f"{settings.BASE_DIR}/{excel_upload.file}") 
        count = df.shape[0]
        for i in range(0,count):
            pincode = df.iat[i, 1]
            landmark = df.iat[i, 2]
            address1 = df.iat[i, 3]
            address2 = df.iat[i, 4]
            address3 = df.iat[i, 5]
            customer = df.iat[i, 6]
            customer = Customer.objects.get(pk=customer)
            address_data = CustomerAddressData.objects.create(customer=customer,pincode=pincode,landmark=landmark,address1=address1,address2=address2,address3=address3)
            address_data.save()
        address_data =  CustomerAddressData.objects.all() 
        serializer = CustomerAddressDataSerializer(address_data, many=True)       
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# Customer Office Address Data
class ExportImportCustomerOfficeData(APIView):

    def get(self, request):
        add_to_database()
        office_address_data = CustomerOfficeData.objects.all()
        serializer = CustomerOfficeDataSerializer(office_address_data, many=True)
        df = pd.DataFrame(serializer.data)
        df.to_excel(f"public/static/excel/customer_office_data{uuid.uuid4()}.xlsx", encoding="UTF-8",index=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        add_to_database()
        excel_upload = ExcelFileUpload.objects.create(file=request.FILES['file'])
        df = pd.read_excel(f"{settings.BASE_DIR}/{excel_upload.file}") 
        count = df.shape[0]
        for i in range(0,count):
            pincode = df.iat[i, 1]
            landmark = df.iat[i, 2]
            address1 = df.iat[i, 3]
            address2 = df.iat[i, 4]
            address3 = df.iat[i, 5]
            customer = df.iat[i, 6]
            customer = Customer.objects.get(pk=customer)
            address_data = CustomerOfficeData.objects.create(customer=customer,pincode=pincode,landmark=landmark,address1=address1,address2=address2,address3=address3)
            address_data.save()
        address_data =  CustomerOfficeData.objects.all() 
        serializer = CustomerOfficeDataSerializer(address_data, many=True)       
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# Loan Amount Data
class ExportImportLoanAmountData(APIView):

    def get(self, request):
        add_to_database()
        customer_address_data = LoanAmountData.objects.all()
        serializer = LoanAmountDataSerializer(customer_address_data, many=True)
        df = pd.DataFrame(serializer.data)
        df.to_excel(f"public/static/excel/loan_amount_data{uuid.uuid4()}.xlsx", encoding="UTF-8",index=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        add_to_database()
        excel_upload = ExcelFileUpload.objects.create(file=request.FILES['file'])
        df = pd.read_excel(f"{settings.BASE_DIR}/{excel_upload.file}") 
        count = df.shape[0]
        for i in range(0,count):
            agreementDate = df.iat[i, 1]
            LRN = df.iat[i, 2]
            tenor = df.iat[i, 3]
            advEMI = df.iat[i, 4]
            mob = df.iat[i, 5]
            customer = df.iat[i, 6]
            customer = Customer.objects.get(pk=customer)
            loan_data = LoanAmountData.objects.create(customer=customer,agreementDate=agreementDate,LRN=LRN,tenor=tenor,advEMI=advEMI,mob=mob)
            loan_data.save()
        loan_data =  LoanAmountData.objects.all()  
        serializer = LoanAmountDataSerializer(loan_data, many=True)      
        return Response(serializer.data, status=status.HTTP_201_CREATED)



class ImportExcelFileUpload (viewsets.ModelViewSet):
    serializer_class = ExcelFileUploadSerializer
    queryset = ExcelFileUpload.objects.all()
    @csrf_exempt
    def dispatch(self, *args, **kwargs):
        return super(ImportExcelFileUpload, self).dispatch(*args, **kwargs)