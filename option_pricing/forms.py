from django import forms
from . models import Option

import datetime

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field, Fieldset
from crispy_forms.bootstrap import FormActions, InlineRadios

EXP_YEAR_CHOICES = [('', ''), ('2019', '2019'), ('2020', '2020'), ('2021', '2021'),]
EXP_MONTH_CHOICES = [
    ('', ''),
    ('1', 'JAN'),
    ('2', 'FEB'),
    ('3', 'MAR'),
]

OPTION_TYPE = [
    ('call', 'Call'),
    ('put', 'Put'),
]

class OptionSelectionForm(forms.Form):
    option_type = forms.ChoiceField(
        label="Option Type",
        widget=forms.RadioSelect,
        choices=OPTION_TYPE,
        initial = 'call',
    )
    exp_month = forms.CharField(
        label="Expiration Month",
        widget=forms.Select(
        choices=EXP_MONTH_CHOICES,
    ))
    exp_year = forms.CharField(
        label="Expiration Year",
        widget=forms.Select(
        choices=EXP_YEAR_CHOICES,
    ))


    # Uni-form
    helper = FormHelper()
    helper.form_method = 'GET'
    #helper.form_class = 'form-horizontal'
    #helper.label_class = 'col-lg-4'
    #helper.field_class = 'col-lg-8'
    #helper.add_input(Submit('submit', 'Submit', css_class='btn_primary'))
    helper.layout = Layout(

        InlineRadios('option_type', style="font-size: 0.8rem;"),
        Field('exp_month', style="font-size: 0.8rem;"),
        Field('exp_year', style="font-size: 0.8rem;"),
        FormActions(
            Submit('submit', 'Submit', css_class="btn-primary"),
        )
    )


class SimpleIVForm(forms.ModelForm):
    class Meta:
        model = Option
        fields = ['optiontype', 'asset', 'date', 'strike', 'expmonthyear']
"""
        widgets = {
            'optiontype':forms.TextInput(attrs={'class':'form-control'}),
            'asset':forms.TextInput(attrs={'class':'form-control'}),
            'expmonthyear': forms.TextInput(attrs={'class':'form-control'}),
            'strike' : forms.ModelChoiceField(queryset=Option.objects.all())
        }
"""


class TestIVForm(forms.Form):
    callputflag = forms.CharField(max_length=5)
    assetname = forms.CharField(max_length=10)
    exp_month = forms.CharField(max_length=10)
    exp_year = forms.CharField(max_length=5)
    calc_date = forms.DateField(initial=datetime.date.today)
    strike_price = forms.ModelChoiceField(queryset=Option.objects.none())
"""
    def __init__(self, *args, **kwargs):
        callputflagid = kwargs.pop('callputflag', None)
        assetnameid = kwargs.pop('assetname', None)
        exp_monthid = kwargs.pop('exp_month', None)
        exp_yearid = kwargs.pop('exp_year', None)
        super(TestIVForm, self).__init__(*args, **kwargs)
        if callputflagid and assetnameid and exp_monthid and exp_yearid:
            self.fields['strike'].queryset = Option.objects.filter(optiontype__exact=callputflagid).filter(asset__exact=assetnameid).filter(expmonthyear__month__exact=exp_monthid).filter(expmonthyear__year__exact=exp_yearid).values_list('strike', flat=True).order_by('strike')

        if assetnameid:
            self.fields['strike'].queryset = Option.objects.filter(asset__exact=assetnameid).values_list('strike', flat=True).order_by('strike')
        if exp_monthid:
            self.fields['strike'].queryset = Option.objects.filter(expmonthyear__month__exact=exp_monthid).values_list('strike', flat=True).order_by('strike')
        if exp_yearid:
            self.fields['strike'].queryset = Option.objects.filter(expmonthyear__year__exact=exp_yearid).values_list('strike', flat=True).order_by('strike')
"""
