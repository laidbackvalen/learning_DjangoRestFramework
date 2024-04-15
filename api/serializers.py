from rest_framework import serializers
from api.models import Company, Employees

# Serializers: Serializers are used to convert complex data types (such as model instances or querysets) into native Python datatypes that can be easily rendered into JSON, XML, or other content types. Serializers also handle deserialization, converting request data into valid Python objects. They are typically defined in serializers.py files within Django apps and are crucial for building RESTful APIs with DRF.

# Create Serializers here
class CompanySerializers(serializers.HyperlinkedModelSerializer):
    company_id = serializers.ReadOnlyField()
    class Meta:
        model = Company
        fields = "__all__"


class EmployeeSerializers(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = Employees
        fields = "__all__"
