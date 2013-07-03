

def list(*args, **kwargs):
    """ Get list of all accounts.
    """
    return "account/", {}


def get(account_id, *args, **kwargs):
    """ Get account by id.

        Required params:
        - account_id:    survey ID
    """
    tail = "account/%s" % account_id
    params = {

    }
    params.update(kwargs)
    return tail, params
