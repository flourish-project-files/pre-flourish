from edc_action_item import Action, site_action_items, HIGH_PRIORITY

from edc_locator.action_items import SubjectLocatorAction

MATERNAL_OFF_STUDY_ACTION = 'submit-pf-caregiver-study'
CHILD_OFF_STUDY_ACTION = 'submit-pf-child-study'
PRE_FLOURISH_CAREGIVER_LOCATOR_ACTION = 'submit-pf-caregiver-locator'


class MaternalOffStudyAction(Action):
    name = MATERNAL_OFF_STUDY_ACTION
    display_name = 'Submit Pre Flourish Caregiver Offstudy'
    reference_model = 'pre_flourish.preflourishoffstudy'
    admin_site_name = 'pre_flourish_admin'
    priority = HIGH_PRIORITY
    singleton = True

class ChildOffStudyAction(Action):
    name = CHILD_OFF_STUDY_ACTION
    display_name = 'Submit Pre Flourish Child Offstudy'
    reference_model = 'pre_flourish.preflourishchildoffstudy'
    admin_site_name = 'pre_flourish_admin'
    priority = HIGH_PRIORITY
    singleton = True


class PreFlourishCaregiverLocatorAction(SubjectLocatorAction):
    name = PRE_FLOURISH_CAREGIVER_LOCATOR_ACTION
    display_name = 'Submit Pre Flourish Caregiver Locator'
    reference_model = 'pre_flourish.preflourishcaregiverlocator'
    admin_site_name = 'pre_flourish_admin'


site_action_items.register(PreFlourishCaregiverLocatorAction)
site_action_items.register(ChildOffStudyAction)
site_action_items.register(MaternalOffStudyAction)
