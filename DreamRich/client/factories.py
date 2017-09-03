import datetime
import factory.fuzzy
from client.validators import validate_CPF
from django.contrib.auth.models import User
from faker import Factory
from . import models


class UserFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = User

    username = factory.Faker('word')
    password = factory.PostGenerationMethodCall('set_password',
                                                'default123')
    email = factory.LazyAttribute(lambda x: '{}@mail.com'.format(x.username))
    is_staff = True
    is_superuser = True


fake = Factory.create('pt_BR')


def gen_cpf(factory):
    cpf = ""
    while cpf == "":
        try:
            cpf = validate_CPF(fake.cpf())
        except:
            pass
    return cpf


class CountryFactory(factory.DjangoModelFactory):

    class Meta:
        model = models.Country

    name = factory.Sequence(lambda n: 'country%s' % n)


class StateFactory(factory.DjangoModelFactory):

    class Meta:
        model = models.State

    name = factory.Sequence(lambda n: 'state%s' % n)
    country = factory.SubFactory(CountryFactory)


class AddressFactory(factory.DjangoModelFactory):

    class Meta:
        model = models.Address

    city = factory.Faker('word')
    type_of_address = factory.Sequence(lambda n: 'type%s' % n)
    neighborhood = factory.Sequence(lambda n: 'neighborhood%s' % n)
    detail = factory.Sequence(lambda n: 'detail%s' % n)
    state = factory.SubFactory(StateFactory)
    number = 1
    complement = factory.Sequence(lambda n: 'complement%s' % n)


class ClientFactory(factory.DjangoModelFactory):

    class Meta:
        model = models.Client

    name = factory.Faker('name')
    surname = factory.Faker('name')
    birthday = factory.LazyFunction(datetime.datetime.now)
    profession = factory.Sequence(lambda n: 'profession%s' % n)
    telephone = factory.Sequence(lambda n: 'tel%s' % n)
    email = factory.Sequence(lambda n: '%s@gmail.com' % n)
    hometown = factory.Faker('word')
    cpf = factory.LazyAttribute(gen_cpf)

    @factory.post_generation
    def addresses(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of groups were passed in, use them
            for address in extracted:
                self.addresses.add(address)


class DependentFactory(factory.DjangoModelFactory):

    class Meta:
        model = models.Dependent

    name = factory.Faker('name')
    surname = factory.Faker('name')
    birthday = factory.LazyFunction(datetime.datetime.now)


class BankAccountFactory(factory.DjangoModelFactory):

    class Meta:
        model = models.BankAccount

    agency = factory.Sequence(lambda n: '%s' % n)
    account = factory.Sequence(lambda n: '%s' % n)


class ActiveClientMainFactory(ClientFactory):

    class Meta:
        model = models.ActiveClient

    id_document = factory.django.ImageField(color='green')
    address = factory.RelatedFactory(AddressFactory, 'client')
    proof_of_address = factory.django.ImageField(color='blue')
    bank_account = factory.RelatedFactory(BankAccountFactory,
                                                 'active_client')
    spouse = factory.RelatedFactory(ClientFactory, 'active_spouse')
    dependent = factory.RelatedFactory(DependentFactory, "active_client")
