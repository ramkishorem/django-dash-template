from decimal import Decimal as decim

from django.db.models import Sum
from django.template import loader, RequestContext, Context
from django.core.mail import send_mail, EmailMessage
from django.conf import settings

def get_default_record(Model):
    """used for models where a default record will be created with pk 1 using fixtures

    parameters:
        model"""
    return Model.objects.get(pk = 1)

def get_object_with_property(Model, property, value):
    """used to get object by specifying a property.

    the property has to be unique for this
    parameters:
        Model
        property as string
        value"""
    for item in Model.objects.all():
        if item.__getattribute__(property) == value:
            return item
    raise Model.DoesNotExist

def render_for_json(request, template_name, data_dict):
    t = loader.get_template(template_name)
    c = RequestContext(request, data_dict)
    return t.render(c)

def render_template_as_string(template_name, data_dict):
    t = loader.get_template(template_name)
    c = Context(data_dict)
    return t.render(c)

def serialize_decimal_default(obj):
    """
    to make decimal values json serializable
    """
    if isinstance(obj, decim):
        return str(obj)
    raise TypeError

def send_email(subject, message, recipients, html_message='',
    sender=settings.DEFAULT_FROM_EMAIL, bcc_admin = False, bcc_list = []):

    subject = "%s - %s"%(settings.ORG_NAME, subject)
    if settings.DEBUG:
        print(message, html_message)
    bcc = [settings.CONTACT_EMAIL] if bcc_admin else []
    message = html_message or message
    email = EmailMessage(subject, message, sender, recipients, bcc+bcc_list)
    if html_message:
        email.content_subtype='html'
    email.send()

def get_many_to_many_value_from_ajax_request(request, field_name):
    raw_value = request.GET.get(field_name, None)
    if raw_value == 'null':
        raw_value = None
    return raw_value.split(',') if raw_value else []
