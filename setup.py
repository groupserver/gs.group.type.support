# -*- coding: utf-8 -*-
############################################################################
#
# Copyright © 2012, 2014 OnlineGroups.net and Contributors.
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
import codecs
import os
from setuptools import setup, find_packages
from version import get_version

version = get_version()

with codecs.open('README.rst', encoding='utf-8') as f:
    long_description = f.read()
with codecs.open(os.path.join("docs", "HISTORY.rst"),
                 encoding='utf-8') as f:
    long_description += '\n' + f.read()

name = 'gs.group.type.support'
url = 'https://github.com/groupserver/{0}/'.format(name)

setup(name=name,
      version=version,
      description='Support for "support" groups in GroupServer',
      long_description=long_description,
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          "Environment :: Web Environment",
          "Framework :: Zope2",
          "Intended Audience :: Developers",
          'License :: OSI Approved :: Zope Public License',
          "Natural Language :: English",
          "Natural Language :: French",
          "Operating System :: POSIX :: Linux",
          "Programming Language :: Python",
          "Topic :: Software Development :: Libraries :: Python Modules",
      ],
      keywords='group, support, posts, topics, canpost, privacy',
      author='Michael JasonSmith',
      author_email='mpj17@onlinegroups.net',
      url=url,
      license='ZPL 2.1',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['gs', 'gs.group', 'gs.group.type', ],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'zope.app.content',
          'zope.browserpage',
          'zope.cachedescriptors',
          'zope.component',
          'zope.i18n[compile]',
          'zope.i18nmessageid',
          'zope.interface',
          'zope.tal',
          'zope.tales',
          'Zope2',
          'gs.group.base',
          'gs.group.member.canpost',
          'gs.group.privacy',
          'gs.group.type.set',
      ],
      entry_points="""
          # -*- Entry points: -*-
      """,)
