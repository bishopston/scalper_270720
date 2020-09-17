from django.shortcuts import get_object_or_404, render
from django.db.models import Sum
from .models import Option, Stock
from .filters import OptionFilter
from .forms import OptionSelectionForm, TestIVForm, SimpleIVForm
import datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.views.generic import TemplateView
from django.http import JsonResponse

import json


def home(request):
    option_list = Option.objects.filter(date__gt='2020-3-30').order_by('date')[:5]
    option_filter = OptionFilter(request.GET, queryset=option_list)
    return render(request, 'option_pricing/option_list.html', { 'option_filter': option_filter })


def paginate_test(request):
    option_list = Option.objects.filter(date__gt='2020-4-28 12:00:00').order_by('date')[:200]
    paginator = Paginator(option_list, 100)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'option_pricing/paginate_test_2.html', {'page_obj': page_obj})

   
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
    option_ftse = Option.objects.filter(asset='FTSE').distinct('strike').order_by('strike')
    
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


def OptionFtseViewDJForm(request):
    option_ftse = Option.objects.filter(asset='FTSE').distinct('strike').order_by('strike')
    
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
        'optionselectionform' : OptionSelectionForm(),
    }
    return render(request, 'option_pricing/optionftse_djform.html', context)


def OptionFtseViewDetail(request, optionsymbol):
    option_ftse_strikespan = Option.objects.filter(optionsymbol=optionsymbol).order_by('-date')
    option_symbol = Option(optionsymbol=optionsymbol)
    trade_symbol = option_symbol.optionsymbol 

    context = {
        'option_ftse_strikespan' : option_ftse_strikespan,
        'trade_symbol' : trade_symbol,
    }

    return render(request, 'option_pricing/option_ftse_strikespan.html', context)

def zingchartView(request, stock):

    question = Option(asset=stock)
    stock_name = question.asset

    return render(request, 'option_pricing/zingchart.html', {'stock_name': stock_name})

def zingchartView1(request, tradesymbol):
    optiondata = []

    option = Option.objects.filter(optionsymbol=tradesymbol).order_by('date')
    #opt = option.all()

    for i in option:
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


"""
def IVCalcView(request):
    qs = Option.objects.all()

    testIVform = TestIVForm()
        
    callputflag_query = request.GET.get('callputflag')
    asset_name_query = request.GET.get('assetname')
    exp_month_query = request.GET.get('exp_month')
    exp_year_query = request.GET.get('exp_year')
    calc_date_query = request.GET.get('calc_date')

    if callputflag_query != '' and callputflag_query is not None:
        qs = qs.filter(optiontype__icontains=callputflag_query)

    if asset_name_query != '' and asset_name_query is not None:
        qs = qs.filter(asset__icontains=asset_name_query)

    if exp_month_query != '' and exp_month_query is not None:
        qs = qs.filter(expmonthyear__month=exp_month_query)

    if exp_year_query != '' and exp_year_query is not None:
        qs = qs.filter(expmonthyear__year=exp_year_query)

    if callputflag_query != '' and callputflag_query is not None:
        if asset_name_query != '' and asset_name_query is not None:
            if exp_month_query != '' and exp_month_query is not None:
                if exp_year_query != '' and exp_year_query is not None:
                    testIVform.fields['strike_price'].queryset = qs
    #testIVform.fields['strike_price'].queryset = qs

    #testIVform = TestIVForm(callputflag_query, asset_name_query, exp_month_query, exp_year_query)

    context = {
        'qs' : qs,
        'callputflag_query': callputflag_query,
        'asset_name_query': asset_name_query,
        'exp_month_query' : exp_month_query,
        'exp_year_query' : exp_year_query,
        'testIVform': testIVform,
    }
    return render(request, 'option_pricing/iv_test_strike.html', context)

"""
"""
def IVModelCalcView(request):
    qs = Option.objects.all()

    simpleIVForm = SimpleIVForm()
        
    callputflag_query = request.GET.get('callputflag')
    asset_name_query = request.GET.get('assetname')
    exp_date_query = request.GET.get('expmonthyear')
    #calc_date_query = request.GET.get('calc_date')

    if callputflag_query != '' and callputflag_query is not None:
        qs = option_ftse.filter(optiontype__icontains=callputflag_query)

    if asset_name_query != '' and asset_name_query is not None:
        qs = option_ftse.filter(asset__icontains=asset_name_query)

    if exp_date_query != '' and exp_date_query is not None:
        qs = option_ftse.filter(expmonthyear__icontains=exp_date_query)

    simpleIVForm.fields['strike'].queryset = Option.objects.filter(optiontype__exact=callputflag_query).filter(asset__exact=asset_name_query).filter(expmonthyear__exact=exp_date_query).values_list('strike', flat=True).order_by('strike')
    #testIVform.fields['strike_price'].queryset = qs

    context = {
        'qs' : qs,
        'callputflag_query': callputflag_query,
        'asset_name_query': asset_name_query,
        'exp_date_query' : exp_date_query,
        'simpleIVForm': simpleIVForm,
    }
    return render(request, 'option_pricing/iv_test_model_strike.html', context)

"""

