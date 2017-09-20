from rest_framework import routers
from patrimony.views import (
    ActiveClientViewSet,
    ArrearageClientViewSet,
    RealEstateClientViewSet,
    CompanyParticipationClientViewSet,
    EquipmentClientViewSet,
    LifeInsuranceClientViewSet,
    IncomeClientViewSet,
    RegularCostClientViewSet,
    PatrimonyClientViewSet,
    ActiveFAViewSet,
    ArrearageFAViewSet,
    RealEstateFAViewSet,
    CompanyParticipationFAViewSet,
    EquipmentFAViewSet,
    LifeInsuranceFAViewSet,
    IncomeFAViewSet,
    RegularCostFAViewSet,
    PatrimonyFAViewSet,
)

app_name = 'patrimony'

router = routers.DefaultRouter()

# Routes for Clients and Common Employee
router.register('active', ActiveClientViewSet)
router.register('arrearage', ArrearageClientViewSet)
router.register('realestate', RealEstateClientViewSet)
router.register('companyparticipation', CompanyParticipationClientViewSet)
router.register('equipment', EquipmentClientViewSet)
router.register('lifeinsurance', LifeInsuranceClientViewSet)
router.register('income', IncomeClientViewSet)
router.register('regularcost', RegularCostClientViewSet)
router.register('', PatrimonyClientViewSet)

# Routes for Financial Adviser
router.register('faactive', ActiveFAViewSet)
router.register('faarrearage', ArrearageFAViewSet)
router.register('farealestate', RealEstateFAViewSet)
router.register('facompanyparticipation', CompanyParticipationFAViewSet)
router.register('faequipment', EquipmentFAViewSet)
router.register('falifeinsurance', LifeInsuranceFAViewSet)
router.register('faincome', IncomeFAViewSet)
router.register('faregularcost', RegularCostFAViewSet)
router.register('fa', PatrimonyFAViewSet)

urlpatterns = router.urls
