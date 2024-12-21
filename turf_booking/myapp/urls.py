

from django.urls import path
from .views import *


urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    # ///////////////////////////// ADMIN ///////////////////////////////////////

    path('turfowner/', Turfowners.as_view(), name='turfowner'),
    path('complaints/', Complaints.as_view(), name='complaints'),
    path('reply/<int:c_id>',reply.as_view(), name='reply'),
    path('accept_turf/<int:t_id>', accept_turf.as_view(),name='accept_turf'),
    path('reject_turf/<int:t_id>', reject_turf.as_view(),name='reject_turf'),
    path('Users/',Users.as_view(), name='users'),
    path('Addmanagment/',Addmanagment.as_view(), name='addmanagment'),
    path('Viewbooking/',Viewbooking.as_view(), name='viewbooking'),
    path('viewequipment/',viewequipment.as_view(), name='viewequipment'),
    path('viewfeedback/',Viewfeedback.as_view(), name='viewfeedbavck'),
    path('adminhome/',Adminhome.as_view(), name='adminhome'),
    path('addequipment/',addequipment.as_view(), name="addequipment"),
    path('editequipment/<int:id>',editequipment.as_view(),name='editequipment'),

    # ///////////////////////////// OWNER ///////////////////////////////////////

    path('',viewlogin.as_view(),name="Login"),
    path('manageequips',manageequips.as_view(), name='manageequips'),  
    path('deleteequipment/<int:id>',deleteequipment.as_view(), name='deleteequipment'),
    path('turfownerhome', turfownerhome.as_view(), name='turfownerhome'),
    path('turf_complaint/', turf_complaint.as_view(), name='turf_complaint'),
]
