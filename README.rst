=========================
``gs.group.type.support``
=========================
~~~~~~~~~~~~~~~~~~~~~~~~~~
Support for support groups
~~~~~~~~~~~~~~~~~~~~~~~~~~

:Author: `Michael JasonSmith`_
:Contact: Michael JasonSmith <mpj17@onlinegroups.net>
:Date: 2014-10-14
:Organization: `GroupServer.org`_
:Copyright: This document is licensed under a
  `Creative Commons Attribution-Share Alike 4.0 International License`_
  by `OnlineGroups.Net`_.

Introduction
============

Support groups in GroupServer_ provide a central contact point
for people that have problems to contact someone who can provide
some help. Like normal groups, it allows many people to be
contacted by sending a message to one email address. Unusually,
*non* *members* and those without a profile can send messages to
a support group; only blocked members are prevented from posting
to the support group. The privacy of a support group is fixed to
secret, so only the members can view the group and posts.

This product provides a `marker interface`_ to mark the group as
a support group, a *set* class and an *unset* class to `change
the group type`_, and a `change privacy`_ page. However, no
can-post rules [#canpost]_ are provided (unusually for a
``gs.group.type.*`` product).

Marker interface
================

The ``gs.group.type.support.IGSSupportGroup`` marker interface is
used to explicitly mark a group as a support group. This marker
interface has the following inheritance tree::

  gs.group.base.interfaces.IGSGroupMarker
      △
      │
  gs.group.type.support.IGSSupportGroup

Change the group type
=====================

The class ``gs.group.type.support.set.SetSupportGroup`` provides
the code to change a group to a support group [#set]_. It changes
the reply-to for the list, alters the `marker interface`_ to make
it a support group, and sets the correct privacy (allowing
everyone to post but only group members to view the group and
posts).

The class ``gs.group.type.support.set.UnsetSupportGroup``
*unsets* the group. However, the privacy is never changed back,
so it will remain *Secret* until the site administrator
explicitly changes the privacy.

Change privacy
==============

The *Change privacy* is overwritten by this product, to prevent
the site administrator from changing the privacy, effectively
locking the privacy on *secret*. The reason for this is that
support groups tend to collect spam, because anyone is allowed to
post. Showing spam on a site makes the site look like a
spam-source, so search engines treat the site as a low-quality
information source.

While an argument could be made to restrict a support group to
*private* or secret, it was expedient to ensure the group is just
secret.

Resources
=========

- Code repository:
  https://github.com/groupserver/gs.group.type.support
- Translations:
  https://www.transifex.com/projects/p/gs-group-type-support/
- Questions and comments to
  http://groupserver.org/groups/development
- Report bugs at https://redmine.iopen.net/projects/groupserver

.. [#canpost] See ``gs.group.member.canpost`` for more information:
              <https://github.com/groupserver/gs.group.member.canpost/>

.. [#set] See ``gs.group.type.set`` for more information:
          <https://github.com/groupserver/gs.group.type.set/>
   
.. _GroupServer: http://groupserver.org/
.. _GroupServer.org: http://groupserver.org/
.. _OnlineGroups.Net: https://onlinegroups.net
.. _Michael JasonSmith: http://groupserver.org/p/mpj17
..  _Creative Commons Attribution-Share Alike 4.0 International License:
    http://creativecommons.org/licenses/by-sa/4.0/

