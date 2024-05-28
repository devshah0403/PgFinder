from django.urls import path
from owner import owner_views
from django.contrib import admin
from django.urls import include,re_path as url

from owner.owner_views import ChartData
from pg.views import HomeView

urlpatterns = [
    path('show/',owner_views.show),
    path('error/',owner_views.error),
    path('user/<int:id>',owner_views.usershow),
    path('owner/',owner_views.ownershow),
    path('cat/',owner_views.catshow),
    path('feedback/<int:id>',owner_views.showFeed),
    path('feed_delete/<int:id>', owner_views.destroyFeed),
    path('pgfacility/', owner_views.showPgfacility),
    path('wishlist/',owner_views.showWishlist),
    path('cat_update/<int:id>', owner_views.updateCat),
    path('cat_delete/<int:id>', owner_views.destroyCat),
    path('cat_insert/',owner_views.insertCat),
    path('pg/',owner_views.pgshow),
    path('pg_update/<int:id>', owner_views.updatePg),
    path('pg_delete/<int:id>', owner_views.destroyPg),
    path('pgimgedit/<int:id>',owner_views.showimgedit),
    path('pgimgupd/<int:id>',owner_views.updimg),
    path('enqshow/',owner_views.enquiry_show),
    path('res/<int:id>',owner_views.response),
    path('send/<int:id>',owner_views.send_res),

    path('pg_insert/',owner_views.insertPg),
    path('area/',owner_views.areashow),
    path('facility/',owner_views.facilityshow),

    path('facility_insert/',owner_views.insertFacility),

    path('facility_delete/<int:id>', owner_views.destroyFacility),
    path('facility_update/<int:id>', owner_views.updateFacility),

    path('add/<int:id>',owner_views.add_pgfac),
    path('ins_pgfac/<int:id>',owner_views.ins_pgfac),

    path('oprofile/',owner_views.o_profile),
    path('o_logout/',owner_views.ownerLogout),
    path('book/',owner_views.bookshow),

    path('accept/<int:id>',owner_views.accept_order),
    path('reject/<int:id>',owner_views.reject_order),

    path('acc_avail/<int:id>',owner_views.accept_avail),
    path('rej_avail/<int:id>',owner_views.reject_avail),
    path('acc_pay/<int:id>',owner_views.acc_pay),
    path('rej_pay/<int:id>',owner_views.rej_pay),

    path('o_dashboard/',owner_views.o_dashboard),

    path('d_accept/<int:id>',owner_views.d_accept_order),
    path('d_reject/<int:id>',owner_views.d_reject_order),
    path('d_acc_pay/<int:id>', owner_views.d_acc_pay),
    path('d_rej_pay/<int:id>', owner_views.d_rej_pay),

    url(r'home', HomeView.as_view(), name='home'),
    url(r'^api/chart/data/$', ChartData.as_view(), name='api-data'),
    ]