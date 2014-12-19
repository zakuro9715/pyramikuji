from pyramid.view import view_config

@view_config(route_name='home', renderer='templates/home.html')
def home_view(request):
    return {}

@view_config(route_name='mikuji', renderer='templates/mikuji_result.html')
def mikuji_view(context, request):
    return {'text': context.text}

@view_config(route_name='mikuji_json', renderer='json')
def mikuji_json_view(context, request):
    return context

