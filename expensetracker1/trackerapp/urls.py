from django.urls import path
from . import views


urlpatterns=[
   path("",views.index,name='index'),
   path("signup/",views.signup,name='signup'),
   # path("<emailid>/wallet/",views.wallet, name='wallet'),
   path("wallet/",views.wallet, name='wallet'),

]
