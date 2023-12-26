from django.urls import path
from .views import ListBlogView

urlpatterns=[

    path('',ListBlogView.as_view(),name='blog'),
]