from django.urls import path, include
from django.views.generic import RedirectView
from django.conf import settings

subapp_urls_path = lambda x:'{{project_name}}.%s.dashboard.urls'%x

app_name = 'dashboard'

urlpatterns = [
    path('', RedirectView.as_view(url=settings.DASHBOARD_HOME_URL,
        permanent=False), name='main'),
    path('#firstAppName#/', include(subapp_urls_path('#firstAppName#'),
        namespace='#firstAppName#')),
]
