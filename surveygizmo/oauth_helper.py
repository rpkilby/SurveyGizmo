
import rauth


class SGAuthService(rauth.OAuth1Service):
    """ This is a helper class that wraps `rauth.OAuth1Service` and slightly
        simplifies the process of authenciating with SurveyGizmo.
        For further details on the underlying implementation and inherited
        properties, refer to the rauth documentation.

        This class should primarily be used for retrieving an access_token,
        which can then be provided to the API. To do this, provide the
        `consumer_key` and `consumer_secret` given to you during application
        registration, and make the subsequent calls to `get_authorize_url` and
        `get_access_token`.

        `get_authorize_url` will generate a request token and provide a url
        that directs a user to authenticate your application with SurveyGizmo.
        SurveyGizmo will then make a request containing the `oauth_verifier`
        to the callback_url specified during registration.

        `get_access_token` takes the `oauth_verifier` provided by SurveyGizmo
        and trades it and your request token for an access token pair. This
        contains the `access_token` and `access_token_secret`. The token pair
        should be saved securely and then provided to the API for requests.


        This helper class can also be used to directly make custom calls to
        SurveyGizmo's REST API. After calling `get_access_token`, the service
        is able to create a session object through `get_session`, which will
        make the actual requests. Refer to the rauth documentation for more
        information on `Session` objects.
        If the original `SGAuthService` object has been discarded,
        reinstantiate it with the `access_token` and `access_token_secret`.

        :param consumer_key: Client consumer key, required for signing.
        :type consumer_key: str
        :param consumer_secret: Client consumer secret, required for signing.
        :type consumer_secret: str
        :param access_token: Client oauth token, required for authenticating.
        :type access_token: str
        :param access_token_secret: Client oauth token secret, required for authenticating.
        :type access_token_secret: str
    """
    def __init__(self, consumer_key, consumer_secret,
                 access_token=None, access_token_secret=None):

        self.access_token = access_token
        self.access_token_secret = access_token_secret
        super(SGAuthService, self).__init__(
            name="surveygizmo",
            consumer_key=consumer_key,
            consumer_secret=consumer_secret,
            request_token_url='https://restapi.surveygizmo.com/head/oauth/request_token',
            access_token_url='https://restapi.surveygizmo.com/head/oauth/access_token',
            authorize_url='https://restapi.surveygizmo.com/head/oauth/authenticate',
            base_url='https://restapi.surveygizmo.com/'
        )

    def get_authorize_url(self):
        """ Generates a request token and generates a URL for authorizing your
            application.
        """
        self._request_token, self._request_token_secret = self.get_request_token()
        return super(SGAuthService, self).get_authorize_url(self._request_token)

    def get_access_token(self, oauth_verifier):
        """ Retrieves an access token pair form SurveyGizmo. This invalidates the
            `oauth_verifier`.
            :param oauth_verifier: Verification code tied to an authorization request.
            :type oauth_verifier: str
        """
        access_pair = super(SGAuthService, self).get_access_token(
            self._request_token,
            self._request_token_secret,
            data={'oauth_verifier': oauth_verifier}
        )
        self.access_token, self.access_token_secret = access_pair
        return access_pair

    def get_session(self):
        """ Gets an authenticated session object. This session can make requests
            to SurveyGizmo's REST API.
        """
        token = (self.access_token, self.access_token_secret)
        return super(SGAuthService, self).get_session(token)
