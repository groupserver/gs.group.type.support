# coding=utf-8
from zope.component import createObject, getMultiAdapter
from gs.group.base.page import GroupPage
from gs.group.member.canpost.interfaces import IGSPostingUser

class PostingRules(GroupPage):
    
    def rules(self):
        canPost = getMultiAdapter((self.loggedInUserInfo, self.context), 
                    IGSPostingUser)
        retval = canPost.rules
        return retval

