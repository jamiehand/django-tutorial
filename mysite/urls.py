"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^polls/', include('polls.urls', namespace="polls")),  # Namespacing URL names allows the project to
        # distinguish betw. apps. (Add namespaces to my root URLconf. Also change in polls/templates/polls/index.html!)
    url(r'^admin/', include(admin.site.urls)),  # Why is the above in quotes and this one not in quotes?
        # Not sure if this applies here:
        # {% extends "base.html" %} (with quotes) uses the literal value "base.html" as the name of the parent
        # template to extend.
        # {% extends variable %} uses the value of variable. If the variable evaluates to a string, Django will use that
        # string as the name of the parent template. If the variable evaluates to a Template object, Django will use
        # that object as the parent template.
        # (https://docs.djangoproject.com/en/1.8/ref/templates/builtins/)
]
