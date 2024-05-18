import os
from dotenv import load_dotenv
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import BasePermission

from .models import Rates, Account, Place, WorkerAccount, ClientOrder, UserLanguage
from .serializers import (
    RatesSerializer,
    AccountSerializer,
    PlaceSerializer,
    WorkerSerializer,
    ClientOrderSerializer,
    UserLanguageSerializer
)

load_dotenv()


class CustomPermission(BasePermission):
    def has_permission(self, request, view):
        token = request.headers.get('Authorization')
        base_token_client = os.environ['TOKEN']
        base_token_worker = os.environ['WORKER-TOKEN']
        return token == base_token_client or token == base_token_worker


class RatesView(generics.ListAPIView):
    queryset = Rates.objects.all()
    serializer_class = RatesSerializer
    permission_classes = [CustomPermission]


class PlaceView(generics.ListAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
    permission_classes = [CustomPermission]


class AccountCreateView(generics.CreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [CustomPermission]


class WorkerCreateView(generics.CreateAPIView):
    queryset = WorkerAccount.objects.all()
    serializer_class = WorkerSerializer


class AccountByTelegramIdView(generics.RetrieveUpdateAPIView):  # Изменено на RetrieveUpdateAPIView
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [CustomPermission]
    lookup_field = 'telegram_id'  # Указываем имя поля для поиска в URL

    def put(self, request, *args, **kwargs):
        telegram_id = self.kwargs.get('telegram_id')
        try:
            account = Account.objects.get(telegram_id=telegram_id)
        except Account.DoesNotExist:
            return Response({"detail": "User not found."}, status=404)

        # Обновляем значение поля is_confirm
        is_confirm = request.data.get('is_confirm')
        if is_confirm is not None:
            account.is_confirm = is_confirm
            account.save()
            serializer = self.get_serializer(account)
            return Response(serializer.data)
        else:
            return Response({"detail": "Invalid request."}, status=400)


class WorkerAccountByTelegramIdView(generics.RetrieveUpdateDestroyAPIView):  # Изменено на RetrieveUpdateDestroyAPIView
    queryset = WorkerAccount.objects.all()
    serializer_class = WorkerSerializer
    permission_classes = [CustomPermission]
    lookup_field = 'telegram_id'  # Указываем имя поля для поиска в URL

    def put(self, request, *args, **kwargs):
        telegram_id = self.kwargs.get('telegram_id')
        try:
            account = WorkerAccount.objects.get(telegram_id=telegram_id)
        except WorkerAccount.DoesNotExist:
            return Response({"detail": "User not found."}, status=404)

        # Обновляем значение поля is_confirm
        is_confirm = request.data.get('is_confirm')
        if is_confirm is not None:
            account.is_confirm = is_confirm
            account.save()
            serializer = self.get_serializer(account)
            return Response(serializer.data)
        else:
            return Response({"detail": "Invalid request."}, status=400)


class AccountDeleteAPIView(generics.DestroyAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [CustomPermission]
    lookup_field = 'telegram_id'  # Указываем имя поля для поиска в URL


class ClientOrderView(generics.ListCreateAPIView):
    queryset = ClientOrder.objects.filter(is_completed=False, is_taken=False)
    serializer_class = ClientOrderSerializer
    permission_classes = [CustomPermission]


class ClientOrderByIDView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ClientOrder.objects.all()
    serializer_class = ClientOrderSerializer
    permission_classes = [CustomPermission]


class UserLanguageListAPIView(generics.ListCreateAPIView):
    queryset = UserLanguage.objects.all()
    serializer_class = UserLanguageSerializer
    permission_classes = [CustomPermission]
