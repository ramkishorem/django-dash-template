from django.apps import AppConfig


class AppConfig(AppConfig):
    name = '{% templatetag openvariable %}app_name{% templatetag closevariable %}'
