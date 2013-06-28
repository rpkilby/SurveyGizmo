
import rauth


class SGAuthService(rauth.OAuth1Service):
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
        self._request_token, self._request_token_secret = self.get_request_token()
        return super(SGAuthService, self).get_authorize_url(self._request_token)

    def get_access_token(self, oauth_verifier):
        access_pair = super(SGAuthService, self).get_access_token(self._request_token,
                                                                    self._request_token_secret,
                                                                    data={'oauth_verifier': oauth_verifier})
        self.access_token, self.access_token_secret = access_pair
        return access_pair

    def get_session(self):
        token = (self.access_token, self.access_token_secret)
        return super(SGAuthService, self).get_session(token)
