# sakshi-bank


Code Deployed on Heroku - https://sakshi-bank.herokuapp.com/


=======================================================================================

1. Create tables for each data set

2. Create an excel file with all above columns.

3. Create an api which accepts excel file and saves data in all respective columns.

4. Customer table primary key will be foriegn key in other tables.

5. Show all data after uploading on screen with respective tables.

=======================================================================================

All the above objectives completed.



## How to Use and Test this Application on your computer
- run ```pip install -r requirements.txt```  in your shell to install the specified packages with the specified version.
- run the app ```python manage.py runserver```



## Link for tables

```https://sakshi-bank.herokuapp.com/customer/``` - Customer Table

```https://sakshi-bank.herokuapp.com/branch/``` - Branch Data Table

```https://sakshi-bank.herokuapp.com/customeraddress/``` - Customer Home Address Data Table

```https://sakshi-bank.herokuapp.com/customeroffice/``` - Customer Office Data Table

```https://sakshi-bank.herokuapp.com/loandata/``` - Loan Amount Data Table


## How to test API's

### Method 1:

1. Go to route ```https://sakshi-bank.herokuapp.com/``` and post the following customer excel sheet -> https://github.com/sakshikodarlikar/sakshi-bank/raw/main/Tables%20file/customer2.xlsx and select CUSTOMER option and check the customers added at ```https://sakshi-bank.herokuapp.com/customer/```

2. Go to route ```https://sakshi-bank.herokuapp.com/``` and post the following Branch Data excel sheet -> https://github.com/sakshikodarlikar/sakshi-bank/raw/main/Tables%20file/branch_data2.xlsx and select BRANCH_DATA option and check the Branch Data added at ```https://sakshi-bank.herokuapp.com/branch/```

3. Go to route ```https://sakshi-bank.herokuapp.com/``` and post the following Customer Home Address Data excel sheet -> https://github.com/sakshikodarlikar/sakshi-bank/raw/main/Tables%20file/customer_address_data%202.xlsx and select CUSTOMER_ADDRESS option and check the Customer Home Address Data added at ```https://sakshi-bank.herokuapp.com/customeraddress/```

4. Go to route ```https://sakshi-bank.herokuapp.com/``` and post the following Customer Office Data excel sheet -> https://github.com/sakshikodarlikar/sakshi-bank/raw/main/Tables%20file/customer_office_data%202.xlsx and select CUSTOMER_OFFICE option and check the Customer Office Data added at ```https://sakshi-bank.herokuapp.com/customeroffice/```

5. Go to route ```https://sakshi-bank.herokuapp.com/``` and post the following Loan Amount Data excel sheet -> https://github.com/sakshikodarlikar/sakshi-bank/raw/main/Tables%20file/loan_amount_data%202.xlsx and select LOAN_AMOUNT option and check the Loan Amount Data added at ```https://sakshi-bank.herokuapp.com/loandata/```


### Method 2: Using POSTMAN

1. Open Postman 

2. Post following link - ```https://sakshi-bank.herokuapp.com/customer/``` in the body section select 'form data' option. Write 'file' as key value,select file option from the dropdown and the choose https://github.com/sakshikodarlikar/sakshi-bank/raw/main/Tables%20file/customer2.xlsx file to upload and the send.

3. Post following link - ```https://sakshi-bank.herokuapp.com/branch/``` in the body section select 'form data' option. Write 'file' as key value,select file option from the dropdown and the choose https://github.com/sakshikodarlikar/sakshi-bank/raw/main/Tables%20file/branch_data2.xlsx file to upload and the send.


4. Post following link - ```https://sakshi-bank.herokuapp.com/customeraddress/``` in the body section select 'form data' option. Write 'file' as key value,select file option from the dropdown and the choose https://github.com/sakshikodarlikar/sakshi-bank/raw/main/Tables%20file/customer_address_data%202.xlsx file to upload and the send.


5. Post following link - ```https://sakshi-bank.herokuapp.com/customeroffice/``` in the body section select 'form data' option. Write 'file' as key value,select file option from the dropdown and the choose https://github.com/sakshikodarlikar/sakshi-bank/raw/main/Tables%20file/customer_office_data%202.xlsx file to upload and the send.


6. Post following link - ```https://sakshi-bank.herokuapp.com/loandata/``` in the body section select 'form data' option. Write 'file' as key value,select file option from the dropdown and the choose https://github.com/sakshikodarlikar/sakshi-bank/raw/main/Tables%20file/loan_amount_data%202.xlsx file to upload and the send.



## Link to upload the excel file

```https://sakshi-bank.herokuapp.com/```  - choose a excel file for particular table and select that table. These appends the data in the sqlite database.
