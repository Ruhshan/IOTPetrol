from django.conf.urls import url, include

from .views import *
from .api import *
urlpatterns = [
    
    url(r"view/", ReportView.as_view()),
    url(r'api/list', SaleListApi.as_view()),
]
