from rest_framework import viewsets
from rest_framework.decorators import detail_route

from rolepermissions.mixins import HasPermissionsMixin
from employee.serializers import (
    EmployeeSerializer,
    FinancialAdviserSerializer,
)
from employee.models import (
    Employee,
    FinancialAdviser,
)


class EmployeeViewSet(HasPermissionsMixin, viewsets.ModelViewSet):
    required_permission = 'create_employee'

    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()

    @detail_route
    def a(self, request, *args, **kwargs):
        print(request.user)


class FinancialAdviserViewSet(HasPermissionsMixin, viewsets.ModelViewSet):
    required_permission = 'create_employee'

    serializer_class = FinancialAdviserSerializer
    queryset = FinancialAdviser.objects.all()

    @detail_route(methods=['get'])
    def a(self, request, pk=None, *args, **kwargs):
        print(request.user)
        return None
