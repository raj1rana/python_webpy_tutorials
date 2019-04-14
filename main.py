import web
#importing web from venv
urls = (
    '/', 'index'      # here are the URLS mapping / stands for root URL and 'index is the resource it will call'
)
class index:                              # this is a class index
    def GET(self, name= "raj"):     # this is a GET function with the name perimeter wih name = "raj"
        return "<h1>Hello   "+ name + '</h1>   how are you'   # this is what will be printed to the web browser

# this part is responsile to run the App where the name == "main" then run the app
if __name__ == "__main__":
    app = web.application(urls, globals())   #here we create a variable app and this is a finction web.application(urls,global()) global is afunction
    app.run() # to run the app