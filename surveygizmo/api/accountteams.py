
from surveygizmo.api import base


class AccountTeams(base.Resource):
    resource_fmt_str = 'accountteams/%(accountteams_id)s'
    resource_id_keys = ['accountteams_id']

    def list(self, **kwargs):
        return super(AccountTeams, self).list(**kwargs)

    def get(self, accountteams_id, **kwargs):
        kwargs.update({'accountteams_id': accountteams_id, })
        return super(AccountTeams, self).get(**kwargs)

    def create(self, teamname, **kwargs):
        kwargs.update({
            'teamname': teamname,
        })
        return super(AccountTeams, self).create(**kwargs)

    def update(self, accountteams_id, **kwargs):
        kwargs.update({'accountteams_id': accountteams_id, })
        return super(AccountTeams, self).update(**kwargs)

    def copy(self, **kwargs):
        raise NotImplementedError()

    def delete(self, accountteams_id, **kwargs):
        kwargs.update({'accountteams_id': accountteams_id, })
        return super(AccountTeams, self).delete(**kwargs)
