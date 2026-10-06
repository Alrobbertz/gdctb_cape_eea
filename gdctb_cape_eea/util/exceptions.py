"""
This module provides errors/exceptions and warnings of general use.

Exceptions that are specific to a given package should **not** be here,
but rather in the particular package.

This code is based on that provided by SunPy see
    licenses/SUNPY.rst
"""
import warnings

__all__ = [
    "cape_eeaWarning",
    "cape_eeaUserWarning",
    "cape_eeaDeprecationWarning",
    "cape_eeaPendingDeprecationWarning",
    "warn_user",
    "warn_deprecated",
]


class cape_eeaWarning(Warning):
    """
    The base warning class from which all GDCTB CAPE_EEA warnings should inherit.

    Any warning inheriting from this class is handled by the GDCTB CAPE_EEA
    logger. This warning should not be issued in normal code. Use
    "cape_eeaUserWarning" instead or a specific sub-class.
    """


class cape_eeaUserWarning(UserWarning, cape_eeaWarning):
    """
    The primary warning class for GDCTB CAPE_EEA.

    Use this if you do not need a specific type of warning.
    """


class cape_eeaDeprecationWarning(FutureWarning, cape_eeaWarning):
    """
    A warning class to indicate a deprecated feature.
    """


class cape_eeaPendingDeprecationWarning(PendingDeprecationWarning, cape_eeaWarning):
    """
    A warning class to indicate a soon-to-be deprecated feature.
    """


def warn_user(msg, stacklevel=1):
    """
    Raise a `cape_eeaUserWarning`.

    Parameters
    ----------
    msg : str
        Warning message.
    stacklevel : int
        This is interpreted relative to the call to this function,
        e.g. ``stacklevel=1`` (the default) sets the stack level in the
        code that calls this function.
    """
    warnings.warn(msg, cape_eeaUserWarning, stacklevel + 1)


def warn_deprecated(msg, stacklevel=1):
    """
    Raise a `cape_eeaDeprecationWarning`.

    Parameters
    ----------
    msg : str
        Warning message.
    stacklevel : int
        This is interpreted relative to the call to this function,
        e.g. ``stacklevel=1`` (the default) sets the stack level in the
        code that calls this function.
    """
    warnings.warn(msg, cape_eeaDeprecationWarning, stacklevel + 1)
