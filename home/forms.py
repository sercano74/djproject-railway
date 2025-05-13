from django import forms

class ContactoForm(forms.Form):
    nombre = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    celular = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}))
    mensaje = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))

    def __str__(self):
        return f"{self.nombre} - {self.email}"