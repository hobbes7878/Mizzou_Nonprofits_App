from balance_sheets.models import Revenue_Expense
from balance_sheets.forms import category_select
from django.shortcuts import render_to_response

def index(request):

	form = category_select()
	form.Category

	all_line_items=Revenue_Expense.objects.filter()

	return render_to_response('index.html', {'form':form,  'all_line_items':all_line_items})