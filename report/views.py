from django.shortcuts import render

# Create your views here.
from django.views import View

from report.models import Report


class ReportView(View):
    template_name = 'show_report.html'

    def get(self, request):
        reports = Report.objects.all()
        return render(request, self.template_name, {'reports': reports})
