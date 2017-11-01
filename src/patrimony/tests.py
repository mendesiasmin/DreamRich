import datetime
from django.test import TestCase
from client.factories import ActiveClientMainFactory
from financial_planning.models import FlowUnitChange
from financial_planning.factories import FinancialPlanningFactory
from patrimony.models import Active
from patrimony.factories import (
    PatrimonyMainFactory,
    IncomeFactory,
    ActiveManagerFactory,
    ActiveFactory,
    ArrearageFactory
)


def _flatten(array):
    def inner(array):
        for item in array:
            if isinstance(item, (list, tuple)):
                for inner_item in inner(item):
                    yield inner_item
            else:
                yield item

    return list(inner(array))


class PatrimonyTest(TestCase):

    def setUp(self):
        active_client = ActiveClientMainFactory(
            birthday=datetime.datetime(1967, 1, 1))
        self.patrimony = PatrimonyMainFactory()
        self.patrimony.income_set.all().update(value_monthly=1212.2)
        FinancialPlanningFactory(
            active_client=active_client,
            patrimony=self.patrimony)
        self.common_income = IncomeFactory(value_monthly=round(1200, 2),
                                           thirteenth=False,
                                           patrimony=self.patrimony,
                                           vacation=False)
        self.income_with_thirteenth = IncomeFactory(value_monthly=1200.00,
                                                    thirteenth=True,
                                                    patrimony=self.patrimony,
                                                    vacation=False)
        self.income_with_vacation = IncomeFactory(value_monthly=round(1200, 2),
                                                  thirteenth=False,
                                                  patrimony=self.patrimony,
                                                  vacation=True)

    def test_current_net_investment(self):
        ArrearageFactory(patrimony=self.patrimony, value=351200.00, period=3)
        self.assertEqual(321200.00, self.patrimony.current_net_investment())

    def test_current_property_investment(self):
        self.assertEqual(121.21, self.patrimony.current_property_investment())

    def test_current_income_generation(self):
        self.assertEqual(1345.6100000000001,
                         self.patrimony.possible_income_generation())

    def test_annual_income(self):
        self.assertEqual(self.common_income.annual(), 14400.00)

    def test_annual_income_with_thirteen(self):
        self.assertEqual(self.income_with_thirteenth.annual(), 15600.00)

    def test_annual_income_with_vacation(self):
        self.assertEqual(self.income_with_vacation.annual(), 14800.00)

    def test_current_monthly_income(self):
        self.assertEqual(60962.67, self.patrimony.total_annual_income())

    def test_income_flow(self):
        FlowUnitChange.objects.create(annual_value=500.00, year=2021,
                                      incomes=self.patrimony)
        FlowUnitChange.objects.create(annual_value=-500.00, year=2022,
                                      incomes=self.patrimony)

        flow_regular_cost_with_change = [60962.67, 60962.67, 60962.67,
                                         60962.67, 61462.67, 60962.67,
                                         60962.67, 60962.67, 60962.67,
                                         60962.67]

        self.assertEqual(flow_regular_cost_with_change,
                         self.patrimony.income_flow())


class ActiveManagerTest(TestCase):
    def setUp(self):
        self.active_manager = ActiveManagerFactory(
            patrimony=PatrimonyMainFactory(activemanager=None)
        )

        for active in self.active_manager.actives.all():
            active.delete()

        data = [{'value': 27000.00, 'rate': 1.1879},
                {'value': 125000.00, 'rate': 0.7500},
                {'value': 95000.00, 'rate': 0.9000}]

        for active in data:
            ActiveFactory(**active, active_manager=self.active_manager)

        self.active_manager.real_profit_cdi()

    def test_total_manager(self):
        self.assertAlmostEqual(self.active_manager.total(), 247000, 2)

    # Use real_profit because update_equivalent_rate is internal
    def test_update_equivalent_rates(self):
        equivalents = self.active_manager.actives.values_list(
            'equivalent_rate')
        self.active_manager.CDI = 0.12
        self.active_manager.real_profit_cdi()
        new_equivalents = self.active_manager.actives.values_list(
            'equivalent_rate'
        )

        self.assertNotEqual(equivalents, new_equivalents)

    def test_update_rates_values(self):
        equivalents = [(0.0156,), (0.0455,), (0.0415, )]
        self.active_manager.CDI = 0.12
        self.active_manager.real_profit_cdi()
        new = self.active_manager.actives.values_list('equivalent_rate')

        for values in zip(_flatten(equivalents), _flatten(new)):
            self.assertAlmostEqual(values[0], values[1], 4)

    def test_real_profit_cdi(self):
        self.assertAlmostEqual(
            self.active_manager.real_profit_cdi(), 0.8556, 4)

    def test_real_profit_cdi_zero(self):
        self.active_manager.CDI = 0
        self.assertAlmostEqual(self.active_manager.real_profit_cdi(), 0, 4)


class ActiveTest(TestCase):

    def setUp(self):
        self.active = PatrimonyMainFactory().activemanager.actives.first()
        self.active.value = 100
        self.active.rate = 1.10
        self.active.save()

    def test_update_equivalent_rate(self):
        last_rate = self.active.equivalent_rate
        self.active.update_equivalent_rate(1000, 0.12)
        new_rate = Active.objects.get(pk=self.active.pk).equivalent_rate
        self.assertNotEqual(new_rate, last_rate)

    def test_not_update_rate(self):
        self.active.update_equivalent_rate(1000, 0.12)
        last_rate = Active.objects.get(pk=self.active.pk).equivalent_rate
        self.active.update_equivalent_rate(1000, 0.1201)
        new_rate = Active.objects.get(pk=self.active.pk).equivalent_rate
        self.assertAlmostEqual(new_rate, last_rate, 15)
