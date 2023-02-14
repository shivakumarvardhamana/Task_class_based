from django.urls import path,include
from .views import blog_api,likes_api,user_api,user_owner

from rest_framework.routers import DefaultRouter
router=DefaultRouter()
import rest_framework
# router.register('api',blog_api,basename="api")
# router.register('api1',likes_api,basename="api1")
# router.register('api2',user_api,basename="api2")
router.register('api4',user_owner,basename="api4")
urlpatterns=[
    path('',include(router.urls)),
    path('api',include('rest_framework.urls')),

]