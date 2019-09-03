from flask import render_template
from app import app


@app.route("/")
@app.route("/index")
def index():
    #return "pagina principal"
    pag = "principal"
    return render_template('index.html', title='Principal', pag=pag)

@app.route("/semicondutores")
def semi():
    pag = "semicondutores"
    return render_template('semicondutores.html', title='Semis', pag=pag)

# incluir aqui as paginas que precisam ser colocadas
