from django.conf.urls import url, include
from .views import *


urlpatterns = [
	# Expense CRUD
    url(r'^new_expense/', new_expense, name='new_expense'),
    url(r'^expense_list/', expense_list, name='expense_list'),
    url(r'^edit/(?P<pk>[0-9]+)/', update_expense, name='update_expense'),
    url(r'^delete/(?P<pk>[0-9]+)/', delete_expense, name='delete_expense'),
]