from django.urls import path
from . import views
from option_pricing.views import OptionChartView


urlpatterns = [
    path('', views.home, name="home"),
    path('paginate_test_1/', views.paginate_test_1, name='paginate_test_1'),
    path('bootstrap_filter/', views.BootstrapFilterView, name='bootstrap_filter'),
    path('<int:pk>/', views.OptionDetailView, name='option_detail'),
    path('optionftse/', views.OptionFtseView, name='option_ftse'),
    path('optionftse/<slug:optionsymbol>/', views.OptionFtseViewDetail, name='option_ftse_strikespan'),
    path('chartjstest/', OptionChartView.as_view(), name='option_chart')
]