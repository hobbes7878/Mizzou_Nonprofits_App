from django import forms
from balance_sheets.models import Revenue_Expense


cat_choices=[]
year_choices=[]
categories=Revenue_Expense.objects.values('category').distinct()
years=Revenue_Expense.objects.values('fiscal_date').distinct()

#Create choices tuples
for cat in categories:
	choice=(cat['category'],cat['category'])
	cat_choices.append(choice)

for year in years:
	choice=(int(year['fiscal_date']), year['fiscal_date'])
	year_choices.append(choice)




class category_select(forms.Form):
	Category = forms.ChoiceField(choices=cat_choices)
	Start_Year = forms.ChoiceField(choices=year_choices, initial="")
	End_Year = forms.ChoiceField(choices=year_choices, initial="2012")
	Min_Amount=forms.IntegerField(initial=0)

