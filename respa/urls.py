from django.urls import path, re_path
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static
from tkusers import admin
from django.views.generic.base import RedirectView

from resources.api import RespaAPIRouter
from resources.views.images import ResourceImageView
from resources.views.ical import ICalFeedView

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


admin.autodiscover()

if getattr(settings, 'RESPA_COMMENTS_ENABLED', False):
    import comments.api

if getattr(settings, 'RESPA_CATERINGS_ENABLED', False):
    import caterings.api

if settings.RESPA_PAYMENTS_ENABLED:
    import payments.api.order  # noqa

router = RespaAPIRouter()

schema_view = get_schema_view(
   openapi.Info(
      title="API View",
      default_version='v1',
      description="RESPA API Documentation",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="varaamo@turku.fi"),
      license=openapi.License(name="MIT License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('ra/', include('respa_admin.urls', namespace='respa_admin')),
    path('i18n/', include('django.conf.urls.i18n')),
    path('accounts/', include('allauth.urls')),
    path('grappelli/', include('grappelli.urls')),
    path('resource_image/<int:pk>', ResourceImageView.as_view(), name='resource-image-view'),
    path('v1/', include(router.urls)),
    re_path(r'v1/reservation/ical/(?P<ical_token>[-\w\d]+).ics$', ICalFeedView.as_view(), name='ical-feed'),
    re_path(r'api(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'api/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('', RedirectView.as_view(url='v1/'))
]

if 'reports' in settings.INSTALLED_APPS:
    from reports.api import DailyReservationsReport, ReservationDetailsReport
    urlpatterns.extend([
        path('reports/daily_reservations/', DailyReservationsReport.as_view(), name='daily-reservations-report'),
        path('reports/reservation_details/', ReservationDetailsReport.as_view(), name='reservation-details-report'),
    ])

if settings.RESPA_PAYMENTS_ENABLED:
    from payments import urls as payment_urls  # noqa
    urlpatterns.extend([
        path('payments/', include(payment_urls))
    ])
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
