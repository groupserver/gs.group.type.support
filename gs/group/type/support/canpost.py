# coding=utf-8
from operator import and_
from zope.cachedescriptors.property import Lazy
from zope.component import adapts, getGlobalSiteManager, getAdapters
from zope.interface import implements, providedBy
from Products.CustomUserFolder.interfaces import IGSUserInfo
from gs.group.member.canpost.interfaces import IGSPostingUser, IGSCanPostRule
from interfaces import IGSSupportGroup

class CanPostToSupport(object):
    def __init__(self, userInfo, supportGroup):
        self.userInfo = userInfo
        self.group = supportGroup

    @Lazy
    def rules(self):
        gsm = getGlobalSiteManager()
        retval =  [instance for name, instance in 
                    gsm.getAdapters((self.userInfo, self.group), 
                                    IGSCanPostRule)]
        retval.sort(key=lambda r:r.weight)
        return retval
    
    @Lazy
    def canPost(self):
        return reduce(and_, [rule.canPost for rule in self.rules], True)
    
    @Lazy
    def statusNum(self):
        statusNums = [rule.statusNum for rule in self.rules 
                        if rule.statusNum != 0]
        retval = (statusNums and min(statusNums)) or 0
        assert retval >= 0
        return retval
    
    @Lazy
    def status(self):
        retval = [rule.status for rule in self.rules 
                    if rule.statusNum == self.statusNum][0]
        return retval

