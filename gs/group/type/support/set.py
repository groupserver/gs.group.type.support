# -*- coding: utf-8 -*-
############################################################################
#
# Copyright © 2014 OnlineGroups.net and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
############################################################################
from __future__ import absolute_import, unicode_literals
from gs.group.type.set import SetABC


class SetSupportGroup(SetABC):
    'Set a group folder to be a support group'
    name = 'Support group'
    typeId = 'gs-group-type-support'
    weight = 30
    show = True

    def set(self):
        '''Add the marker-interface to make the group into a support
        group.'''
        iFaces = ['gs.group.type.support.interfaces.IGSSupportGroup']
        self.add_marker_interfaces(self.group, iFaces)
