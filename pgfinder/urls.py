"""pgfinder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

import client
import pg
from pg import views,forms
from client import client_views

#from django.conf.urls import url
from django.contrib import admin
from django.urls import include,re_path as url

from pg.views import HomeView,ChartData

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',pg.views.index),
    path('usershow/',pg.views.showUser),
    path('dashboard/',pg.views.dashboard),
    path('userinsert/',pg.views.insertUser),
    path('userdelete/<int:id>',pg.views.destroyUser),
    path('userupdate/<int:id>',pg.views.updateUser),
    path('userselect/<int:id>',pg.views.selectUser),
    path('ownershow/',pg.views.showOwner),
    path('ownerinsert/',pg.views.insertOwner),
    path('ownerdelete/<int:id>',pg.views.destroyOwner),
    path('ownerupdate/<int:id>', pg.views.updateOwner),
    path('ownerselect/<int:id>', pg.views.selectOwner),
    path('catshow/',pg.views.showCat),
    path('catdelete/<int:id>',pg.views.destroyCat),
    path('catinsert/',pg.views.insertCat),
    path('catupdate/<int:id>', pg.views.updateCat),
    path('catselect/<int:id>', pg.views.selectCat),
    path('login/',pg.views.adminLogin),
    path('logout/',pg.views.adminLogout),
    path('profile/',pg.views.profile),
    path('forgot_password/',pg.views.forgot),
    path('send_otp/',pg.views.sendotp),
    path('pass/',pg.views.set_password),
    path('pgshow/',pg.views.showPg),
    path('pginsert/',pg.views.insertPg),
    path('pgdelete/<int:id>',pg.views.destroyPg),
    path('pgselect/<int:id>',views.selectPg),
    path('pgupdate/<int:id>',views.updatePg),
    path('test/',views.show1),
    path('bookshow/',views.showBook),
    path('report1/',views.report_1),
    path('report2/',views.report_2),
    path('report3/',views.report_3),
    path('pg_imgedit/<int:id>',views.showimgedit),
    path('pg_imgupd/<int:id>',views.updimg),



    #======================================
    url(r'home', HomeView.as_view(), name='home'),
    url(r'^api/chart/data/$', ChartData.as_view(),name='api-data'),
    #url(r'^admin/', admin.site.urls)








    path('areashow/',pg.views.showArea),
    path('areainsert/',pg.views.insertArea),
    path('areadelete/<int:id>',pg.views.destroyArea),
    path('areaupdate/<int:id>',pg.views.updateArea),
    path('facilityshow/', pg.views.showFacility),
    path('facilityinsert/', pg.views.insertFacility),
    path('facilitydelete/<int:id>', pg.views.destroyFacility),
    path('facilityupdate/<int:id>', pg.views.updateFacility),
    path('feedshow/', pg.views.showFeed),
    path('feeddelete/<int:id>', pg.views.destroyFeed),
    path('pgfacilityshow/', pg.views.showPgfacility),
    path('404/',pg.views.error),

    path('client/', include('client.client_urls')),
    path('owner/', include('owner.owner_urls')),
]

