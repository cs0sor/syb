from pyramid.config import Configurator
from sqlalchemy import engine_from_config

from .models import (
    DBSession,
    Base,
    )


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('pyramid_chameleon')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('about', '/about')
    config.add_route('case-studies', '/case-studies')
    config.add_route('contact', '/contact')
    config.add_route('test', '/test')
    config.add_route('thanks', '/thanks')
    config.scan()
    return config.make_wsgi_app()
