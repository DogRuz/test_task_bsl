from django.conf.urls import url

from test_task.views import get_status, add_balance, subtraction_balance, get_info_person

urlpatterns = [
    url(r'^ping/?$', get_status),
    url(r'^add/?$', add_balance),
    url(r'^substract/?$', subtraction_balance),
    url(r'^status/?$', get_info_person),
]