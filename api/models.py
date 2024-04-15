from django.db import models

# Models: Models represent the structure and behavior of data in the application. They are typically defined in models.py files within Django apps and use Django's built-in ORM (Object-Relational Mapping) to interact with the database. Models define the data schema, relationships between data entities, and any business logic associated with the data.

# Create your models here.
class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    about = models.TextField()
    type = models.CharField(max_length=100,choices=(
            ("IT", "IT"),
            ("Non IT", "Non IT"),
            ("Mobiles Phones", "Mobiles Phones"),
        ),
    )
    added_date = models.DateField(auto_now=True)
    active = models.BooleanField(default=True)
    
    def __str__(self) :
        return self.name +'--'+self.location
        

# Employee Model
class Employees(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=10)
    about = models.TextField()
    position = models.CharField(max_length=50,choices=(
            ("Manager", "manager"),
            ("Software developer", "sd"),
            ("Project Leader", "pl"),
        ))
    company = models.ForeignKey(Company, on_delete=models.CASCADE, default=1)
