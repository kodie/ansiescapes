***********
ansiescapes
***********

`ANSI escape codes <http://www.termsys.demon.co.uk/vtansi.htm>`_ for manipulating the terminal - A Python port of `sindresorhus <https://github.com/sindresorhus>`_'s `ansi-escapes <https://github.com/sindresorhus/ansi-escapes>`_ Node.js module.

Installation
============
.. code-block:: bash

  $ pip install ansiescapes

Usage
=====
.. code-block:: python

  import ansiescapes
  import sys

  # Moves the cursor two rows up and to the left
  sys.stdout.write(ansiescapes.cursorUp(2) + ansiescapes.cursorLeft)
  #=> '\u001B[2A\u001B[1000D'

API
===

cursorTo(x, [y])
----------------
Set the absolute position of the cursor. `x0` `y0` is the top left of the screen.

cursorMove(x, [y])
------------------
Set the position of the cursor relative to its current position.

cursorUp(count)
---------------
Move cursor up a specific amount of rows. Default is `1`.

cursorDown(count)
-----------------
Move cursor down a specific amount of rows. Default is `1`.

cursorForward(count)
--------------------
Move cursor forward a specific amount of rows. Default is `1`.

cursorBackward(count)
---------------------
Move cursor backward a specific amount of rows. Default is `1`.

cursorLeft
----------
Move cursor to the left side.

cursorSavePosition
------------------
Save cursor position.

cursorRestorePosition
---------------------
Restore saved cursor position.

cursorGetPosition
-----------------
Get cursor position.

cursorNextLine
--------------
Move cursor to the next line.

cursorPrevLine
--------------
Move cursor to the previous line.

cursorHide
----------
Hide cursor.

cursorShow
----------
Show cursor.

eraseLines(count)
-----------------
Erase from the current cursor position up the specified amount of rows.

eraseEndLine
------------
Erase from the current cursor position to the end of the current line.

eraseStartLine
--------------
Erase from the current cursor position to the start of the current line.

eraseLine
---------
Erase the entire current line.

eraseDown
---------
Erase the screen from the current line down to the bottom of the screen.

eraseUp
-------
Erase the screen from the current line up to the top of the screen.

eraseScreen
-----------
Erase the screen and move the cursor the top left position.

scrollUp
--------
Scroll display up one line.

scrollDown
----------
Scroll display down one line.

clearScreen
-----------
Clear the terminal screen.

beep
----
Output a beeping sound.

image(input, [options])
-----------------------
Display an image.

*Currently only supported on iTerm2 >=3*

See `termimg <https://github.com/kodie/termimg>`_ for a higher-level module.

input
~~~~~

Type: `Buffer`

Buffer of an image. Usually read in with `open`.

Example:

.. code-block:: python

  import ansiescapes
  import sys
  from codecs import open

  with open('image.png', 'rb') as imageFile:
    f = imageFile.read()
    b = bytearray(f)

  sys.stdout.write(ansiescapes.image(b))

options
~~~~~~~

width
_____
height
______

Type: `string` `number`

The width and height are given as a number followed by a unit, or the word "auto".

- `N`: N character cells.
- `Npx`: N pixels.
- `N%`: N percent of the session's width or height.
- `auto`: The image's inherent size will be used to determine an appropriate dimension.

preserveAspectRatio
___________________

Type: `boolean`

Default: `true`

setCwd([path])
--------------

Type: `string`

Default: `os.getcwd()`

`Inform iTerm2 <https://www.iterm2.com/documentation-escape-codes.html>`_ of the current directory to help semantic history and enable `Cmd-clicking relative paths <https://coderwall.com/p/b7e82q/quickly-open-files-in-iterm-with-cmd-click>`_.

License
=======
MIT. See the `LICENSE file <LICENSE.md>`_ for more info.
