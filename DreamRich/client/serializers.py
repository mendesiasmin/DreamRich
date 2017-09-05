from rest_framework import serializers
from client.models import (
    Address,
    Client,
    ActiveClient,
    BankAccount,
    State,
    Country,
    Dependent
)


class AddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = Address
        fields = [
            'city',
            'type_of_address',
            'neighborhood',
            'detail',
            'cep',
            'number',
            'complement'
        ]


class StateSerializer(serializers.ModelSerializer):

    class Meta:
        model = State
        fields = [
            'name',
            'abbreviation'
        ]


class CountrySerializer(serializers.ModelSerializer):
    country_states = StateSerializer(many=True, read_only=True)

    class Meta:
        model = Country
        fields = [
            'name',
            'abbreviation',
            'country_states'
        ]


class DependentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dependent
        fields = [
            'name',
            'surname',
            'active_client',
            'birthday'
        ]


class BankAccountSerializer(serializers.ModelSerializer):
    active_client_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = BankAccount
        fields = [
            'agency',
            'account',
            'active_client_id'
        ]


class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = [
            'name',
            'surname',
            'birthday',
            'profession',
            'cpf',
            'telephone',
            'email',
            'hometown',
            'id'
        ]


class ActiveClientSerializer(serializers.ModelSerializer):
    dependents = DependentSerializer(many=True, read_only=True)
    address = AddressSerializer(many=True, read_only=True)
    spouse = ClientSerializer(read_only=True)
    bank_account = BankAccountSerializer(read_only=True)

    id_document = serializers.ImageField(read_only=True)
    proof_of_address = serializers.ImageField(read_only=True)

    class Meta:

        model = ActiveClient
        fields = ClientSerializer.Meta.fields + [
            'address',
            'dependents',
            'id_document',
            'proof_of_address',
            'bank_account',
            'spouse',
            'id'
        ]
