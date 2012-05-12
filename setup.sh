#!/bin/bash
###############################################################################
#
# file:     setup.sh
#
# Purpose:  wrapper for more suitable/easy installation from source
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

# ############################
# CONFIGURABLE SETTINGS: BEGIN
# ############################

#
# Defines the installation path
#
# this is used to override the default distutils installation path,
# that places files publicly available in dist-packages directory.
#
# This is an attempt to simulate the same behavior of packaging installation
#
install_path=/usr/local

# ############################
# CONFIGURABLE SETTINGS: END
# ############################

#
# Force Termsaver private library to be available for its plugins
#
export PYTHONPATH=$PYTHONPATH:$install_path/share/termsaver

# execute setup installation to specific path (instead of default)
python setup.py install \
    --install-lib=$install_path/share/termsaver/termsaverlib/plugins \
    --install-data=$install_path

