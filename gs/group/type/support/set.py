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
from zope.component import createObject
from gs.group.type.set import (SetABC, UnsetABC)
from gs.group.privacy.interfaces import IGSChangePrivacy


class SetSupportGroup(SetABC):
    'Set a group folder to be a support group'
    name = 'Support group: non-members can post, but only members can '\
           'see the group'
    weight = 30
    show = True

    def set(self):
        self.set_marker()
        self.set_secret()
        self.set_list_property('unclosed', 1, 'boolean')
        self.set_list_property('replyto', 'sender')

    def set_marker(self):
        '''Add the marker-interface to make the group into a support
        group.'''
        iFaces = ['gs.group.type.support.interfaces.IGSSupportGroup']
        self.add_marker(self.group, iFaces)

    def set_secret(self):
        'Support groups should always be private'
        groupInfo = createObject('groupserver.GroupInfo', self.group)
        changer = IGSChangePrivacy(groupInfo)
        changer.set_group_secret()


class UnsetSupportGroup(UnsetABC):
    name = 'Support group'
    setTypeId = 'gs-group-type-support-set'

    def unset(self):
        self.unset_marker()
        self.del_list_property('unclosed')
        self.del_list_property('replyto')

    def unset_marker(self):
        iFaces = ['gs.group.type.support.interfaces.IGSSupportGroup']
        self.del_marker(self.group, iFaces)
