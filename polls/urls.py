from django.urls import path

from . import views

urlpatterns = [

    path('', views.index, name='index'),

    path('blog', views.blog, name='blog'),
    
    path('about', views.about, name='about'),

    path('portfolio', views.portfolio, name='portfolio'),
 
    path('contact', views.contact, name='contact'),

    path('<int:product_id>/', views.detail, name='detail'),

    path('<int:product_id>/results/', views.results, name='results'),

    path('<int:product_id>/vote/', views.vote, name='vote'),
]
