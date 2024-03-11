from django.urls import path
from.import views

urlpatterns =[
    path('',views.index,name='index'),
    path('ad/',views.ad,name='ad'),
    path('movie/<int:movie_id>/',views.detalis,name='detalis'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('update/<int:movie_id>/',views.update,name='update'),
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
]
