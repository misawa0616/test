from django.urls import path
from datetimeobj import views


urlpatterns = [
    path('', views.TestDatetimeAPIView.as_view())
]
