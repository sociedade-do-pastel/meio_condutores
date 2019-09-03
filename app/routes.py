from app import app

@app.route("/")
@app.route("/index")
def index():
    return "pagina principal"

@app.route("/semicondutores")
def semi():
    return "semicondutores explicação"

# incluir aqui as paginas que precisam ser colocadas
