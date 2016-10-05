from django import forms

from .models import Departamento

class DepartamentoForm(forms.ModelForm):

	class Meta:
		model = Departamento

		fields = [
		'Id_departamento',
		'nombre',
		'Estado',

		]

		labels= {
		'Id_departamento': 'Id_departamento',
		'nombre': 'nombre',
		'Estado': 'Estado',
		
}


widgets= {
		'Id_departamento': forms.TextInput(attrs={'class':'form-control'}),
        'nombre': forms.TextInput(attrs={'class':'form-control'}),
		'Estado': forms.Select(attrs={'class':'form-control','id':'InputEstado'}),
}