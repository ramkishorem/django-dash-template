from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import logout, login
from django.views.generic import RedirectView

from .views import login_redirect
# from emailusernames.views import login

media_urls =  static(settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT) if settings.DEBUG else []

urlpatterns = [
    path('', RedirectView.as_view(url=settings.LOGIN_URL),
        name='home'),

    path('dashboard/', include('{{project_name}}.dashboard.urls',
        namespace='dashboard')),
    # path('user/', include('emailusernames.urls',
    #     namespace='emailusernames')),
    path('admin/', admin.site.urls),

    path('login', login, {'template_name': 'login.html'}, name='login'),
    path('login-redirect', login_redirect, name='login-redirect'),
    path('logout', logout, {
        'next_page': settings.LOGIN_URL}, name='logout'),
] + media_urls
