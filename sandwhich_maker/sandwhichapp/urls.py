from django.urls import path 
from sandwhichapp.views import SandwhichappView, IngredientsListView, SandwichGeneratorView

urlpatterns = [
    # sandwhich
    path('', SandwhichappView.as_view(), name='sandwhich'),
    path('ingredients/<str:ingredient_type>', IngredientsListView.as_view(), name='ingredients_list'),
    path('random', SandwichGeneratorView.as_view(), name='sandwich_generator'),
]