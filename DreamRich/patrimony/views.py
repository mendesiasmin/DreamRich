from rest_framework import viewsets
from rolepermissions.mixins import HasPermissionsMixin

from patrimony.serializers import (
    PatrimonySerializer,
    ActiveSerializer,
    ArrearageSerializer,
    RealEstateSerializer,
    CompanyParticipationSerializer,
    EquipmentSerializer,
    LifeInsuranceSerializer,
    IncomeSerializer,
    RegularCostSerializer,

)

from patrimony.models import (
    Patrimony,
    Active,
    Arrearage,
    RealEstate,
    CompanyParticipation,
    Equipment,
    LifeInsurance,
    Income,
    RegularCost,
)


class PatrimonyClientViewSet(HasPermissionsMixin,
                             viewsets.ReadOnlyModelViewSet):
    required_permission = 'see_client_complete_data'
    serializer_class = PatrimonySerializer
    queryset = Patrimony.objects.all()


class ActiveClientViewSet(HasPermissionsMixin, viewsets.ReadOnlyModelViewSet):
    required_permission = 'see_client_complete_data'
    serializer_class = ActiveSerializer
    queryset = Active.objects.all()


class ArrearageClientViewSet(HasPermissionsMixin,
                             viewsets.ReadOnlyModelViewSet):
    required_permission = 'see_client_complete_data'
    serializer_class = ArrearageSerializer
    queryset = Arrearage.objects.all()


class RealEstateClientViewSet(HasPermissionsMixin,
                              viewsets.ReadOnlyModelViewSet):
    required_permission = 'see_client_complete_data'
    serializer_class = RealEstateSerializer
    queryset = RealEstate.objects.all()


class CompanyParticipationClientViewSet(
        HasPermissionsMixin, viewsets.ReadOnlyModelViewSet):
    required_permission = 'see_client_complete_data'
    serializer_class = CompanyParticipationSerializer
    queryset = CompanyParticipation.objects.all()


class EquipmentClientViewSet(HasPermissionsMixin,
                             viewsets.ReadOnlyModelViewSet):
    required_permission = 'see_client_complete_data'
    serializer_class = EquipmentSerializer
    queryset = Equipment.objects.all()


class LifeInsuranceClientViewSet(
        HasPermissionsMixin, viewsets.ReadOnlyModelViewSet):
    required_permission = 'see_client_complete_data'
    serializer_class = LifeInsuranceSerializer
    queryset = LifeInsurance.objects.all()


class IncomeClientViewSet(HasPermissionsMixin, viewsets.ReadOnlyModelViewSet):
    required_permission = 'see_client_complete_data'
    serializer_class = IncomeSerializer
    queryset = Income.objects.all()


class RegularCostClientViewSet(
        HasPermissionsMixin, viewsets.ReadOnlyModelViewSet):
    required_permission = 'see_client_complete_data'
    serializer_class = RegularCostSerializer
    queryset = RegularCost.objects.all()


class PatrimonyFAViewSet(HasPermissionsMixin, viewsets.ModelViewSet):
    required_permission = 'see_client_complete_data'
    serializer_class = PatrimonySerializer
    queryset = Patrimony.objects.all()


class ActiveFAViewSet(HasPermissionsMixin, viewsets.ModelViewSet):
    required_permission = 'see_client_complete_data'
    serializer_class = ActiveSerializer
    queryset = Active.objects.all()


class ArrearageFAViewSet(HasPermissionsMixin, viewsets.ModelViewSet):
    required_permission = 'see_client_complete_data'
    serializer_class = ArrearageSerializer
    queryset = Arrearage.objects.all()


class RealEstateFAViewSet(HasPermissionsMixin, viewsets.ModelViewSet):
    required_permission = 'see_client_complete_data'
    serializer_class = RealEstateSerializer
    queryset = RealEstate.objects.all()


class CompanyParticipationFAViewSet(
        HasPermissionsMixin, viewsets.ModelViewSet):
    required_permission = 'see_client_complete_data'
    serializer_class = CompanyParticipationSerializer
    queryset = CompanyParticipation.objects.all()


class EquipmentFAViewSet(HasPermissionsMixin, viewsets.ModelViewSet):
    required_permission = 'see_client_complete_data'
    serializer_class = EquipmentSerializer
    queryset = Equipment.objects.all()


class LifeInsuranceFAViewSet(HasPermissionsMixin, viewsets.ModelViewSet):
    required_permission = 'see_client_complete_data'
    serializer_class = LifeInsuranceSerializer
    queryset = LifeInsurance.objects.all()


class IncomeFAViewSet(HasPermissionsMixin, viewsets.ModelViewSet):
    required_permission = 'see_client_complete_data'
    serializer_class = IncomeSerializer
    queryset = Income.objects.all()


class RegularCostFAViewSet(HasPermissionsMixin, viewsets.ModelViewSet):
    required_permission = 'see_client_complete_data'
    serializer_class = RegularCostSerializer
    queryset = RegularCost.objects.all()
