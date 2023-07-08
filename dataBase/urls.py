from django.contrib import admin
from django.urls import path
from . import views 
from .views import getCreate,GetEpisodes

urlpatterns = [
    path('get_most_view/',views.get_most_view ,name="k"),
    path('getCreatte/', getCreate.as_view()),
    path('GetEpisodes/<int:show_id>', GetEpisodes.as_view()),
    path('getMostPopularShow/', views.getMostPopular),
    path('getStarplus/', views.getStarplus),
    path('verifyUserr/', views.user_vrify),
    path('getStarBharat/', views.getStarBharat),
    path('getSlide/', views.getSlide),
    path('register/', views.add_user),
    path('add_update/', views.add_update,name="add_updat")
]

from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
