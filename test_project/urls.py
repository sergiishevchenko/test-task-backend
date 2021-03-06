"""test_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from test_project.views import init, image_page, add_new_images, image_page_from_list
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('image_page/', image_page, name='image_page'),
    path('image_page/<int:id>', image_page_from_list, name='image_page_from_list'),
    path('add_new_images', add_new_images, name='add_new_image'),
    path('', init, name='init')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
