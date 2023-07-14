"""
URL configuration for zd_note project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from . import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    # 需要添加app_name
    path('search/', include('search.urls', namespace='search')),
    path('update_notice/', include('update_notice.urls', namespace='update_notice')),
    path('user/', include('user.urls', namespace='user')),
    path('', include('web.urls', namespace='web')),
    # path('jobs/', include('jobs.urls', namespace='jobs')),

    # path('search/', include(('search.urls', 'search'), namespace='search')),
    # path('update_notice/', include(('update_notice.urls', 'update_notice'), namespace='update_notice')),
    # path('user/', include(('user.urls', 'user'), namespace='user')),
    # path('', include(('web.urls', 'web'), namespace='web')),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # 开发期间提供media
