# from . import views
# from django.urls import path
#
# urlpatterns = [
#
#     path('',views.demo,name='demo')
# ]
from travelproject import settings
from django.conf.urls.static import static
from django.urls import path
from . import views


urlpatterns = [
    path('',views.demo,name='demo'),
    # path('',views.dem,name='dem')


]
if settings.DEBUG:
   urlpatterns+=static(settings.STATIC_URL,
               document_root=settings.STATIC_ROOT)
   urlpatterns+=static(settings.MEDIA_URL,
               document_root=settings.MEDIA_ROOT)

