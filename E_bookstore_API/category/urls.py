from django.urls import path
from .views import CategoryList , CategoryNames , FeaturedBooks

urlpatterns = [
    path('', CategoryNames.as_view(), name='category-names'),
    path('<str:name>/', CategoryList.as_view(), name='category-list'),
    path('featured/', FeaturedBooks.as_view(), name='featured-books')

]
