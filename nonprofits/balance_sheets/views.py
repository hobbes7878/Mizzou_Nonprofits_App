from balance_sheets.models import Revenue_Expense
from django.shortcuts import render_to_response

def index(request):

	categories=Revenue_Expense.objects.values('category').distinct()

	all_line_items=Revenue_Expense.objects.all()

	return render_to_response('index.html', {'categories':categories,  'all_line_items':all_line_items})