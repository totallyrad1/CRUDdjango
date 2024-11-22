from django.contrib import admin
from django.urls import path, include
from .views import ItemList, ItemDetail, LocationList, LocationDetail

urlpatterns = [
    path('item/', ItemList.as_view()),
    path('item/<int:pk>', ItemDetail.as_view()),
    path('location/', LocationList.as_view()),
    path('item/<int:pk>', LocationDetail.as_view()),
]