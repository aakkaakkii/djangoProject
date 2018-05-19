"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path

from mysite.views import view, login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/', view.article_view, name='home'),
    path('article/<int:article_id>', view.article_view2, name='article_page'),
    path('addArticle/', view.add_article, name='addArticle'),
    path('getData/', view.get_data),
    path('some/', view.get_data, name='some'),
    path('remove/', view.remove, name='remove'),
    path('removeData/', view.remove_data, name='remove_data'),
    path('loadData/', view.load_data, name='load_data'),
    path('login/', login.login_view, name='login'),
    path('logout/', login.logout_view, name='logout'),
    path('register/', login.register_view, name='register')

]
