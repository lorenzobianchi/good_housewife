from django import forms
from .models import Spesa, TipoSpesa
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Div, HTML

class SpesaForm(forms.ModelForm):

    class Meta:
        model = Spesa
        fields = ('__all__')

    def __init__(self, *args, **kwargs):
        super(SpesaForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = "spesa_form";
        self.helper.include_media = False
        self.helper.layout = Layout(
            Div(
                Div('importo', css_class='col-sm-6 col-xs-12'),
                Div('causale', css_class='col-sm-6 col-xs-12'),
                css_class='row mb-4'
            ),
            Div(
                Div('data', css_class='col-sm-6 col-xs-12'),
                Div('tipo_spesa', css_class='col-sm-6 col-xs-12'),
                css_class='row mb-4'
            ),
            Div(
                Div('note', css_class='col-sm-12 col-xs-12'),
                css_class='row mb-4'
            ),
            Div(
                Div(
                    # HTML('<a class="btn btn-danger white" href="%s">ANNULLA</a>' % reverse('agente_detail', kwargs={'pk':self.instance.agente.pk})),
                    Submit('submit', 'SALVA', css_class="pull-right"),
                    css_class="col-md-12"
                ),
                css_class='row'
            ),
        )


class TipoSpesaForm(forms.ModelForm):

    class Meta:
        model = TipoSpesa
        fields = ('__all__')

    def __init__(self, *args, **kwargs):
        super(TipoSpesaForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = "tipo_spesa_form";
        self.helper.include_media = False
        self.helper.layout = Layout(
            Div(
                Div('nome', css_class='col-sm-4 col-xs-12'),
                css_class='row mb-4'
            ),
            Div(
                Div('colore_badge', css_class='col-sm-4 col-xs-12'),
                css_class='row mb-4'
            ),
            Div(
                Div('spesa_ordinaria', css_class='col-sm-4 col-xs-12'),
                css_class='row mb-4'
            ),
            Div(
                Div(
                    # HTML('<a class="btn btn-danger white" href="%s">ANNULLA</a>' % reverse('agente_detail', kwargs={'pk':self.instance.agente.pk})),
                    Submit('submit', 'SALVA', css_class="pull-right"),
                    css_class="col-md-12"
                ),
                css_class='row'
            ),
        )
