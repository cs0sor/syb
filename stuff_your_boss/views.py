from pyramid.response import Response
from pyramid.view import view_config
import colander
import deform

from sqlalchemy.exc import DBAPIError

from .models import (
    DBSession,
    MyModel,
    )

@view_config(route_name='home', layout='front_page', renderer='templates/home.pt')
def home(request):

    return {}

@view_config(route_name='test', layout='public', renderer='templates/test.pt')
def test(request):

    return {}


@view_config(route_name='about', layout='public', renderer='templates/about.pt')
def about(request):

    return {}

@view_config(route_name='contact', layout='public', renderer='templates/contact.pt')
def contact(request):

    class nameSchema(colander.Schema):
    
        name = colander.SchemaNode(colander.String('UTF-8'))

        email_address = colander.SchemaNode(colander.String('UTF-8'))

        message = colander.SchemaNode(
                colander.String(),
                validator=colander.Length(max=100),
                widget=deform.widget.TextAreaWidget(rows=10, cols=60))
    
    
    schema = nameSchema()
    
    form = deform.Form(schema, buttons=(u'send', u'cancel'))
    
    if 'send' in request.POST:
    
        try:
    
            controls = request.POST.items()
    
            values = form.validate(controls)
    
        except deform.ValidationFailure, e:
    
            # Validation Failure
    
            return {'form': e.render()}
    
    

    return {'form': form.render()}

@view_config(route_name='case-studies', layout='public', renderer='templates/case_studies.pt')
def case_studies(request):

    return {}

conn_err_msg = """\
Pyramid is having a problem using your SQL database.  The problem
might be caused by one of the following things:

1.  You may need to run the "initialize_stuff_your_boss_db" script
    to initialize your database tables.  Check your virtual
    environment's "bin" directory for this script and try to run it.

2.  Your database server may not be running.  Check that the
    database server referred to by the "sqlalchemy.url" setting in
    your "development.ini" file is running.

After you fix the problem, please restart the Pyramid application to
try it again.
"""

