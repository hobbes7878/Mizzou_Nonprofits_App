from balance_sheets.models import Revenue_Expense
from django.shortcuts import render_to_response

def index(request):
	all_line_items=Revenue_Expense.objects.all()

	return render_to_response('index.html', {'all_line_items':all_line_items})