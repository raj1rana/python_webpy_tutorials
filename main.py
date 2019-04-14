import web
#importing web from venv
urls = (
    '/', 'index'      # here are the URLS mapping / stands for root URL and 'index is the resource it will call'
)
render = web.template.render("resources")     # render is a veriable that will render the web.template and "is the foldername"
class index:                              # this is a class index
    def GET(self, name= "raj" , age = 23):     # this is a GET function with the name perimeter wih name = "raj"
        return render.main(name, age)   # this is what will be printed to the web browser

# this part is responsile to run the App where the name == "main" then run the app
if __name__ == "__main__":
      # render is a veriable that will render the web.template and "is the foldername"
    app = web.application(urls, globals())   #here we create a variable app and this is a finction web.application(urls,global()) global is afunction
    app.run() # to run the app