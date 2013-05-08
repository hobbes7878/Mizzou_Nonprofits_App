from balance_sheets.models import Revenue_Expense
from balance_sheets.forms import category_select
from django.shortcuts import render_to_response
from django.db.models import Q

import csv

def index(request):

	form = category_select()
	cat_query= request.GET.get('Category','')
	year_query=request.GET.get('Fiscal_Year','')
	amt_query=request.GET.get('Min_Amount',1)
	
	if cat_query or year_query or amt_query:
		qset = (
			Q(category=cat_query) &
			Q(fiscal_date=year_query) &
			Q(amount__gt=amt_query) 
			)
		all_line_items=Revenue_Expense.objects.filter(qset)
	else:
		all_line_items=Revenue_Expense.objects.all()

	# all_line_items=Revenue_Expense.objects.filter()

	return render_to_response('index.html', {'form':form,  'all_line_items':all_line_items})