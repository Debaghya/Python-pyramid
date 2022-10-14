from pyramid.config import Configurator
from pyramid.session import SignedCookieSessionFactory

from pyramid_sqlalchemy import metadata




def main(global_config, **settings):
    config = Configurator(settings=settings)
    config.include('pyramid_jinja2')
    config.scan()
    config.include('pyramid_sqlalchemy')
    metadata.create_all()
    config.add_static_view(name='deform_static', path='deform:static')
    config.add_static_view(name='static', path='mysite.site:static')
    config.add_route('home', '/')

    # User routes with route factory
    config.add_route('users_list', '/users',
                     factory='.users.models.user_factory')
    config.add_route('users_add', '/users/add',
                     factory='.users.models.user_factory')
    config.add_route('users_view', '/users/{id}',
                     factory='.users.models.user_factory')
    config.add_route('users_edit', '/users/{id}/edit',
                     factory='.users.models.user_factory')
    config.add_route('users_delete', '/users/{id}/delete',
                     factory='.users.models.user_factory')

    session_secret = settings['session.secret']
    session_factory = SignedCookieSessionFactory(session_secret)
    config.set_session_factory(session_factory)



    return config.make_wsgi_app()
