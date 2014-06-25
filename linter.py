"""This module exports the CoffeeJshint plugin class."""

from __future__ import absolute_import, print_function, unicode_literals
from SublimeLinter.lint import Linter, util


class CoffeeJshint(Linter):
    """
    Provides an interface to coffee-jshint.
    """
    syntax = "coffeescript"
    cmd = "coffee-jshint"
    executable = None
    version_args = "--version"
    version_re = r"(?P<version>\d+\.\d+\.\d+)"
    version_requirement = '>= 0.1.2'
    regex = r"(?P<line>\d+):(?P<col>\d+):\s*(?P<message>.*)"
    multiline = False
    line_col_base = (1, 1)
    tempfile_suffix = "coffee"
    error_stream = util.STREAM_STDOUT
    selectors = {}
    word_re = None
    defaults = {
        "--globals:,": "require,module,window,document"
    }
    inline_settings = None
    inline_overrides = ("globals",)
    comment_re = r"\s*#"
