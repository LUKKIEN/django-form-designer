import os
import random
from datetime import datetime
from os import path
from os.path import join
import logging

from django.core.context_processors import csrf
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.db import models
from form_designer.models import FormDefinition
from django.utils.translation import ugettext as _
from django import forms
from django.forms import widgets
from django.http import HttpResponseRedirect
from django.conf import settings
from form_designer import app_settings


class DesignedForm(forms.Form):
    def __init__(self, form_definition, initial_data=None, *args, **kwargs):
        super(DesignedForm, self).__init__(*args, **kwargs)
        for def_field in form_definition.formdefinitionfield_set.all():            
            self.add_defined_field(def_field, initial_data)
        self.fields[form_definition.submit_flag_name] = forms.BooleanField(required=False, initial=1, widget=widgets.HiddenInput)

    def add_defined_field(self, def_field, initial_data=None):
        if initial_data and initial_data.has_key(def_field.name):
            if not def_field.field_class in ('forms.MultipleChoiceField', 'forms.ModelMultipleChoiceField'):
                def_field.initial = initial_data.get(def_field.name)
            else:
                def_field.initial = initial_data.getlist(def_field.name)
        self.fields[def_field.name] = eval(def_field.field_class)(**def_field.get_form_field_init_args())        

def process_form(request, form_definition, context={}, is_cms_plugin=False):
    logger = logging.getLogger('Form')

    success_message = form_definition.success_message or _('Thank you, the data was submitted successfully.')
    error_message = form_definition.error_message or _('The data could not be submitted, please try again.')

    message = None    
    form_error = False
    form_success = False
    
    is_submit = False
    
    # If the form has been submitted...
    if request.method == 'POST' and request.POST.get(form_definition.submit_flag_name):
        form = DesignedForm(form_definition, None, request.POST, request.FILES)
        is_submit = True
    if request.method == 'GET' and request.GET.get(form_definition.submit_flag_name):
        form = DesignedForm(form_definition, None, request.GET)
        is_submit = True
        
    if is_submit:
        if form.is_valid():

            logger.info('process_form: mailing to {0}, from {1}, subject: {2}'.format(form_definition.mail_to, form_definition.mail_from, form_definition.mail_subject)) #TODO: remove this (only added to debug contact mailing issue on production

            # Handle file uploads
            files = []
            if hasattr(request, 'FILES'):
                logger.info('process_form: adding {0} file{1}'.format(len(request.FILES), 's' if len(request.FILES) > 1 else '')) #TODO: remove this (only added to debug contact mailing issue on production
                for file_key in request.FILES:
                    file_obj = request.FILES[file_key]
                    file_name = '%s.%s_%s' % (
                        datetime.now().strftime('%Y%m%d'),
                        random.randrange(0, 10000),
                        file_obj.name,
                    )
                    
                    if not os.path.exists(settings.FORM_UPLOADS):
                        os.mkdir(settings.FORM_UPLOADS)
                    
                    destination = open(join(settings.FORM_UPLOADS, file_name), 'wb+')
                    for chunk in file_obj.chunks():
                        destination.write(chunk)
                    destination.close()
                    form.cleaned_data[file_key] = join(settings.FORM_UPLOADS_URL, file_name)
                    files.append(join(settings.FORM_UPLOADS, file_name))
            
            # Successful submission
            if 'django_notify' in settings.INSTALLED_APPS:
                request.notifications.success(success_message)
            else:
                form_success = True
                message = success_message
            if form_definition.log_data:
                form_definition.log(form)
            if form_definition.mail_to:
                logger.info('process_form: sending mail') #TODO: remove this (only added to debug contact mailing issue on production
                form_definition.send_mail(form, files)
            if form_definition.success_redirect and not is_cms_plugin:
                # TODO Redirection does not work for cms plugin
                return HttpResponseRedirect(form_definition.action or '?')
            if form_definition.success_clear:
                form = DesignedForm(form_definition) # clear form
        else:
            form_error = True
            if form.errors:
                error_message += ' ' + _('Please check the following field(s): ') + ', '.join(form.errors)
            if 'django_notify' in settings.INSTALLED_APPS:
                request.notifications.error(error_message)
            else:
                message = error_message
    else:        
        if form_definition.allow_get_initial:
            form = DesignedForm(form_definition, initial_data=request.GET)
        else:
            form = DesignedForm(form_definition)
    
    context.update({
        'message': message,
        'form_error': form_error,
        'form_success': form_success,
        'form': form,
        'form_definition': form_definition
    })
    context.update(csrf(request))

    return context

def detail(request, object_name):
    form_definition = get_object_or_404(FormDefinition, name=object_name)
    result = process_form(request, form_definition)
    if isinstance(result, HttpResponseRedirect):
        return result
    else:
        result.update({
            'form_template': form_definition.form_template_name or app_settings.get('FORM_DESIGNER_DEFAULT_FORM_TEMPLATE')
        })
        return render_to_response('html/formdefinition/detail.html', result, context_instance=RequestContext(request))
