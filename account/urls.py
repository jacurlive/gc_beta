from django.urls import path
from .views import (
    RatesView,
    AccountCreateView,
    PlaceView,
    AccountByTelegramIdView,
    AccountDeleteAPIView,
    WorkerCreateView,
    WorkerAccountByTelegramIdView,
    ClientOrderView,
    ClientOrderByIDView,
    UserLanguageListAPIView,
    UserLanguageDetailAPIView,
    AccountDetailByPhoneNumberAPIView,
    RateDetailByID
)

urlpatterns = [
    path("rates/", RatesView.as_view()),
    path("account/", AccountCreateView.as_view()),
    path("place/", PlaceView.as_view()),
    path("account/<int:telegram_id>", AccountByTelegramIdView.as_view()),
    path("account/phone/<str:phone_number>", AccountDetailByPhoneNumberAPIView.as_view()),
    path("account/delete/<int:telegram_id>", AccountDeleteAPIView.as_view()),
    path("worker/", WorkerCreateView.as_view()),
    path("worker/<int:telegram_id>", WorkerAccountByTelegramIdView.as_view()),
    path("order/", ClientOrderView.as_view()),
    path("order/<int:pk>", ClientOrderByIDView.as_view()),
    path("account/language", UserLanguageListAPIView.as_view()),
    path("account/language/<int:user_id>", UserLanguageDetailAPIView.as_view()),
    path("rates/<int:pk>", RateDetailByID.as_view())
]
