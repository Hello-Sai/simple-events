from django.urls import path,include
from .views import  DetailView, RegistrationViewset,EventsViewset
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
'''This API is used to register an event to a participant'''

router.register('register_event',RegistrationViewset)

''' This API retrieves the list of all events created'''

router.register('list_events',EventsViewset)

urlpatterns = [
    # This api retreives the particular event details
    path('event_detail/<pk>',DetailView.as_view()),
    path('',include(router.urls))
]