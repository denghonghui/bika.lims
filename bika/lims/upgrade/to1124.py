import logging
from Acquisition import aq_base
from Acquisition import aq_inner
from Acquisition import aq_parent
from Products.CMFCore import permissions
from bika.lims.permissions import *
from Products.CMFCore.utils import getToolByName


def upgrade(tool):
    """ New policy maps for entities versioning
    """
    portal = aq_parent(aq_inner(tool))
    setup = portal.portal_setup
    wf = portal.portal_workflow

    setup.runImportStepFromProfile('profile-bika.lims:default', 'repositorytool')
    wf.updateRoleMappings()

    return True
