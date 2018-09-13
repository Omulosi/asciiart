#
#
#

import os
import webapp2
import jinja2
from models import Art

# add jinja2 template engine
template_dir = os.path.join(os.path.dirname('__file__'), 'templates')
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir),
                               autoescape=True)

def render_str(template, **params):
    t = jinja_env.get_template(template)
    return t.render(params)

class BaseHandler(webapp2.RequestHandler):
    def render(self, template, **kw):
        self.response.out.write(render_str(template, **kw))

    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)


class MainHandler(BaseHandler):
    def get(self):
        self.render('index.html')

class NewArt(BaseHandler):
    def render_front(self, title="", art="", error=""):
        self.render('ascii.html', title=title, art=art, error=error)

    def get(self):
        self.render_front()

    def post(self):
        title = self.request.get("title")
        category = self.request.get("category")
        art = self.request.get("art")

        if (title and category and art):
            a = Art(title=title, category=category, art=art)
            a.put()
            self.redirect("/")
        else:
            error = "Invalid inputs!"
            self.render_front(title, art, error)

class Category(BaseHandler):
    def get(self, category):
        #arts = Art.gql("WHERE category = :category", category=category)
        arts = Art.all() # Returns a query object
        arts.filter("category = ", category).order("-created")
        self.render('category.html', arts=arts, category=category)


app = webapp2.WSGIApplication([('/?', MainHandler),
                               ('/add-art/?', NewArt),
                               ('/categories/([a-zA-Z]+)', Category)],
                               debug=True)
