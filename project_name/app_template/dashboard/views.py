import json

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.exceptions import PermissionDenied
from django.contrib import messages

from helpers.dashboard import dashboard_permission

@dashboard_permission
def main(request):
    return render(request, '{% templatetag openvariable %}app_name{% templatetag closevariable %}/dashboard/main.html', {
        'app_title':'{% templatetag openvariable %}app_name|title{% templatetag closevariable %}',
        })