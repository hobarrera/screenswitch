Screenswitch
============

This tiny utility toggles between two connected screens (screen as in
LCD Monitor, NOT Xorg screens). If both are enabled, one will be disabled
(which one is undefined). If both are disabled, one will be enabled
(which one is undefined).

If more than two screens are connected, the results are undefined.
If only one monitor is connected, nothing will happen.

The main goal of this script, is to bind it to some keybind, and quickly
switch between screens when I get home. It shouldn't be too much effort
to handle three screens. It should also be possible to rotate between
screen1, screen2 and both, and I may implement this in future.

Of course, patches are very much welcome.

Requires python-xrandr.

Distributed under the terms of the BSD license; see LICENSE for details.

Copyright (c) 2013 Hugo Osvaldo Barrera
