from django.db import models
import numpy


class ReserveInLack(models.Model):

    value_0_to_24_mounth = models.PositiveSmallIntegerField()

    value_24_to_60_mounth = models.PositiveSmallIntegerField()

    value_60_to_120_mounth = models.PositiveSmallIntegerField()

    value_120_to_240_mounth = models.PositiveSmallIntegerField()

    def patrimony_necessery_in_period(self, mounth_quantities, value):
        rate = self.protection_manager.financial_planning.real_gain()
        return numpy.pv(rate, mounth_quantities, -value)

    def patrimony_necessery_total(self):
        portion_0_to_24_mounth = self.patrimony_necessery_in_period(
            24, self.value_0_to_24_mounth)
        portion_24_to_60_mounth = self.patrimony_necessery_in_period(
            36, self.value_24_to_60_mounth)
        portion_60_to_120_mounth = self.patrimony_necessery_in_period(
            60, self.value_60_to_120_mounth)
        portion_120_to_240_mounth = self.patrimony_necessery_in_period(
            120, self.value_120_to_240_mounth)

        total = portion_0_to_24_mounth + portion_24_to_60_mounth +\
            portion_60_to_120_mounth + portion_120_to_240_mounth

        return total


class EmergencyReserve(models.Model):

    mounth_of_protection = models.PositiveSmallIntegerField()

    def necessery_value(self):
        regular_cost_mounthly = self.protection_manager.financial_planning.\
            cost_manager.total()
        total = self.mounth_of_protection * regular_cost_mounthly

        return total

    def risk_gap(self):
        current_patrimony = self.protection_manager.financial_planning.\
            patrimony.current_net_investment()
        necessery_value = self.necessery_value()
        if current_patrimony < necessery_value:
            total = necessery_value - current_patrimony
        else:
            total = 0

        return total


class ProtectionManager(models.Model):

    reserve_in_lack = models.OneToOneField(
        ReserveInLack,
        on_delete=models.CASCADE,
        related_name='protection_manager',
    )

    emergency_reserve = models.OneToOneField(
        EmergencyReserve,
        on_delete=models.CASCADE,
        related_name='protection_manager',
    )
