# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from .models import *
from .forms import *


def new_expense(request):
	if request.method == 'POST':
		form = ExpenseForm(request.POST)
		form.save()
		return redirect('expense_list')
	else:
		form = ExpenseForm()	
	return render(request, 'expense/new_expense.html', {'form': form})


def expense_list(request):
	expenses = Expense.objects.all().order_by('-date')
	return render(request, 'expense/expense_list.html', {'expenses': expenses})


def update_expense(request, pk):
	expense = Expense.objects.get(pk=pk)
	if request.method == 'POST':
		form = ExpenseForm(request.POST, instance=expense)
		form.save()
		return redirect('expense_list')
	else:
		form = ExpenseForm(instance=expense)	
	return render(request, 'expense/update_expense.html', {'form': form})


def delete_expense(request, pk):
	expense = Expense.objects.get(pk=pk)
	expense.delete()
	return redirect('expense_list')		

