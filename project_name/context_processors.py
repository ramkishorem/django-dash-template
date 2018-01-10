from django.conf import settings

def string_resources(request):
    return {
        'ORG_NAME': settings.ORG_NAME,
        'SITE_NAME': settings.SITE_NAME,
        'CONTACT_EMAIL': settings.CONTACT_EMAIL,
        'LOGIN_URL': settings.LOGIN_URL,
    }
