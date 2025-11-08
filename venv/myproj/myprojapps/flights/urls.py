from django.urls import path
from . import views
urlpatterns = [
    path("", views.FlightsView.as_view()),
    path('tflight/', views.flightT),
    path('show/', views.show),
    path('edit/<int:id>', views.edit),
    path('update/<int:id>', views.update),
    path('delete/<int:id>', views.destroy),
]