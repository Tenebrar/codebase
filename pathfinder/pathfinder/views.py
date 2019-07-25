from webserver.util.view_decorators import template_view


@template_view('pathfinder/index.html')
def index():
    # TODO return the apps I have (if possible automatically) as urls, and adjust the html accordingly
    return {'apps': {'charsheet': 'sheets'}}
