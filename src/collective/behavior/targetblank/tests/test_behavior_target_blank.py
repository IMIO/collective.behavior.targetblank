# -*- coding: utf-8 -*-
from collective.behavior.targetblank.behaviors.target_blank import ITargetBlankMarker
from collective.behavior.targetblank.testing import COLLECTIVE_BEHAVIOR_TARGETBLANK_INTEGRATION_TESTING  # noqa
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.behavior.interfaces import IBehavior
from zope.component import getUtility

import unittest


class TargetBlankIntegrationTest(unittest.TestCase):

    layer = COLLECTIVE_BEHAVIOR_TARGETBLANK_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])

    def test_behavior_target_blank(self):
        behavior = getUtility(IBehavior, 'collective.behavior.targetblank.target_blank')
        self.assertEqual(
            behavior.marker,
            ITargetBlankMarker,
        )