def IVDateListView(request):
    qs = Option.objects.all().distinct('strike').order_by('strike')
    
    callputflag_query = request.GET.get('option_type')
    asset_name_query = request.GET.get('asset_name')
    exp_month_query = request.GET.get('exp_month')
    exp_year_query = request.GET.get('exp_year')

    if callputflag_query != '' and callputflag_query is not None:
        qs = qs.filter(optiontype__icontains=callputflag_query)

    if asset_name_query != '' and asset_name_query is not None:
        qs = qs.filter(asset__icontains=asset_name_query)

    if exp_month_query != '' and exp_month_query is not None:
        qs = qs.filter(expmonthyear__month=exp_month_query)

    if exp_year_query != '' and exp_year_query is not None:
        qs = qs.filter(expmonthyear__year=exp_year_query)

    context = {
        'queryset' : qs,
        'callputflag_query': callputflag_query,
        'asset_name_query': asset_name_query,
        'exp_month_query' : exp_month_query,
        'exp_year_query' : exp_year_query,
        #'optionselectionform' : OptionSelectionForm(),
    }
    return render(request, 'option_pricing/iv_date_list.html', context)

def OptionViewDetail(request, optionsymbol):
    option_strikespan = Option.objects.filter(optionsymbol=optionsymbol).order_by('-date')
    option_symbol = Option(optionsymbol=optionsymbol)
    trade_symbol = option_symbol.optionsymbol 

    context = {
        'option_strikespan' : option_strikespan,
        'trade_symbol' : trade_symbol,
    }

    return render(request, 'option_pricing/option_strikespan.html', context)

def zingchartView3(request, tradesymbol):
    optiondata = []

    option = Option.objects.filter(optionsymbol=tradesymbol).order_by('date')
    #opt = option.all()

    for i in option:
        optiondata.append({json.dumps(i.date.strftime("%d-%m-%Y")):i.closing_price})

    print(optiondata)
    return JsonResponse(optiondata, safe=False)

def OptionIVDateViewDetail(request, optionsymbol):
    closing_prices = Option.objects.filter(optionsymbol=optionsymbol).order_by('date').values_list('closing_price', flat=True)
    strikes = Option.objects.filter(optionsymbol=optionsymbol).order_by('date').values_list('strike', flat=True)
    dates = Option.objects.filter(optionsymbol=optionsymbol).order_by('date').values_list('date', flat=True)
    str_dates = [date_obj.strftime('%Y-%m-%d') for date_obj in dates]
    asset_name = Option.objects.filter(optionsymbol=optionsymbol).values_list('asset', flat=True)
    _asset_name = asset_name[0]+'.ATH'
    stock_prices = Stock.objects.filter(symbol=_asset_name).filter(date__range=(str_dates[0], str_dates[-1])).order_by('date').values_list('close', flat=True)

    return render(request, 'option_pricing/option_ftse_strikespan.html', context)
    