import re
#from docutils.core import publish_parts
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound, HTTPNotFound
from pyramid.url import route_url

from .models import (
    DBSession,
    Page,
    )

#@view_config(route_name='home', renderer='templates/mytemplate.pt')
def view_fishlog(request):
    return HTTPFound(location = route_url('view_page',request,           pagename='FrontPage'))
def view_page(request):
    pagename = request.matchdict['pagename']
    session = DBSession()
    page = session.query(Page).filter_by(name=pagename).first()
    if page is None:
        return HTTPNotFound('No such page')

    #content = publish_parts(page.data, writer_name='html')['html_body']
    content = "Hello World"
    return dict(page=page, content=content)

