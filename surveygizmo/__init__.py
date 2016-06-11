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

from .surveygizmo import SurveyGizmo, ImproperlyConfigured

__all__ = ['SurveyGizmo', 'ImproperlyConfigured']
