

def list(*args, **kwargs):
    """ Get list of all account users.

        Optional params:
        - page:             page number
        - resultsperpage:   number of results per page
    """
    return "accountuser/", {}


def get(accountuser_id, *args, **kwargs):
    """ Get account user by id.

        Required params:
        - accountuser_id:    account user ID
    """
    tail = "accountuser/%s" % accountuser_id
    params = {

    }
    params.update(kwargs)
    return tail, params


def create(email, *args, **kwargs):
    """ Create new accountuser object.

        Required params:
        - email:                email address

        Optional params:
        - username:             username
        - password:             password
        - team:                 team ID
        - create_access_token:  only allowed when using oauth
    """
    tail = "accountuser/"
    params = {
        '_method': 'PUT',
        'email': email,
    }
    params.update(kwargs)
    return tail, params


def update(accountuser_id, *args, **kwargs):
    """ Update existing accountuser object.

        Required params:
        - accountuser_id:       accountuser ID

        Optional params:
        - email:                email address
        - username:             username
        - password:             password
        - team:                 team ID
    """
    tail = "accountuser/%s" % accountuser_id
    params = {
        '_method': 'POST',
    }
    params.update(kwargs)
    return tail, params


def copy(accountuser_id, email, *args, **kwargs):
    """ Copy new account user object from existing account user.

        Required params:
        - accountuser_id:       account user ID
        - email:                email address

        Optional params:
        - username:             username
        - password:             password
        - team:                 team ID
    """
    tail = "accountuser/%s" % accountuser_id
    params = {
        '_method': 'POST',
        'email': email,
        'copy': 'true',
    }
    params.update(kwargs)
    return tail, params


def delete(accountuser_id, *args, **kwargs):
    """ Delete account user object.

        Required params:
        - accountuser_id:       accountuser ID
    """
    tail = "accountuser/%s" % accountuser_id
    params = {
        '_method': 'DELETE',
    }
    params.update(kwargs)
    return tail, params
