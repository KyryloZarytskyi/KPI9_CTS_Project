from django.urls import path
from .views import EquationView

urlpatterns = [
    path('<int:id>/', EquationView.as_view(), name='equation'),
]
