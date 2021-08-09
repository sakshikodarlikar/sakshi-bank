from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework.routers import DefaultRouter
from django.views.decorators.csrf import csrf_exempt   

router = DefaultRouter()
router.register(r'',  views.ImportExcelFileUpload, basename='imort')


urlpatterns = [
    path('customer/', views.ExportImportCustomer.as_view(), name='customer'),
    path('branch/', views.ExportImportBranchData.as_view(), name='branch'),
    path('customeraddress/', views.ExportImportCustomerAddressData.as_view(), name='customeraddress'),
    path('customeroffice/', views.ExportImportCustomerOfficeData.as_view(), name='customeroffice'),
    path('loandata/', views.ExportImportLoanAmountData.as_view(), name='loandata'),
    path('', include(router.urls) , name='import'),
    ]