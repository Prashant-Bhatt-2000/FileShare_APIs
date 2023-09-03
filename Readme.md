# Assignment EZ

## Installation 

    step1: clone repository
    step2 : python -m venv env
    stap3: source env/Scripts/activate
    step3 : run command "pip install -r requirements.txt
    step4: cd assignment
    step5: python manage.py makemigrations
    step6: python manage.py migrate
    step7: python manage.py runserver


## Gmail setup

    step 1: Go to Gmail
    step 2: Open Manage your google Accounts
    step 3: Go to security
    step 4: Go to 2-step verification
    step 5: Create App Password
    step 6: Choose Custom App
    step 7: Copy and save the password
    
    settings.py

    EMAIL_HOST_USER = 'Please use your own email'
    EMAIL_HOST_PASSWORD = 'Please Put your own email app generated Password'


## Database
    Note : I have used a localhost postgres so please make necessary changes


## All Apis with data format

    1. Ops Register

        Route : http://localhost:8000/api/accounts/opsregister/

        Data Format : 

        {
            "name": "Prashant",
            "email": "bhatt.prashant2018@gmail.com",
            "password": "password"
        }


    2. Ops login

        Route : http://localhost:8000/api/accounts/opsregister/

        Data Format: 

        {
            "email": "bhatt.prashant2018@gmail.com",
            "password": "password"
        }



    3. Client Register
       
       Route : http://localhost:8000/api/accounts/clientregister/

       Data Format : 

       {
            "name" : "Prashant2",
            "email": "bhatt.prashant2000@gmail.com",
            "password": "password"
       }


    4. File Upload (only Ops can upload file)
       
       Note: In this route you need an auth token which you will get from Ops login.

       Route : http://127.0.0.1:8000/api/files/upload/

       Note: Data should be in form 

       user =  user id
       title = title
       description = description
       file = select file


    5. Download File (Only Client Can download the Files)
       
        Note : You need an Client access token to download file

       Route : http://localhost:8000/api/files/downloadfile/file_id

       Note : Paste link in Browser to download the file



    6. List all Files (Only Client Can List the Files)

       Note : You need an Client access token to get list 

       Route : http://localhost:8000/api/files/getfiles/ 
    
# Note : For Account verification a link will be send to registered account once you click on that link your Account will be verified

## You will not be allowed to Perform any operation without verification


## For test cases 

    use command : python manage.py test


## For Deployment we can use Digital Ocean 
