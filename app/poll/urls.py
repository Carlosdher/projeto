from django.urls import include, path
from django.conf.urls import include, url
from django.contrib.auth import views as auth_views

from . import views as poll

app_name = 'poll'

urlpatterns = [
    # Propose
    path('propostas/', poll.ProposeView.as_view(), name='propose-list'),
    path('proposta/nova/', poll.ProposeCreateView.as_view(), name='propose-create'),
    path('proposta/<uuid:pk>/', poll.ProposeDetailView.as_view(), name='propose-detail'),
]