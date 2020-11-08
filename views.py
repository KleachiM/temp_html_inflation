import csv

from django.shortcuts import render

def inflation_view(request):
    template_name = 'inflation.html'
    to_context = []
    with open('inflation_russia.csv') as f:
        from_csv = csv.DictReader(f, delimiter=";")
        for row in from_csv:
            to_context.append(row)
            for month in row:
                if row[month] and month != 'Год':
                    row[month] = float(row[month])
        fields = from_csv.fieldnames
    context = {'years': to_context,
               'fields': fields
               }

    return render(request, template_name,
                  context)