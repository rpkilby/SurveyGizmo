'''
    SurveyGizmo
    -----------

    A Python Wrapper for SurveyGizmo's restful API service

        >>> from surveygizmo import SurveyGizmo
        >>> sg = SurveyGizmo('v3')
        >>> sg.config.auth_method = 'user:md5'
        >>> sg.config.username = ...
        >>> sg.config.md5_hash = ...

        ...

        >>> surveys = sg.api.survey.list()
        >>> print surveys

'''

__title__ = 'surveygizmo'
__version_info__ = ('0', '2', '0')
__version__ = '.'.join(__version_info__)
__author__ = 'Ryan P Kilby'
__license__ = 'BSD 3-Clause'
__copyright__ = 'Copyright 2013-2014 NC State University'
__all__ = ['SurveyGizmo', 'ImproperlyConfigured', 'SGAuthService']


# Import pattern from rauth. This is necessary for imports during setup/install
try:
    from .oauth_helper import SGAuthService
    from .surveygizmo import SurveyGizmo, ImproperlyConfigured, default_52x_handler

    # placate pyflakes
    (SGAuthService, SurveyGizmo, ImproperlyConfigured, default_52x_handler)
except ImportError:  # pragma: no cover
    pass
