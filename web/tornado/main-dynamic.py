import tornado.web
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("hello.html", name="Visitor")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ], template_path="templates")

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    print("Server running at http://localhost:8888")
    tornado.ioloop.IOLoop.current().start()