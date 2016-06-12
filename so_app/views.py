from django.shortcuts import render
from django.views.generic import View
from models import StackOverflowTagsInfo
from plot import plot_data


class HomeView(View):
    """
    View for landing page
    """

    def get(self, request, *args, **kwargs):
        tags = StackOverflowTagsInfo.objects.all()
        if tags:
            div1, div2 = plot_data(tags)
            return render(request, 'index.html', {'div1': div1, 'div2': div2})
        return render(request, 'index.html')
