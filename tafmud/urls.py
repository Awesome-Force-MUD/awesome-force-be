# END POINTS ARE DEFINED HERE

from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from tafmudapp.api import PlayerSerializerViewSet, RoomSerializerViewSet

# views is the django auth boiler plate given to us
from rest_framework.authtoken import views

# create a new router for our players
router = routers.DefaultRouter()
# register the player endpoint NAME aka URL with our players view set
router.register('player', PlayerSerializerViewSet)
# register a room endpoint 
router.register('room', RoomSerializerViewSet)
# register a world endpoint
# router.register('world', )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)), # ~~> gives us access to our api/player end point
    # LOGIN POINT FO FE
    path('api-token-auth/', views.obtain_auth_token), # ~~> pass obtain auth token out of views when decalring new path
]
