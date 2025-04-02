from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), # الصفحة الرئيسية
    path('simple/query', views.simple_query, name='simple_query'),  
    path('complex/query', views.complex_query, name='complex_query'),  

    
    path('list_books/', views.list_books, name='books.list_books'),
    path('viewbook/<int:bookId>/', views.viewbook, name='viewbook'),
    path('aboutus/', views.aboutus, name='books.aboutus'),
    path('links/', views.links, name='books.links'),
    path('formatting/', views.formatting, name='books.formatting'),
    path('listing/', views.listing, name='books.listing'),
    path('tables/', views.tables, name='books.tables'),
    path('search/', views.search, name='books.search'),

]
