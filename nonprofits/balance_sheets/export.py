import csv
from django.http import HttpResponse


def export_to_csv(request):
	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = 'attachment;filename="export.csv"'

	writer = csv.writer(response)

	return response
