from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.list_answers, name='home'),
    path('final/', views.user_result, name='final_score'),
    path('register/', views.register, name='register'),
    path('log-in/', views.login_user, name='login_user'),
    path('logout/', views.logout_user, name='logout_user'),
    path('results.', views.list_of_results, name='results'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)