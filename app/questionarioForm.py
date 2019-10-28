import sys
class QuestionarioForm():
    def calcularRespostas(self, respostas):
        corretas = [0, 0, 1, 0, 0, 1, 1, 1, 0, 0]
        contador = 0
        resposta_serv = []
        if len(respostas) != len(corretas):
            return "Envie todos os dados corretamente :DD", None, None
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
        percent = (contador/len(respostas))*100

        return contador, resposta_serv, percent
