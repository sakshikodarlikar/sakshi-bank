from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *
# Register your models here.

@admin.register(Customer)
class userdat(ImportExportModelAdmin):
    pass
@admin.register(BranchData)
class userdat(ImportExportModelAdmin):
    pass

@admin.register(CustomerAddressData)
class userdat(ImportExportModelAdmin):
    pass

@admin.register(CustomerOfficeData)
class userdat(ImportExportModelAdmin):
    pass

@admin.register(LoanAmountData)
class userdat(ImportExportModelAdmin):
    pass

@admin.register(ExcelFileUpload)
class userdat(ImportExportModelAdmin):
    pass

