from django.contrib import admin
from django.urls import path,include
from api.views import CompanyViewset, EmployeesViewset
from rest_framework import routers

# URLs: URL routing determines how incoming HTTP requests are mapped to view functions or viewsets. In DRF, URL routing is typically configured using Django's URL patterns (urls.py files). URLs define the endpoints of the API and specify which views or viewsets should handle requests to those endpoints.


# Routers: Routers are optional components in DRF that simplify the process of URL routing for viewsets. Routers automatically generate URL patterns for CRUD operations based on the viewsets provided. They are defined in routers.py files within Django apps and are registered in the project's URL configuration.

router = routers.DefaultRouter()
router.register(r'companies', CompanyViewset)
router.register(r'employees', EmployeesViewset)
urlpatterns = [
   path('',include(router.urls)),
  
]






# http://localhost:8000/api/v1/companies/
# http://127.0.0.1:8000/api/v1/employees/