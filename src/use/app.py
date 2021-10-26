"""
Module that will run use and use --test

This is the primary module that does all of the work.

Technically, we could put many of these functions in __main__.py. That is the
main module of this application anyway. However, for testing purposes we want all
functions in modules and we only want script code in the file __main__.py

Author: Christian M. Fulton
Date: 25.Oct.2021
"""

import tests
import main
from mod import ProxyModule


def using_use():
    """
    Used to use use
    """
    use = main.Use()
    use.__dict__.update({k: v for k, v in globals().items()})
    use = ProxyModule(use)


def execute(args):
    err = "Usage: python use --test"
    if len(args) < 1:
        using_use()
    elif len(args) == 1:
        if args[0] == "--test":
            tests.test_all()
    else:
        print(err)
