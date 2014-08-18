
from surveygizmo.api import base


class ContactList(base.Resource):
    resource_fmt_str = 'contactlist/%(contactlist_id)s'
    resource_id_keys = ['contactlist_id']

    def list(self, **kwargs):
        """ Get list of all contacts for a survey campaign.

            Optional params:
            - page:             page number
            - resultsperpage:   number of results per page
        """
        return super(ContactList, self).list(**kwargs)

    def get(self, contactlist_id, **kwargs):
        """ Get contact by id.

            Required params:
            - contactlist_id:   contactlist ID

            Optional params:
            - page:             page number
            - resultsperpage:   number of results per page
        """
        kwargs.update({
            'contactlist_id': contactlist_id,
        })
        return super(ContactList, self).get(**kwargs)

    def create(self, listname, **kwargs):
        """ Create new contact object.

            Required params:
            - listname

            Optional params:
            refer to official documentation
        """
        kwargs.update({
            'listname': listname,
        })
        return super(ContactList, self).create(**kwargs)

    def update(self, contactlist_id, semailaddress, **kwargs):
        """ Change existing contact object.

            Required params:
            - contactlist_id:   contactlist ID
            - semailaddress:    contact's email address

            Optional params:
            refer to official documentation
        """
        kwargs.update({
            'contactlist_id': contactlist_id,
            'semailaddress': semailaddress,
        })
        return super(ContactList, self).update(**kwargs)

    def copy(self, **kwargs):
        raise NotImplementedError()

    def delete(self, **kwargs):
        raise NotImplementedError()
