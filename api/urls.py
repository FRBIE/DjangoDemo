from django.urls import path

from api.views import ProtectView,ChartDataView

urlpatterns = [
    path('protectTest/', ProtectView.as_view(), name='protected_view'),
    path('chartData/', ChartDataView.as_view(), name='chart_data'),
]