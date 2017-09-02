from django.test import TestCase
from django.conf.urls import url
from accounts.views import (login_view, register_view )
urlpatterns =[

    url('r,^$',login_view),
    url('r,^$',register_view),

]
# Create your tests here.
