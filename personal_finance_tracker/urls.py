"""personal_finance_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import re_path
from expenses_app import views as expenses_view
from home_app import views as home_view
from debt_app import views as debt_view

urlpatterns = [
    re_path('admin/', admin.site.urls),
    re_path('expenses/',expenses_view.expenses, name='my expenses'),
    re_path('debt/',debt_view.debt, name='my debt'),
    re_path(r'^$', home_view.home, name='home'),
]

admin.site.site_header = "Budget Admin Panel"
admin.site.site_title = "Budget Admin Panel"
admin.site.index_title = ""