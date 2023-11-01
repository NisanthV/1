from django.urls import path
from . import views
urlpatterns = [
    path('',views.home, name="home"),
    path('account/',views.account, name="account"),
    path('register/',views.create,name="create"),
    path('login/',views.login,name="login"),
    path('check/',views.withdraw, name="withdraw"),
    path('details/',views.details,name="details"),
    path('h/',views.statement,name="statement"),

]
