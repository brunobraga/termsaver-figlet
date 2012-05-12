###############################################################################
#
# file:     __init__.py
#
# Purpose:  refer to module documentation for details
#
# Note:     This file is part of Termsaver-Figlet plugin, and should not be used
#           or executed separately.
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
This module holds base classes that are used by all screens within termsaver
application. Each individual "screen" represents a unique screensaver that can
be triggered by termsaver.

The base classes available in this package are:

  * `FigletScreenBase`: the most basic screen class, which will handle simple
     interaction with the terminal.


"""

#
# Python built-in modules
#
import os
import textwrap

#
# Internal modules
#
from termsaverlib.screen.base import ScreenBase
from termsaverlib import common, exception
from termsaverlib.screen.helper.position import PositionHelperBase
from termsaverlib.i18n import _, set_app

#
# Override termsavr default i18n (reuired for plugins with own i18n files)
#
set_app("termsaver-figlet")


class FigletScreenBase(ScreenBase, PositionHelperBase):
    """
    """

    font = 'standard'
    """
    Holds the figlet font name to be used for the screen display

    Default value is "standard"
    """

    figlet_geometry = {'x': 0, 'y': 0}
    """
    """

    figlet_text = ""
    """
    """

    def execute_shell(self, cmd):
        """
        Simple routine to execute shell commands
        """
        try:
            return common.execute_shell(cmd, False)
        except Exception, e:
            raise exception.TermSaverException(help=_(
"""Could not execute the command [%(cmd)s] properly.
%(message)s \nError details: %(error)s""") % {
                     "cmd": " ".join(cmd),
                     "message": "Make sure you have figlet installed!",
                     "error": str(e)
                 }
            )

    def get_fonts(self):
        """
        Retrieve a list of all available figlet fonts,
        by executing the command:
            figlet -I2

        See figlet man pages for detailed documentation on this.
        """

        font_path = self.execute_shell(["figlet", "-I2"])

        # get the font files installed in font_path,
        # and clean them up for printing
        fonts = [os.path.split(x)[1].split(".")[0] \
                 for x in self.execute_shell(["find",
                 font_path, "-iname", "*.flf"]).split("\n")]

        return fonts

    def help_fonts(self):

        fonts = self.get_fonts()
        ScreenBase.usage_header()
        print _("""Here is the list of all available figlet fonts that are
supported in your system:

%(fonts)s

You may try to use them with the option -f/--font. See --help for details.

You may also refer to official figlet documentation for additional details
on how to deal with fonts.
""") % {
         'fonts': "\t" + "\n\t".join(textwrap.wrap(", ".join(fonts), 50)),
        }
        ScreenBase.usage_footer()

    def build_figlet_text(self, text):
        """
        Executes the shell command to get the figlet output, based on
        the defined font, and terminal geometry.
        """

        self.figlet_text = self.execute_shell(["figlet", "-f", self.font, '-w',
                                          str(self.geometry['x']), text])

        temp = self.figlet_text.split("\n")
        if len(temp) > 0:
            self.figlet_geometry['x'] = max([len(x) for x in temp])
        self.figlet_geometry['y'] = len(temp)

        # fix trailing spaces
        new_text = []
        for l in temp:
            if len(l) < self.figlet_geometry['x']:
                new_text.append(
                    l + " " * (self.figlet_geometry['x'] - len(l)))
            else:
                new_text.append(l)
        self.figlet_text = "\n".join(new_text)
