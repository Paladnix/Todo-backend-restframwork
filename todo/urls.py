from django.conf.urls import url
from views import *

urlpatterns = [
        url(r'^user/', User.as_view() ),

        # get
        url(r'^task/list/', TaskList.as_view(), name='TaskList'),
        # put
#        url(r'^task/update/(?P<pk>\w+)', TaskUpdate.as_view(), name='TaskUpdate' ),

        # post
        url(r'^task/add/', TaskAdd.as_view(), name='TaskAdd' ),

]



