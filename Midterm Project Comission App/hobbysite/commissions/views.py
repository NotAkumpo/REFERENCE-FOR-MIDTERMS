from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Commission, Comment


class CommissionListView(ListView):
    model = Commission
    template_name = 'commissions_list.html'

class CommissionDetailView(DetailView):
    model = Comment
    template_name = 'commissions_detail.html'