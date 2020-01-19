from django.urls import path,include
from . import views
from rest_framework import routers

router=routers.DefaultRouter()
router.register('api',views.ApprovalsView)
urlpatterns = [
    path('form/',views.cxcontact,name='myform'),
    path('api/',include(router.urls)),
    path('status/',views.approvereject)
]