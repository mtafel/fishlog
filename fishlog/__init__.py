from pyramid.config import Configurator
from sqlalchemy import engine_from_config
from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy
#from tutorial.security import groupfinder
from .models import DBSession, initialize_sql

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    #engine = engine_from_config(settings, 'sqlalchemy.')
    #DBSession.configure(bind=engine)
    #authn_policy = AuthTktAuthenticationPolicy('sosecret', callback=groupfinder)
    #authz_policy = ACLAuthorizationPolicy()
    engine = engine_from_config(settings, 'sqlalchemy.')
    initialize_sql(engine)

    config = Configurator(settings=settings)
    config.add_static_view('static', 'fishlog:static')
    config.add_route('view_fishlog', '/')
    config.add_route('view_page', '/{pagename}')
    #config.add_route('add_page', '/add_page/{pagename}')
    #config.add_route('edit_page', '/{pagename}/edit_page')
    config.add_view('fishlog.views.view_fishlog', route_name='view_fishlog')
    config.add_view('fishlog.views.view_page', route_name='view_page',
                    renderer='fishlog:templates/view.pt')
    return config.make_wsgi_app()
