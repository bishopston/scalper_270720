from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('paginate_test/', views.paginate_test, name='paginate_test'), #paginate test
    path('bootstrap_filter/', views.BootstrapFilterView, name='bootstrap_filter'), #bootstrap filter test
    path('<int:pk>/', views.OptionDetailView, name='option_detail'), #get option by pk test
    path('optionftse/', views.OptionFtseView, name='option_ftse'), #get FTSE options distinct strikes per user input
    path('optionftse_djform/', views.OptionFtseViewDJForm, name='option_ftse_djform'), #get FTSE options distinct strikes per user input
    path('optionftse/<slug:optionsymbol>/', views.OptionFtseViewDetail, name='option_ftse_strikespan'), #get detailed FTSE option
    path('zingchart/<str:stock>/', views.zingchartView, name="zingchart"), #render zingchart for optionsymbol/closing_price
    path('zingchart/bar/<slug:tradesymbol>/', views.zingchartView1, name="zingchart1"), #get zingchart optionsymbol/closing_price
    path('zingchart/chart/<str:obj>/', views.zingchartView2, name="zingchart2"), #get zingchart date/closing_price for specific optionsymbol
    path('jschart/<str:optionsymbol>/', views.JSChartView, name='js_chart'), #render jschart for date/closing_price
    path('jschart/chart/<str:tradesymbol>/', views.JSChartView1, name="js_chart1"), #get jschart date/closing_price for specific optionsymbol
    #path('simple_IV/', views.IVCalcView, name='iv_calc'),
    #path('simple_model_IV/', views.IVModelCalcView, name='iv_model_calc'),
    path('IV_per_date/', views.IVDateListView, name='iv_date_list'),
    path('option/ivdate/<str:optionsymbol>/', views.OptionIVDateViewDetail, name='option_iv_date_detail'), #get detailed option IV per date
    path('zingchart3/bar/<str:tradesymbol>/', views.zingchartView3, name="zingchart3"), #get zingchart optionsymbol/closing_price
    path('zingchart3/bar/<str:tradesymbol>/', views.zingchartView3, name="zingchart3"), #get zingchart optionsymbol/closing_price
]