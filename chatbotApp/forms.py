from django import forms

class MessageForm(forms.Form):
	question = forms.CharField(label=False, widget=forms.TextInput(attrs={'size': '40', 'id':'id_text', 'class': "user_input"}))