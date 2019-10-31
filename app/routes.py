from flask import render_template, request
from app import app
from app.questionarioForm import QuestionarioForm
from app.progForm import ProgForm
import logging
import sys

@app.route("/")
@app.route("/index")
def index():
    #return "pagina principal"
    pag = "principal"
    return app.send_static_file('index.html')

@app.route("/semicondutores")
def semi():
    pag = "semicondutores"
    return render_template('semicondutores.html', title='Semis', pag=pag)

# incluir aqui as paginas que precisam ser colocadas
@app.route("/questionario", methods=["GET", "POST"])
def questionario():
    form = QuestionarioForm()
    id = request.args.get("id")
    percent = ""
    if request.method == "POST":
        try:
            listaresp = [int(values) for values in request.form.values()]
            respostas, cor_incor, percent = form.calcularRespostas(listaresp)
        except:
            respostas = "Envie todos os dados corretamente"
            cor_incor = None
            percent = 0
        return render_template("questionario.html", title="Questionario", perg = respostas, percent = percent, form=form, cor= cor_incor, id = id)
    else:
        return render_template("questionario.html", title="Questionario", form = form, id = id)


@app.route("/programa", methods=["GET", "POST"])
def programa():
    form = ProgForm()
    if form.validate_on_submit():
        form.calcularItens( resistencia = form.ohm.data,  resistividade = form.resist.data, ar = form.area.data,  comprimento = form.comp.data,  condutividade = form.condut.data)
        return render_template("programa.html", form = form, check = 1)
    return render_template("programa.html", form=form)
