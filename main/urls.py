from django.urls import path

from . import views

urlpatterns = [
    path('', views.log_in),
    path('mainpage/', views.mainpage),
    path('TagView/', views.tagview),
    path('NewTag/', views.newtag),
    path('saveTAG/', views.savetag),
    path('ArticleView/', views.articleview),
    path('NewArticle/', views.newarticle),
    path('saveARTICLE/', views.savearticle),
    path('login/', views.auth_user),
    path('deletetag/<int:id>/', views.deletetag,),
    path('updatetagpage/<int:id>', views.updatetag),
    path('saveupdatetag/<int:id>', views.saveupdatetag),
    path('deletearticle/<int:id>/', views.deletearticle, ),
    path('updatearticlepage/<int:id>/', views.updatearticle),
    path('saveupdatearticle/<int:id>', views.saveupdatearticle),
]
