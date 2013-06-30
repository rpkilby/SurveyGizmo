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

        >>> surveys = sg.api.list_surveys()
        >>> print surveys

'''

__title__ = 'surveygizmo'
__version_info__ = ('0', '0', '1')
__version__ = '.'.join(__version_info__)
__author__ = 'Ryan P Kilby'
__license__ = 'MIT'
__copyright__ = 'Copyright 2013 Ryan P Kilby'
__all__ = ['SurveyGizmo', 'ImproperlyConfigured', 'SGAuthService']


from .oauth_helper import SGAuthService
from .surveygizmo import SurveyGizmo, ImproperlyConfigured
