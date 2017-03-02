from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


import logging
logger = logging.getLogger(__package__)


class SpaView(LoginRequiredMixin, TemplateView):
    """
    Load single-page-app waterfall.js from static files

    See frontend/ for the SPA sources
    """
    template_name = 'annotations/index.html'
