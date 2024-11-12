# homepage/urls.py

from django.urls import path
from homepage.views import ProdutoSaldoView  # Corrija a importação para views.py, não urls.py

urlpatterns = [
    path('', ProdutoSaldoView.as_view(), name='homepage'),  # Corrija o método para as_view()
]
