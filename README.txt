Introduction
============

Support groups in GroupServer_ provide a central contact point for people
that have problems to contact someone who can provide some help. Like
normal groups, it allows many people to be contacted by sending a message
to one email address. Unusually, *non* *members* and those without a
profile can send messages to a support group; only blocked members are
prevented from posting to the support group. Normally the privacy of the
support group set to secret or private, so only the members can view the
posts.

This product provides a `marker interface`_ to mark the group as a support
group. However, no pages, viewlets, nor any can-post rules [#canpost]_ are
provided (unusually for a ``gs.group.type`` egg).

Marker Interface
================

The ``gs.group.type.support.IGSSupportGroup`` marker interface is used to
explicitly mark a group as a support group. This marker interface has the
following inheritance tree::

  gs.group.base.interfaces.IGSGroupMarker
      △
      │
  gs.group.type.support.IGSSupportGroup

Resources
=========

- Code repository: https://source.iopen.net/groupserver/gs.group.type.support
- Questions and comments to http://groupserver.org/groups/development
- Report bugs at https://redmine.iopen.net/projects/groupserver

.. [#canpost] See ``gs.group.member.canpost`` for more information:
   <https://source.iopen.net/groupserver/gs.group.member.canpost/>
.. _GroupServer: http://groupserver.org
