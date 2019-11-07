from django.shortcuts import render
from . import forms, models
from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect
import sys 
import requests


def mailing(request):
    title = "Join Mailing List"
    if request.method == 'POST':
        # POST, generate form with data from the request
        form = forms.MailingForm(request.POST)
        # Call is_valid() to validate data and create cleaned_data and errors dict
        if form.is_valid():
            # Extract form values
            dog_name = form.cleaned_data['dog']
            first_name = form.cleaned_data['first']
            last_name = form.cleaned_data['last']
            email = form.cleaned_data['email']
            

            mailing_list = {
                "Dog_Name":dog_name,
                "First_Name":first_name,
                "Last_Name":last_name,
                "email": email
                }
            


            try:
                requests.post('https://rkbiojpoih.execute-api.us-west-2.amazonaws.com/prod/', json=mailing_list)
                action = 'POST_SUCCESSFULL'
            except ValidationError as err:
                for err in err.messages:
                    form.add_error(None, err)
                action = 'POST_FAILED'
            except:
                print("Unexpected error: " + sys.exc_info()[0])
                form.add_error(None,'Unexpected error - Please contact your system administrator')
                action = 'POST_FAILED'
        else:
            action = 'POST_FAILED'
    else:
        action = 'GET'
        form = forms.MailingForm(auto_id=False, initial={
                              'email': '.com'})
    return render(request, 'mailing/mailing.html', {'action': action, 'form': form, 'title': title})

# Create your views here.
