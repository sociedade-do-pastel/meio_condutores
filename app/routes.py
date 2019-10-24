from flask import render_template, request
from app import app
from flask_wtf import FlaskForm
from wtforms import SubmitField
from wtforms.validators import DataRequired
import logging
import sys

class QuestionarioForm(FlaskForm):
    def calcularRespostas(self, respostas):
        print(respostas, file=sys.stderr)
        corretas = [0, 0, 1, 0, 0, 1, 1, 1, 0, 0]
        contador = 0
        resposta_serv = []
        if len(respostas) != 10:
            return "Envie todos os dados corretamente", None
        else:
            for cont, itens in enumerate(respostas):
                if corretas[cont] == itens:
                    contador +=1
                    resposta_serv.append("Correta")
                else:
                    if itens == 1:
                        resposta_serv.append("Incorreta - Resposta correta = F")
                    else:
                        resposta_serv.append("Incorreta - Resposta correta = V")
            return contador, resposta_serv
                


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
@app.route("/questionario", methods=["GET", "POST"])
def questionario():
    form = QuestionarioForm()
    id = request.args.get("id")
    if request.method == "POST":
        try:
            listaresp = [int(values) for values in request.form.values()]
            respostas, cor_incor = form.calcularRespostas(listaresp)
        except:
            respostas = "Envie todos os dados corretamente"
            cor_incor = None
        return render_template("questionario.html", title="Questionario", perg = respostas, percent= respostas * 10, form=form, cor= cor_incor, id = id)
    else:
        return render_template("questionario.html", title="Questionario", form = form, id = id)
