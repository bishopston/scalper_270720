from django.shortcuts import get_object_or_404, render
from django.db.models import Sum
from .models import Option, OptionSymbol, OptionAsset
from .filters import OptionFilter
import datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.views.generic import TemplateView
from django.http import JsonResponse

import json


def home(request):
    option_list = Option.objects.filter(date__gt='2020-3-30').order_by('date')[:5]
    option_filter = OptionFilter(request.GET, queryset=option_list)
    return render(request, 'option_pricing/option_list.html', { 'option_filter': option_filter })


def paginate_test_1(request):
    option_list = Option.objects.filter(date__gt='2020-4-28 12:00:00').order_by('date')[:200]
    paginator = Paginator(option_list, 100)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'option_pricing/paginate_test_1.html', {'page_obj': page_obj})

   
def BootstrapFilterView(request):
    qs = Option.objects.all()
    underlying_query = request.GET.get('under_name')
    callputflag_query = request.GET.get('option_type')
    exp_date_query = request.GET.get('exp_date')

    if underlying_query != '' and underlying_query is not None:
        qs = qs.filter(asset__icontains=underlying_query)

    if callputflag_query != '' and callputflag_query is not None:
        qs = qs.filter(optiontype__icontains=callputflag_query)

    if exp_date_query != '' and exp_date_query is not None:
        qs = qs.filter(expmonthyear__exact=exp_date_query)

    context = {
        'queryset' : qs,
        'underlying_query' : underlying_query,
        'callputflag_query': callputflag_query,
        'exp_date_query' : exp_date_query,
    }
    return render(request, 'option_pricing/bootstrap_filter.html', context)

def OptionDetailView(request, pk):
    option_detail = Option.objects.get(pk=pk)
    context = {
        'option_detail': option_detail
    }
    return render(request, 'option_pricing/option_detail.html', context)

def OptionFtseView(request):
    option_ftse = Option.objects.filter(asset='FTSE').order_by('date')
    
    callputflag_query = request.GET.get('option_type')
    exp_month_query = request.GET.get('exp_month')
    exp_year_query = request.GET.get('exp_year')

    if callputflag_query != '' and callputflag_query is not None:
        option_ftse = option_ftse.filter(optiontype__icontains=callputflag_query)

    if exp_month_query != '' and exp_month_query is not None:
        option_ftse = option_ftse.filter(expmonthyear__month=exp_month_query)

    if exp_year_query != '' and exp_year_query is not None:
        option_ftse = option_ftse.filter(expmonthyear__year=exp_year_query)

    context = {
        'queryset' : option_ftse,
        'callputflag_query': callputflag_query,
        'exp_month_query' : exp_month_query,
        'exp_year_query' : exp_year_query,
    }
    return render(request, 'option_pricing/option_ftse.html', context)


def OptionFtseViewDetail(request, optionsymbol):
    option_ftse_strikespan = Option.objects.filter(optionsymbol=optionsymbol).order_by('-date')
    option_symbol = Option(optionsymbol=optionsymbol)
    trade_symbol = option_symbol.optionsymbol 

    context = {
        'option_ftse_strikespan' : option_ftse_strikespan,
        'trade_symbol' : trade_symbol,
    }

    return render(request, 'option_pricing/option_ftse_strikespan.html', context)

"""class OptionChartView(TemplateView):
    template_name = 'option_pricing/chartjstest2.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['qs'] = Option.objects.filter(optionsymbol='ALPHA19I0.95').order_by('-date')
        return context
        """

def zingchartView(request, stock):

    question = Option(asset=stock)
    stock_name = question.asset

    return render(request, 'option_pricing/zingchart.html', {'stock_name': stock_name})

def zingchartView1(request, tradesymbol):
    optiondata = []

    option = Option.objects.filter(optionsymbol=tradesymbol).order_by('date')
    opt = option.all()

    for i in opt:
        optiondata.append({json.dumps(i.date.strftime("%d-%m-%Y")):i.closing_price})

    print(optiondata)
    return JsonResponse(optiondata, safe=False)

def zingchartView2(request, obj):
    optiondata = []

    queryset = Option.objects.filter(asset=obj).filter(optiontype='Call').filter(date='2019-07-01 12:00:00')
    qs = queryset.all()

    for i in qs:
        optiondata.append({i.optionsymbol:i.closing_price})

    print(optiondata)
    return JsonResponse(optiondata, safe=False)


def JSChartView(request, optionsymbol):
    option_symbol = Option(optionsymbol=optionsymbol)
    trade_symbol = option_symbol.optionsymbol 

    return render(request, 'option_pricing/jschart.html', {'trade_symbol': trade_symbol})

def JSChartView1(request, tradesymbol):
    optiondata = []

    option = Option.objects.filter(optionsymbol=tradesymbol).order_by('date')
    opt = option.all()

    for i in opt:
        optiondata.append({json.dumps(i.date.strftime("%d-%m-%Y")):i.closing_price})

    print(optiondata)
    return JsonResponse(optiondata, safe=False)