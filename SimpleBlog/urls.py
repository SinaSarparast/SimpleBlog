"""SimpleBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('profile/', include('user.urls')),
    path('articles/', include('articles.urls')),
    path('admin/', admin.site.urls),
    path(r'^ckeditor/', include('ckeditor_uploader.urls'))
    ]

# serving media files only on debug mode
# see: https://docs.djangoproject.com/en/3.1/ref/urls/#django.conf.urls.static.static
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Other way of serving media files in debug mode
# see: https://docs.djangoproject.com/en/3.1/ref/views/#serving-files-in-development
# from django.views.static import serve
# if settings.DEBUG:
#     urlpatterns += [
#         path(r'^media/(?P<path>.*)$', serve,
#             {'document_root': settings.MEDIA_ROOT}
#             )]
