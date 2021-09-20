

from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('shop/', views.shop, name="shop"),
    # to show product by category:
    # path('<slug:category_slug>/', views.shop, name="products_by_category"),





]
