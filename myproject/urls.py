"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from inicio import views as inicio_views
from django.conf.urls.static import static
from django.conf import settings
from empleados import views as empleados_views

# urls de app inicio
extra_patterns1 = [
    url(r'^login', inicio_views.login_view, name = 'login'),
    url(r'^logout/$', inicio_views.login_out, name = 'logout'),
    url(r'^home/$', inicio_views.home, name = 'home'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urls de app empleados
extra_patterns2 = [
    url(r'^nuevo_empleado', empleados_views.nuevo_empleado, name = 'nuevo_empleado'),
    url(r'^profiles', empleados_views.profiles, name = 'profiles'),
    url(r'^profile/(?P<id_emp>[-A-Za-z0-9_]+)$', empleados_views.profile, name = 'profile'),
    url(r'^editar_empleado/(?P<id_emp>[-A-Za-z0-9_]+)$', empleados_views.editar_empleado, name = 'editar_empleado'),
    url(r'^queue', empleados_views.queue, name = 'queue'),
    url(r'^snapshot', empleados_views.snapshot, name = 'snapshot'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(extra_patterns1)),
    url(r'^', include(extra_patterns2)),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
