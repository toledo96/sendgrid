from django.views.generic import TemplateView
from app.forms import ContactForm
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.conf import settings

class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['contact_form'] = ContactForm()
        return context

    def post(self,request,*args, **kwargs):
        #email_from = request.POST.get('email_from')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        #print("email_from:")
        #print(email_from)
        print("email:")
        print(email)
        print("subject:")
        print(subject)
        print("message:")
        print(message)
        # body = render_to_string(
        #     'email_content.html',{
        #         'email_from':email_from,
        #         'email':email,
        #         'subject':subject,
        #         'message':message,
        #     },
        # )
        #aqui viene la parte de enviar mensaje
        # message = Mail(
        #                 # from_email=email_from,
        #                 to_emails= email,
        #                 subject=subject,
        #                 html_content=message)
        # try:
        #     sg = SendGridAPIClient('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')
        #     response = sg.send(message)
        #     print(response.status_code)
        #     print(response.body)
        #     print(response.headers)
        # except Exception as e:
        #     print(e)
        #email_from = settings.DEFAULT_FROM_EMAIL
        send_mail(subject,message,'153170@ids.upchiapas.edu.mx',[email],fail_silently=False)

        return redirect('home')
