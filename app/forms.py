from django import forms

class ContactForm(forms.Form):
    #email_from = forms.EmailField(label = 'De')
    email = forms.EmailField(label = 'Para')
    subject = forms.CharField(label = 'Asunto')  
    
    message = forms.CharField(label = 'Mensaje',
                                widget = forms.Textarea)