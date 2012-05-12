#!/usr/bin/env python
###############################################################################
#
# file:     setup.py
#
# Purpose:  installs the Termsaver-Figlet plugin
#
# Note:     This file is part of Termsaver-Figlet plugin, and should not be
#           used or executed separately.
#
###############################################################################
#
# Copyright 2012 Termsaver
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
#
###############################################################################
"""
The installation script of termsaver-figlet plugin for Termsaver-Figlet plugin.

    sudo python setup.py install

You may also refer to:

    sudo pip install termsaver-figlet

"""

import os
import platform
from distutils.core import setup
from figlet import constants


if platform.system() == 'FreeBSD':
    man_dir = 'man'
else:
    man_dir = 'share/man'

data_files = [(os.path.join('share', 'locale', lang, 'LC_MESSAGES'),
                [os.path.join('locale', lang, 'LC_MESSAGES',
                'termsaver-figlet.mo')]) for lang in os.listdir('locale')]

setup(name='termsaver-figlet',
      version=constants.Plugin.VERSION,
      description='Plugin for termsaver to use figlet text for screensaver.',
      author='Bruno Braga',
      author_email='bruno.braga@gmail.com',
      classifiers=[
            'Development Status :: 5 - Production/Stable',
            'Environment :: Console',
            'Intended Audience :: Developers',
            'Intended Audience :: Information Technology',
            'Intended Audience :: System Administrators',
            'License :: OSI Approved :: Apache Software License',
            'Natural Language :: English',
            'Operating System :: MacOS',
            'Operating System :: POSIX',
            'Programming Language :: Python',
            'Topic :: Terminals',
            'Topic :: Utilities',
      ],
      url='http://www.termsaver.info/plugins',
      keywords=['command-line', 'terminal', 'screensaver'],
      packages=[
            'figlet',
            'figlet.screen',
            'figlet.screen.base',
      ],
      license='Apache License v2',
      data_files=data_files,
)
