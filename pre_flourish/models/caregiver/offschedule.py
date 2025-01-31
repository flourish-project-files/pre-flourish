from django.forms import forms

from flourish_caregiver.models import CaregiverOffSchedule
from pre_flourish.models.caregiver.pre_flourish_consent import PreFlourishConsent


class CaregiverOffSchedule(CaregiverOffSchedule):
    @property
    def latest_consent_obj_version(self):
        subject_consents = PreFlourishConsent.objects.filter(
            subject_identifier=self.subject_identifier, )
        if subject_consents:
            latest_consent = subject_consents.latest('consent_datetime')
            return latest_consent.version
        else:
            raise forms.ValidationError('Missing Subject Consent form, cannot proceed.')
