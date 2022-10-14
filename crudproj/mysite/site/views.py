from pyramid.httpexceptions import HTTPFound
from pyramid.security import remember, forget
from pyramid.view import (
    view_config,
    notfound_view_config,
    forbidden_view_config
)

from pyramid_sqlalchemy import Session

from ..users.models import User


class SiteViews:
    def __init__(self, context, request):
        self.context = context
        self.request = request

    @view_config(route_name='home', renderer='templates/home.jinja2')
    def home(self):
        return dict()

    @notfound_view_config(renderer='templates/notfound.jinja2')
    def not_found(self):
        return dict()

    @forbidden_view_config(renderer='templates/forbidden.jinja2')
    def forbidden(self):
        return dict()

