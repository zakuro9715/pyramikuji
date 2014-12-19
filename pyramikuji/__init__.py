from pyramid.config import Configurator


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('pyramid_mako')
    config.add_mako_renderer('.html', settings_prefix='mako.')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('mikuji', '/mikuji', factory='.resources.mikuji_factory')
    config.add_route('mikuji_json', '/mikuji.json', factory='.resources.mikuji_factory')
    config.scan()
    return config.make_wsgi_app()
