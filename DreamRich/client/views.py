from json import dumps
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from client.serializers import (
    ClientSerializer,
    DependentSerializer,
    ActiveClientSerializer,
    AddressSerializer,
    StateSerializer,
    CountrySerializer,
    BankAccountSerializer
)
from client.models import (
    Client,
    Dependent,
    ActiveClient,
    Address,
    State,
    Country,
    BankAccount
)


class AuthView(APIView):

    def post(self, request):
        """Method to change the password value"""

        try:
            data = request.data
            user = User.objects.get(pk=data.get('userid'))

            if data.get('new_password') != data.get('new_password' +
                                                    '_confirmation'):

                return Response(
                    dumps({'detail': 'different password'}),
                    status=400
                )

            elif user.check_password(data.get('password')):
                user.set_password(data.get('new_password'))
                user.save()
                return Response(
                    dumps({'detail': 'password changed'}),
                    status=200
                )

            return Response(dumps({'detail': 'invalid password'}), status=400)

        except User.DoesNotExist:
            return Response(dumps({'detail': 'user not found'}), status=404)

    def get(self, request, email=None):
        """Reset password sending in e-mail"""

        user = User.objects.filter(email=request.GET.get('email'))

        if user.count() == 1 and user.first() is not None:
            user = user.first()

            random_password = User.objects.make_random_password()
            user.set_password(random_password)
            user.save()

            message = """Olá,\nSua senha foi resetada, acesse a plataforma
                         no link http://127.0.0.1/user/password e troque a
                         senha\nSua nova senha é:\n {}\nAtenciosamente,
                         \nEquipe Dream Rich.""".format(random_password)

            email = EmailMessage('Password reset',
                                 message, to=[user.email])
            email.send()

            return Response(dumps({'detail': 'email sent'}), status=200)

        else:
            return Response(dumps({'detail': 'user not found'}), status=404)


class ClientViewSet(viewsets.ModelViewSet):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()


class DependentViewSet(viewsets.ModelViewSet):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()


class ActiveClientViewSet(viewsets.ModelViewSet):
    serializer_class = ActiveClientSerializer
    queryset = ActiveClient.objects.all()


class AddressViewSet(viewsets.ModelViewSet):
    serializer_class = AddressSerializer
    queryset = Address.objects.all()


class StateViewSet(viewsets.ModelViewSet):
    serializer_class = StateSerializer
    queryset = State.objects.all()


class CountryViewSet(viewsets.ModelViewSet):
    serializer_class = CountrySerializer
    queryset = Country.objects.all()


class BankAccountViewSet(viewsets.ModelViewSet):
    serializer_class = BankAccountSerializer
    queryset = BankAccount.objects.all()
