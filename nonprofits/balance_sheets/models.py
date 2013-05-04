from django.db import models

class Balance_Sheet(models.Model):
	rowid = models.AutoField(primary_key=True)
	ein = models.CharField(max_length=20)
	nonprof_name = models.CharField(max_length=200)
	category = models.CharField(max_length=200)
	fiscal_date = models.CharField(max_length=200)
	amount = models.DecimalField(max_digits=20, decimal_places=2)

    # We're using this to hook up to the crime_data table we already created
	class Meta:
		db_table = 'balance_sheet_data'

    # The __unicode__ method defines how an individual instance of this class
    # will represent itself as a string.
	def __unicode__(self):
		return self.ein + " : "+self.category

class Revenue_Expense(models.Model):
	rowid = models.AutoField(primary_key=True)
	ein = models.CharField(max_length=20)
	nonprof_name = models.CharField(max_length=200)
	category = models.CharField(max_length=200)
	fiscal_date = models.CharField(max_length=200)
	amount = models.DecimalField(max_digits=20, decimal_places=2)

    # We're using this to hook up to the crime_data table we already created
	class Meta:
		db_table = 'revenue_expense_data'

    # The __unicode__ method defines how an individual instance of this class
    # will represent itself as a string.
	def __unicode__(self):
		return self.ein + " : "+self.category