from rest_framework import viewsets
from rolepermissions.mixins import HasPermissionsMixin
from dr_auth.models import BaseUser
from dr_auth.permissions import SomePermission

from client.serializers import (
    ClientSerializer,
    ActiveClientSerializer,
    AddressSerializer,
    StateSerializer,
    CountrySerializer,
    BankAccountSerializer
)
from employee.models import FinancialAdviser
from client.models import (
    Client,
    ActiveClient,
    Address,
    State,
    Country,
    BankAccount
)
from rest_framework.decorators import detail_route


class ClientViewSet(viewsets.ModelViewSet):
    # required_permission = 'see_client_basic_data'
    serializer_class = ClientSerializer
    queryset = Client.objects.all()

class ActiveClientViewSet(viewsets.ModelViewSet):
    permission_classes = (SomePermission, )
    required_permission = 'create_employee'
    serializer_class = ActiveClientSerializer
    queryset = ActiveClient.objects.all()

    # def get_queryset(self):
    #     user = self.request.user
    #     print(user)
    #     base_user = BaseUser.objects.filter(username = user.username).first()
    #     print(base_user.permissions)

class AddressViewSet(viewsets.ModelViewSet):
    # required_permission = 'see_client_basic_data'
    serializer_class = AddressSerializer
    queryset = Address.objects.all()


class StateViewSet(viewsets.ModelViewSet):
    # required_permission = 'see_client_basic_data'
    serializer_class = StateSerializer
    queryset = State.objects.all()


class CountryViewSet(viewsets.ModelViewSet):
    # required_permission = 'see_client_basic_data'
    serializer_class = CountrySerializer
    queryset = Country.objects.all()


class BankAccountViewSet(viewsets.ModelViewSet):
    # required_permission = 'see_client_basic_data'
    serializer_class = BankAccountSerializer
    queryset = BankAccount.objects.all()
