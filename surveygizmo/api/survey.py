
from surveygizmo.api import base


class Survey(base.Resource):
    resource_fmt_str = 'survey/%(survey_id)s'
    resource_id_keys = ['survey_id']

    def list(self, **kwargs):
        return super(Survey, self).list(**kwargs)

    def get(self, survey_id, **kwargs):
        kwargs.update({'survey_id': survey_id, })
        return super(Survey, self).get(**kwargs)

    def create(self, title, type, **kwargs):
        kwargs.update({
            'title': title,
            'type': type,
        })
        return super(Survey, self).create(**kwargs)

    def update(self, survey_id, **kwargs):
        kwargs.update({'survey_id': survey_id, })
        return super(Survey, self).update(**kwargs)

    def copy(self, survey_id, **kwargs):
        kwargs.update({
            'survey_id': survey_id,
        })
        return super(Survey, self).copy(**kwargs)

    def delete(self, survey_id, **kwargs):
        kwargs.update({'survey_id': survey_id, })
        return super(Survey, self).delete(**kwargs)
