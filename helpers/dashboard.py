from django.contrib.auth.decorators import user_passes_test
from django.conf import settings

dashboard_permission = user_passes_test(
    lambda u:u.is_staff or u.is_superuser, login_url=settings.LOGIN_URL)

is_superuser = user_passes_test(lambda u:u.is_superuser,
    login_url=settings.LOGIN_URL)
