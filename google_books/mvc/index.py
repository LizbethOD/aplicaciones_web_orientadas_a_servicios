import web 
import requests 
import json

render = web.template.render("mvc/")

class Index():

  def GET(self):
    data = None
    return render.index(data)

  def POST(self):
    form = web.input()
    book_name = form.book_name
    
    result = requests.get("https://www.googleapis.com/books/v1/volumes?q="+book_name)

    book = result.json()

    items = book["items"]

    encoded = json.dumps(items)
    decoded = json.loads(encoded)

    url = decoded[0]["volumeInfo"]["infoLink"]
    url_imagen = decoded[0]["volumeInfo"]["imageLinks"]["smallThumbnail"]
    nom_actor = str(decoded[0]["volumeInfo"]["authors"])

    link = "<a href='"+url+"'>"+book_name+"</a>"
    imagen = "<img src='"+url_imagen+"'/>"
    autor =  "<label>'"+nom_actor+"'<label>"
    
    data= {
      "nom_libro": "Nombre del libro: "+book_name, "imagen": imagen, "autor": "Autor del libro: "+autor, "url": "Link para poder comprarlo: "+link
   }
    
    return render.index(data)