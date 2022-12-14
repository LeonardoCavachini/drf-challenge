from django.conf.urls import url, include
from rest_auth.views import (
    LoginView,
    LogoutView,
    UserDetailsView,
    PasswordChangeView,
    PasswordResetConfirmView,
    PasswordResetView,
)
from rest_auth.registration.views import (
    RegisterView,
)
from rest_framework_nested import routers

from .views import (
    ChangeEmailViewSet,
    ChangeEmailConfirmationViewSet,
)

###
# Routers
###
""" Main router """
router = routers.SimpleRouter()

###
# URLs
###
urlpatterns = [
    url(
        r'^login/$',
        LoginView.as_view(),
        name='rest_login',
    ),
    url(
        r'^logout/$',
        LogoutView.as_view(),
        name='rest_logout',
    ),
    url(
        r'^user/$',
        UserDetailsView.as_view(),
        name='rest_user_details',
    ),
    url(
        r'^change-password/$',
        PasswordChangeView.as_view(),
        name='rest_password_change',
    ),
    url(
        r'^change-email/(?P<uuid>[^/]+)/$',
        ChangeEmailConfirmationViewSet.as_view(),
        name='change-email-confirmation',
    ),
    url(
        r'^change-email/$',
        ChangeEmailViewSet.as_view(),
        name='change-email',
    ),
    url(
        r'^password/reset/$',
        PasswordResetView.as_view(),
        name='rest_password_reset',
    ),
    url(
        r'^password/reset/confirm/$',
        PasswordResetConfirmView.as_view(),
        name='rest_password_reset_confirm',
    ),
    url(
        r'^register/$',
        RegisterView.as_view(),
        name='rest_register',
    ),
    url(r'^', include(router.urls)),
]
