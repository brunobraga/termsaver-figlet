<!-- 
###############################################################################
#
# file:     README
#
# Purpose:  holds basic information about Termsaver-Figlet plugin, 
#           in markdown format for GitHub.
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
-->

TermSaver-FigLet
================

*A FigLet-based plugin with a set of screensavers for TermSaver application.*

You may also want to visit our website: 

**<http://www.termsaver.info/plugins>**

![termsaver](https://github.com/brunobraga/termsaver-figlet/raw/master/extras/termsaver-figlet-main_medium.jpeg)


Background
----------

See detailed documentation of TermSaver application here:

**<http://github.com/brunobraga/termsaver/>**

Based on the above, this plugin comes to place to give extra-functionalities
to TermSaver application:

  * Screensavers using FigLet fonts as output (cool ASCII based font drawings
that make a good case for terminal screensavers)


Requirements
------------

  * Linux, or Mac
  * Python 2.4+ (and < 3.x)
  * Termsaver 
  * Figlet


Installation
------------

#### Fast and Simple

For those without the time or patience to scan through the rest of this 
document, here is the installation procedure, plain and simple:

        pip install termsaver-figlet

And you are done!

**Note**: I discourage the use of *easy_install* (does not add man pages, or 
localization files)


#### From the Source

1. Download the Source 
[here](http://pypi.python.org/pypi/termsaver-figlet/)
2. Unpack it
     
        tar -zxvf termsaver-figlet-{version}.tar.gz

3. Install it

        sudo ./setup.sh

**Note**: Use the bash script instead of the setup.py python script because it prepares the environment to handle the Termsaver library dependencies. See this bash script if you want to run things yourself.

4. All done! 


Features
--------

The TermSaver is a very simple application, built with the idea to allow more 
screensavers to be added to its core. Developers, please read the section below. 

The current published screensavers are:

#### Figlet Fly

Shows a flying (horizontally) text using Figlet fonts.

#### Figlet Stat

An alternative to Termsaver's **randtxt**, using Figlet fonts instead.

 - - -

**Disclaimer Note**: termsaver-figlet holds no responsibility for the fonts offered 
Figlet and/or installed by third-parties, nor it has controls to filter them. Use it at your own risk.


Developers
----------

Feel free to help us out by improving this, or use it as base for creating your own Termsaver plugins. Some guidelines for that will be available soon.


Roadmap
-------

There is no current roadmap defined, besides improvement tickets created in
[Issues](https://github.com/brunobraga/termsaver-figlet/issues) tab in GitHub.
Refer also to <http://github.com/brunobraga/termsaver-figlet/wiki/Brainstorming> for
some insights of stuff we are thinking about.

Contribute
----------

### Translation

The internationalization of this application follows same standards of most
applications out there, by using *gettext* and MO/PO files.

The translation is still being finished up, and when it is ready for 
contributor calls, we will post detailed information about the procedure.

Let us know you want to help: <support@termsaver.info>


### Submit a bug

If you find any errors in this application, you are more than welcome to 
participate. You can:

* report the bug: <https://github.com/brunobraga/termsaver-figlet/issues>

* Fork this project: <https://github.com/brunobraga/termsaver-figlet/fork>
    

Uninstall
----------

### Using Pip

    pip uninstall termsaver-figlet

### Manual Uninstall

Just remove manually the following files:

    # For Linux boxes
    rm -rvf /usr/local/bin/termsaver/plugins/figlet 
    find /usr/local/share/locale/ -name "termsaver-figlet.mo" -exec rm -rfv {} \; 

