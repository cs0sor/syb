from pyramid_layout.layout import layout_config

@layout_config(name='front_page', template='templates/front_page.pt')
@layout_config(name='public', template='templates/public_layout.pt')
class MainLayout(object):

    page_title = 'Stuff Your Boss'

    def __init__(self, context, request):

        self.context = context
        
        self.request = request
        
        self.home_url = request.application_url