from django.contrib.auth.decorators import login_required


class LoginRequireMixin(object):

    @classmethod
    def as_view(cls, **init_kwargs):
        view = super(LoginRequireMixin, cls).as_view(**init_kwargs)
        return login_required(view)
