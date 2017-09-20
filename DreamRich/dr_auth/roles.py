from rolepermissions.roles import AbstractUserRole


class CommonEmployee(AbstractUserRole):
    available_permissions = {
        'see_client_basic_data': True,
        'change_client_data': False,
        'see_client_complete_data': False,
        'create_employee': False,
    }


class FinancialAdviser(AbstractUserRole):
    available_permissions = {
        'see_client_basic_data': True,
        'change_client_data': True,
        'see_client_complete_data': True,
        'create_employee': True,
    }


class Client(AbstractUserRole):
    available_permissions = {
        'see_client_basic_data': True,
        'change_client_data': False,
        'see_client_complete_data': True,
        'create_employee': False,
    }
