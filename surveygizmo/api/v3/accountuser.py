

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


def create(title, type, *args, **kwargs):
    """ Create new account user object.

        Required params:
            - email   email address

        Optional params:
            - username:
            - password:
            - team:                     team ID
            - create_access_token:
    """
    tail = "accountuser/"
    params = {
        '_method': 'PUT',
    }
    params.update(kwargs)
    return tail, params


def change(accountuser_id, *args, **kwargs):
    """ Change existing account user object.

        Required params:
        - accountuser_id: account user ID

        Optional params:
        - title:                    account user title
        - status:                   select from [launched, closed, deleted]
        - theme:                    theme ID
        - team:                     team ID
        - options[internal_title]:  internal title
        - blockby:                  select from [NONE, IP, COOKIE]
    """
    tail = "accountuser/%s" % accountuser_id
    params = {
        '_method': 'POST',
    }
    params.update(kwargs)
    return tail, params


def copy(accountuser_id, title, *args, **kwargs):
    """ Copy new account user object from existing account user.

        Required params:
        - accountuser_id:    account user ID
        - title:        account user title

        Optional params:
        - status:                   select from [launched, closed, deleted]
        - theme:                    theme ID
        - team:                     team ID
        - options[internal_title]:  internal title
        - blockby:                  select from [NONE, IP, COOKIE]
    """
    tail = "accountuser/%s" % accountuser_id
    params = {
        '_method': 'POST',
        'title': title,
        'copy': 'true',
    }
    params.update(kwargs)
    return tail, params


def delete(accountuser_id, *args, **kwargs):
    """ Delete account user object.

        Required params:
        - accountuser_id: accountuser ID
    """
    tail = "accountuser/%s" % accountuser_id
    params = {
        '_method': 'DELETE',
    }
    params.update(kwargs)
    return tail, params
