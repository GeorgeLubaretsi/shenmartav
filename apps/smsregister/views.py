# -*- coding: utf-8 -*
"""
Views contact
"""
__docformat__ = 'epytext en'


from django.core.mail import send_mail
from django.shortcuts import redirect
from django.utils.translation import ugettext as _
from django.views.generic import FormView, TemplateView

from .forms import SMSRegisterForm



class Show (FormView):
    """Show SMS registration form."""
    template_name = 'smsregister/show.html'
    form_class = SMSRegisterForm


    def form_valid (self, form):
        subject = u""
        body = (u"addmobile "+ 
                form.data['name'].replace(" ","") + u" " +
                form.data['number'] + u" " +
                form.data['lang'] + u" " +
                u"False" + u" " +
                form.data['subscribe'])

        send_mail(subject, body, 'registration@myparliament.ge',['derek@transparency.ge'])

        return redirect('smsregister_thanks')


    def form_invalid (self, form):
        return self.render_to_response({'form': form})



class Thanks (TemplateView):
    """Show thanks page."""
    template_name = 'smsregister/thanks.html'