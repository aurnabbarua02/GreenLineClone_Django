from django import forms

class sendmessageform(forms.Form):
    name = forms.CharField(widget=forms.TextInput(), required=False)
    email = forms.EmailField(widget=forms.EmailInput(), required=False)
    subject = forms.CharField(widget=forms.TextInput(), required=False)
    message = forms.CharField(widget=forms.Textarea(), required=False)

class EticketForm(forms.Form):
    leaving_from = forms.ChoiceField(
        choices=[],  
        widget=forms.Select(attrs={'id': 'LEAVING_FROM'})
    )
    going_to = forms.ChoiceField(
        choices=[],  
        widget=forms.Select(attrs={'id': 'GOING_TO'})
    )
    date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'id': 'date'})
    )

class ConfirmTicketForm(forms.Form):
    passenger_name = forms.CharField(max_length=100) 
    passenger_email = forms.EmailField(max_length=100)    
    number_of_ticket = forms.IntegerField()
    transaction_id = forms.CharField(max_length=30)
