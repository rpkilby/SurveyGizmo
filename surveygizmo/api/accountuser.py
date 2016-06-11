
from surveygizmo.api import base


class AccountUser(base.Resource):
    resource_fmt_str = 'accountuser/%(accountuser_id)s'
    resource_id_keys = ['accountuser_id']

    def list(self, **kwargs):
        return super(AccountUser, self).list(**kwargs)

    def get(self, accountuser_id, **kwargs):
        kwargs.update({'accountuser_id': accountuser_id, })
        return super(AccountUser, self).get(**kwargs)

    def create(self, email, **kwargs):
        kwargs.update({
            'email': email,
        })
        return super(AccountUser, self).create(**kwargs)

    def update(self, accountuser_id, **kwargs):
        kwargs.update({'accountuser_id': accountuser_id, })
        return super(AccountUser, self).update(**kwargs)

    def copy(self, **kwargs):
        raise NotImplementedError()

    def delete(self, accountuser_id, **kwargs):
        kwargs.update({'accountuser_id': accountuser_id, })
        return super(AccountUser, self).delete(**kwargs)
