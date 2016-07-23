from django.conf.urls import patterns, url
from drip import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    # url(r'^$', views.Provider.as_view()),
    url(r'^user/?$', views.UserView.as_view()),
    url(r'^remind/?$', views.SendReminder.as_view()),
    
    
    
]