

def list(*args, **kwargs):
    """ Get list of all account teams.

        Optional params:
        - showdeleted:      include deleted accountteams
        - page:             page number
        - resultsperpage:   number of results per page
    """
    return "accountteams/", {}


def get(accountteams_id, *args, **kwargs):
    """ Get account teams by id.

        Required params:
        - accountteams_id:    account teams ID
    """
    tail = "accountteams/%s" % accountteams_id
    params = {

    }
    params.update(kwargs)
    return tail, params


def create(*args, **kwargs):
    """ Create new accountteams object.

        Optional params:
        - teamname:         team name
        - description:      team description
        - color:            team color #FF00FF
        - defaultrole:      2 - 6 (ID of role)
    """
    tail = "accountteams/"
    params = {
        '_method': 'PUT',
    }
    params.update(kwargs)
    return tail, params


def update(accountteams_id, *args, **kwargs):
    """ Update existing accountteams object.

        Required params:
        - accountteams_id:  accountteams ID

        Optional params:
        - teamname:         team name
        - description:      team description
        - color:            team color #FF00FF
        - defaultrole:      2 - 6 (ID of role)
    """
    tail = "accountteams/%s" % accountteams_id
    params = {
        '_method': 'POST',
    }
    params.update(kwargs)
    return tail, params


def copy(accountteams_id, *args, **kwargs):
    """ Copy new account teams object from existing account teams.

        Required params:
        - accountteams_id:  account teams ID

        Optional params:
        - teamname:         team name
        - description:      team description
        - color:            team color #FF00FF
        - defaultrole:      2 - 6 (ID of role)
    """
    tail = "accountteams/%s" % accountteams_id
    params = {
        '_method': 'POST',
        'copy': 'true',
    }
    params.update(kwargs)
    return tail, params


def delete(accountteams_id, *args, **kwargs):
    """ Delete account teams object.

        Required params:
        - accountteams_id:       accountteams ID
    """
    tail = "accountteams/%s" % accountteams_id
    params = {
        '_method': 'DELETE',
    }
    params.update(kwargs)
    return tail, params
