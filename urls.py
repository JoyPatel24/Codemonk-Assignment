from django.conf.urls import url
from EmployeeApp import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[

    url(r'^user$',views.employeeApi),
    url(r'^user/([0-9]+)$',views.employeeApi),

    url(r'^user/savefile',views.SaveFile)
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)