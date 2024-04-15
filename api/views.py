from django.shortcuts import render
from rest_framework import viewsets
from api.models import Company, Employees
from api.serializers import CompanySerializers, EmployeeSerializers
from rest_framework.decorators import action
from rest_framework.response import Response

# The structure of Django REST Framework (DRF) follows the Model-View-Controller (MVC) architectural pattern, similar to Django itself. However, in DRF, the "Controller" part is often represented by "Views", which handle incoming HTTP requests, process data, and return HTTP responses. Here's a breakdown of the typical structure of a Django REST Framework application:

# Views: Views are responsible for processing incoming HTTP requests and returning HTTP responses. In DRF, views are often implemented as viewsets or generic views, which provide high-level abstractions for common CRUD (Create, Read, Update, Delete) operations on resources. Views handle tasks such as data validation, authentication, authorization, and pagination. They are defined in views.py files within Django apps.


# Create your views here.
class CompanyViewset(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializers

    # companies/{companies/id}/employees
    @action(detail=True, methods=["get"])
    def employees(self, request, pk=None):
        try:
            company = Company.objects.get(pk=pk)
            emps = Employees.objects.filter(company=company)
            emps_serializer = EmployeeSerializers(emps, many=True, context={"request": request})
            return Response(emps_serializer.data)
        except Exception as e:
            print(e)
            return Response({"messsage": "Company might not exists!!"})


class EmployeesViewset(viewsets.ModelViewSet):
    queryset = Employees.objects.all()
    serializer_class = EmployeeSerializers
