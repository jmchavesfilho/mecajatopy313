from django.forms import ModelForm
from .models import Servico, CategoriaManutencao

class FormServico(ModelForm):
    class Meta:
        model = Servico
        exclude = ['finalizado', 'protocolo']

    def _init_(self, *args, **kwargs):
        super()._init_(*args, **kwargs)     
        print(self.fields['titulo'].widget.att)



        #aula 06  parada 20min
