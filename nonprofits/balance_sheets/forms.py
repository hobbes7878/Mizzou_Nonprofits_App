from django import forms
from balance_sheets.models import Revenue_Expense


choices=[("Default","Select a category")]
categories=Revenue_Expense.objects.values('category').distinct()

#Create choices tuples
for cat in categories:
	choice=(cat['category'],cat['category'])
	choices.append(choice)



class category_select(forms.Form):
	Category = forms.ChoiceField(choices=choices)
	Min_Amount=forms.IntegerField()
