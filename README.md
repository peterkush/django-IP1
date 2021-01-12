# django-IP1
This is an Independent project for Moringa Core Django module, Jan 8 2021.

## Author
peter kungu

### Description
Is a photo gallery web application to showcase beautiful pictures. Users get can view photos uploaded by admin. Users can see photos based on the location, by clicking on the listed locations in the menu. They can also copy the link to a photo to paste at their discretion. They can also search for photos based on the categories.

### features
~ The home page allows users to see various images
~ User can see all images per location they were taken
~ Users can also search for images based categories
~ Admin can upload images from a django dashboard

### Deployed link



##### Cloning the repository:


#### Install and activate Virtual
 ```bash 
-  - source virtual/bin/activate  
```  

##### Navigate into the folder and install requirements  
 ```bash 
cd gallery pipenv  install -r requirements.txt 
#### Install Dependencies  
 ```bash 
 pipenv install -r requirements.txt 
```  
##### Setup Database  
  SetUp your database User,Password, Host then make migrate  
 ```bash 
python manage.py makemigrations gallery
 ``` 
 Now Migrate  
 ```bash 
 python manage.py migrate 

### run app
 ```bash 
 python manage.py runserver 
```  
##### Testing the application 
 ```bash 
 python manage.py test 
```
Open the application on your browser `127.0.0.1:8000`.  

## Technology used  
  
* [Python3.6](https://www.python.org/)  
* [Django 3.0.](https://docs.djangoproject.com/en/3.0/) 
* [Heroku](https://heroku.com)  
* [Git](for version control)

## License

- Licensed under[MIT license](license).