"""ChartApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import url
from site_builder import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'preview/', views.preview, name='preview'),
    url(r'iupload/', views.iupload, name='iupload'),
    url(r'save/', views.save_html, name='save'),
    url(r'addTheme/', views.add_themes, name='add-themes'),
    url(r'deleteTheme/', views.delete_themes, name='delete-themes')
]
