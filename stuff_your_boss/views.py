from pyramid.view import view_config
import colander
import deform
from pyramid_mailer import get_mailer
from pyramid_mailer.message import Message
from webob import exc

@view_config(
    route_name='home',
    layout='front_page',
    renderer='templates/home.pt')
def home(request):
    return {}

@view_config(route_name='test', layout='public', renderer='templates/test.pt')
def test(request):
    return {}


@view_config(route_name='about', layout='public', renderer='templates/about.pt')
def about(request):
    return {}

@view_config(
    route_name='contact',
    layout='public',
    renderer='templates/contact.pt')
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

        mailer = get_mailer(request)

        message = Message(
            subject="Message from SYB site",
            sender="admin@stuffyourboss.org.uk",
            recipients=["newcastlesolfed@gmail.com"],
            body="From: %s %s \n\n %s" % (
                values['name'],
                values['email_address'],
                values['message']))

        mailer.send(message)

        return exc.HTTPSeeOther(location=request.route_url('thanks'))

    if 'cancel' in request.POST:

        return exc.HTTPSeeOther(location=request.route_url('home'))

    return {'form': form.render()}

@view_config(
    route_name='case-studies',
    layout='public',
    renderer='templates/case_studies.pt')
def case_studies(request):
    return {}

@view_config(
    route_name='thanks',
    layout='public',
    renderer='templates/thanks.pt'
    )
def thanks(request):
    return{}

