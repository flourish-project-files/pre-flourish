import re

from django.db.models import Q
from edc_base.view_mixins import EdcBaseViewMixin
from edc_dashboard.view_mixins import ListboardFilterViewMixin, SearchFormViewMixin
from edc_dashboard.views import ListboardView
from edc_navbar import NavbarViewMixin

from ...model_wrappers import CaregiverChildConsentModelWrapper
from ...model_wrappers.child.child_consent_model_wrapper import ChildConsentModelWrapper


class ChildListboardView(EdcBaseViewMixin, NavbarViewMixin,
                         ListboardFilterViewMixin, SearchFormViewMixin,
                         ListboardView):

    listboard_template = 'pre_flourish_child_listboard_template'
    listboard_url = 'pre_flourish_child_listboard_url'
    listboard_panel_style = 'success'
    listboard_fa_icon = "far fa-user-circle"

    model = 'pre_flourish.preflourishcaregiverchildconsent'
    model_wrapper_cls = CaregiverChildConsentModelWrapper
    navbar_name = 'pre_flourish_dashboard'
    navbar_selected_item = 'child_subjects'
    search_form_url = 'pre_flourish_child_listboard_url'

    def get_queryset_filter_options(self, request, *args, **kwargs):
        options = super().get_queryset_filter_options(request, *args, **kwargs)
        if kwargs.get('subject_identifier'):
            options.update(
                {'subject_identifier': kwargs.get('subject_identifier')})
        return options

    def extra_search_options(self, search_term):
        q = Q()
        if re.match('^[A-Z]+$', search_term):
            q = Q(first_name__exact=search_term)
        return q
