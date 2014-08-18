
from surveygizmo.api import base


class Account(base.Resource):
    resource_fmt_str = 'account/'
    resource_id_keys = []

    def list(self, **kwargs):
        raise NotImplementedError()

    def get(self, **kwargs):
        return super(Account, self).get(**kwargs)

    def create(self, **kwargs):
        raise NotImplementedError()

    def update(self, **kwargs):
        raise NotImplementedError()

    def copy(self, **kwargs):
        raise NotImplementedError()

    def delete(self, **kwargs):
        raise NotImplementedError()
