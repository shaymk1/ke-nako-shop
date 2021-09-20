

from django.urls import path
# from store import views as store_views
from . import views


urlpatterns = [
   
    path('<slug:category_slug>/', views.fetching_products_by_category,
         name="products_by_category"),
    



    
]
