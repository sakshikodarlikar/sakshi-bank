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


## Link to upload the excel file

```https://sakshi-bank.herokuapp.com/```  - choose a excel file for particular table and choose that table. These appends the data in the sqlite database.

## Link for tables

```https://sakshi-bank.herokuapp.com/customer/``` - Customer Table

```https://sakshi-bank.herokuapp.com/branch/``` - Branch Data Table

```https://sakshi-bank.herokuapp.com/customeraddress/``` - Customer Home Address Data Table

```https://sakshi-bank.herokuapp.com/customeroffice/``` - Customer Office Data Table

```https://sakshi-bank.herokuapp.com/loandata/``` - Loan Amount Data Table

