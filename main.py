from flask import (Flask,
                   render_template,
                   request,
                   make_response,
                   redirect
                   )
from models import artwork
app = Flask('app')
artwork.initialize()


@app.route('/')
def index():
    list_art = artwork.Artwork.select()
    results = []
    for art in list_art:
        art_item = {
            'description': art.description,
            'thumbnail_link': art.thumbnail_link,
            'fullimage_link': art.fullimage_link
        }
        results.append(art_item)
    return render_template("index.html", images=results)


app.run(debug=True, host='0.0.0.0', port=8080)