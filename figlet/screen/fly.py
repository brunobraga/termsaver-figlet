###############################################################################
#
# file:     fly.py
#
# Purpose:  refer to python doc for documentation details.
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
This module contains a simple screen that displays a running dot on terminal.
See additional information in the class itself.

The screen class available here is:

    * `FigletFlyScreen`
"""

#
# Python mobdules
#
import random
import time

#
# Internal modules
#
from termsaverlib.screen.base import ScreenBase
from termsaverlib import constants, exception
from termsaverlib.i18n import _, set_app

#
# Internal modules
#
from termsaverlib.plugins.figlet.screen.base import FigletScreenBase

#
# Override termsavr default i18n (reuired for plugins with own i18n files)
#
set_app("termsaver-figlet")


class FigletFlyScreen(FigletScreenBase):
    """
    Simple screen that displays a running (animation) dot on a terminal window.

    From its base classes, the functionality provided here bases on the
    settings defined below:

        * clean up each cycle: True
          this will force the screen to be cleaned (cleared) before each new
          cycle is displayed
    """

    word = ''
    """
    Holds the word to be displayed on screen
    """

    def __init__(self):
        """
        The constructor of this class.
        """
        ScreenBase.__init__(self,
            "figlet-fly",
            _("displays flying text"),

            {'opts': 'hw:d:f:', 'long_opts': ['help', 'word=', 'delay=',
                                            'help-fonts', 'font=']},
        )
        self.word = constants.App.TITLE
        self.delay = 0.05
        self.cleanup_per_cycle = True

    def _run_cycle(self):
        """
        Executes a cycle of this screen.
        """
        # calculate random position based on screen size
        self.get_terminal_size()

        self.build_figlet_text(self.word)

        # make sure the figlet output can be printed on available screen
        if len(self.figlet_text.split("\n")) > self.geometry['y']:
            raise exception.InvalidOptionException("word",
                _("The word you are trying to print is just too big."))

        if self.position['x'] == self.geometry['x'] \
                + self.figlet_geometry['x']:
            self.position['x'] = 1
            self.position['y'] = random.randint(1,
                self.geometry['y'] - self.figlet_geometry['y'])

        self.position['x'] += 1
        new_text = ""
        for l in self.figlet_text.split("\n"):

            # print start/end in pieces
            if self.position['x'] < self.figlet_geometry['x']:
                txt = l[self.figlet_geometry['x'] - self.position['x']:]
            elif self.position['x'] > self.geometry['x']:
                txt = " " * (self.position['x'] - self.figlet_geometry['x']) \
                    + l[:self.geometry['x'] - self.position['x']]
            else:
                txt = " " * (self.position['x'] - self.figlet_geometry['x']) \
                    + l
            new_text += "\n" + txt

        print "\n" * self.position['y'] + new_text
        time.sleep(self.delay)

    def _usage_options_example(self):
        """
        Describe here the options and examples of this screen.

        The method `_parse_args` will be handling the parsing of the options
        documented here.

        Additionally, this is dependent on the values exposed in `cli_opts`,
        passed to this class during its instantiation. Only values properly
        configured there will be accepted here.
        """
        print _("""
Options:

 -w, --word   Sets the word to be displayed
              default is the name of this application (if you need to use
              spaces, don't forget to place the word with quotes)
 -d, --delay  Sets the speed of the displaying characters
              default is 0.05 of a second (advised to keep
              between 0.1 and 0.01).
 -f, --font   the figlet font to be used, default is the figlet default
              (see `figlet -I3` command for details or figler man pages)
 -h, --help   Displays this help message
     --help-fonts
              Displays the available fonts that can be used with
              the -f/--font option.
Example:

    $ %(app_name)s %(screen)s
    This will trigger the screensaver to display the default word
    %(app_title)s in random locations of the screen

    $ %(app_name)s %(screen)s -w FooBar -f lean -d 0.005
    This will trigger the screensaver to display the word FooBar
    in random locations of the screen, using the "lean" figlet font with
    a delay of 0.005 seconds (fast).
""") % {
        'app_name': constants.App.NAME,
        'screen': self.name,
       }

    def _parse_args(self, prepared_args):
        """
        Handles the special command-line arguments available for this screen.
        Although this is a base screen, having these options prepared here
        can save coding for screens that will not change the default options.

        See `_usage_options_example` method for documentation on each of the
        options being parsed here.

        Additionally, this is dependent on the values exposed in `cli_opts`,
        passed to this class during its instantiation. Only values properly
        configured there will be accepted here.
        """
        for o, a in prepared_args[0]:  # optlist, args
            if o in ("-h", "--help"):
                self.usage()
                self.screen_exit()
            elif o == "--help-fonts":
                self.help_fonts()
                self.screen_exit()
            elif o in ("-d", "--delay"):
                try:
                    # make sure argument is a valid value (float)
                    self.freeze_delay = float(a)
                except:
                    raise exception.InvalidOptionException("delay")
            elif o in ("-w", "--word"):
                # make sure argument is a valid value
                if a in (None, ''):
                    raise exception.InvalidOptionException("word")
                self.word = a
            elif o in ("-f", "--font"):
                # make sure argument is a valid value (exists)
                self.font = str(a)
                if self.font not in self.get_fonts():
                    raise exception.InvalidOptionException("font",
                        _("Font does not exist"))
            else:
                # this should never happen!
                raise Exception(_("Unhandled option. See --help for details."))
