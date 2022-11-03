from django.urls import path
from . import views
 
urlpatterns = [
    path('', views.show),
    path('add/', views.add),
    path('edit/<uuid:id>', views.edit),
    path('update/<uuid:id>', views.update),
    path('delete/<uuid:id>', views.delete),
    path('add_reaction/<slug:reaction_type>/<uuid:movieId>', views.add_reaction),

]