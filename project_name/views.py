from django.http import HttpResponseRedirect
from django.urls import reverse
from django.conf import settings

def login_redirect(request):
    if request.user.is_staff or request.user.is_superuser:
        return HttpResponseRedirect(reverse('dashboard:main'))
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('home'))
    return HttpResponseRedirect(settings.LOGIN_URL)
