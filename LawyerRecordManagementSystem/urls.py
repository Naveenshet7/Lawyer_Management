"""LawyerRecordManagementSystem URL Configuration

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
from django.urls import path
from lawyer.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='index'),
    path('about',about,name='about'),
    path('lawyer',lawyer,name='lawyer'),
    path('lawyerDtls/<int:pid>',lawyerDtls,name='lawyerDtls'),
    path('search', search, name='search'),
    path('view_SearchReports/<int:pid>', view_SearchReports, name='view_SearchReports'),
    path('contact',contact,name='contact'),
    path('admin_login',admin_login,name='admin_login'),
    path('dashboard', dashboard, name='dashboard'),
    path('add_PracticeArea', add_PracticeArea, name='add_PracticeArea'),
    path('manage_PracticeArea', manage_PracticeArea, name='manage_PracticeArea'),
    path('edit_PracticeArea/<int:pid>', edit_PracticeArea, name='edit_PracticeArea'),
    path('delete_PracticeArea/<int:pid>', delete_PracticeArea, name='delete_PracticeArea'),
    path('add_Lawyer', add_Lawyer, name='add_Lawyer'),
    path('manage_Lawyer', manage_Lawyer, name='manage_Lawyer'),
    path('edit_Lawyer/<int:pid>', edit_Lawyer, name='edit_Lawyer'),
    path('delete_Lawyer/<int:pid>', delete_Lawyer, name='delete_Lawyer'),
    path('bwdateReports', bwdateReports, name='bwdateReports'),
    path('searchReport', searchReport, name='searchReport'),
    path('view_Reports/<int:pid>', view_Reports, name='view_Reports'),
    path('changePassword', changePassword, name='changePassword'),
    path('logout', Logout, name='logout')

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
