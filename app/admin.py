# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import *


class ExpenseAdmin(admin.ModelAdmin):
	list_filter = ['date']
	search_fields = ['purpose']
	list_display = ['purpose', 'amount']


admin.site.register(Expense, ExpenseAdmin),



