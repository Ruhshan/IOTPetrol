from django.shortcuts import render

# Create your views here.
from django.views import View

from report.models import Sale


class ReportView(View):
    template_name = 'report/show_report.html'

    def get(self, request):
        reports = Sale.objects.all()
        return render(request, self.template_name, {'reports': reports})


