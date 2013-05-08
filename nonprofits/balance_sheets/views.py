from balance_sheets.models import Revenue_Expense
from balance_sheets.forms import category_select
from balance_sheets.export import export_to_csv
from django.shortcuts import render_to_response
from django.db.models import Q



def index(request):

	form = category_select()
	
	cat_query= request.GET.get('Category','')
	start_year_query=request.GET.get('Start_Year','')
	end_year_query=request.GET.get('End_Year','')
	amt_query=request.GET.get('Min_Amount',1)
	
	if cat_query:
		qset = (
			Q(category=cat_query) &
			(Q(fiscal_date__gte=start_year_query) & Q(fiscal_date__lte=end_year_query)) &
			Q(amount__gt=amt_query) 
			)
		all_line_items=Revenue_Expense.objects.filter(qset).order_by('-amount')
	else:
		all_line_items=[]

	return render_to_response('index.html', {'form':form,  'all_line_items':all_line_items})


#I have no idea how to hook this up...
