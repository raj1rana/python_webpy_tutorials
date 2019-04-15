#import area
import web


#urls and their mapping
urls = (
    '/' ,'home'
)


#classes/routes
class home:
    def GET(self):
        return "home"

#app aggeriagation and functions
if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
