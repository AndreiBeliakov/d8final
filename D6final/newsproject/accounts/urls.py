from django.urls import path
from .views import AccountView, upgrade_me, subscribe_me


urlpatterns = [
    path('account/', AccountView.as_view()),
    path('upgrade/', upgrade_me, name='upgrade'),
    path('subscribe/', subscribe_me, name='subscribe'),
    path('news/subscribe/', subscribe_me, name='subscribe')

]