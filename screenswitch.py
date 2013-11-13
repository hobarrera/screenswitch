#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# Copyright (c) 2013 Hugo Osvaldo Barrera <hugo@osvaldobarrera.com.ar>
#
# Permission to use, copy, modify, and distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

import sys

from xrandr import xrandr

if not xrandr.has_extension():
  print("xrandr unsupported, :(")
  sys.exit(1)

screen = xrandr.get_current_screen()

# The output that is now on, and will be disabled
current_screen = None
# The output that will be enabled (or remain enabled)
next_screen = None

for name, output in screen.outputs.iteritems():
  if output.is_connected(): # Only consider connected outputs
    if output.is_active():
      if current_screen is None: # If this is the first active output, mark it as current
        current_screen = output
      else:
        next_screen = output # If it's the the second active output, mark it as next
    else:
      next_screen = output # If it's disabled, mark it as next

if next_screen:
  next_screen.set_to_preferred_mode()
  screen.apply_output_config() # We need to enable first because python-xrandr blows up if no outputs are left enabled
  if current_screen:
    current_screen.disable()
    screen.apply_output_config() # Apply final changes
  screen.apply_config() # This fixes resolution if the last output has resolution different to the first one
