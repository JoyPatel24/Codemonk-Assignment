from rest_framework import serializers
from DjangoAPI.EmployeeApp.models import User
from EmployeeApp.models import Departments,Employees

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields=('UserId','UserName','EmployeeId','DateOfJoining','createdAt','modifiedAt')