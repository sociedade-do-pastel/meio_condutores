from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DecimalField
from wtforms.validators import NumberRange, Optional 
import sys
class ProgForm(FlaskForm):
    ohm = DecimalField("Resistência",default=None, validators=[NumberRange(min = 0, message="Não insira valores negativos" ), Optional()])
    resist =  DecimalField("Resistividade",default =None, validators=[NumberRange(min = 0, message="Não insira valores negativos" ), Optional()])
    area = DecimalField("Área",default = None, validators=[NumberRange(min = 0, message="Não insira valores negativos" ), Optional()])
    comp = DecimalField("Comprimento",default=None, validators=[NumberRange(min = 0, message="Não insira valores negativos" ), Optional()])
    condut = DecimalField("Condutividade",default=None, validators=[NumberRange(min = 0, message="Não insira valores negativos" ), Optional()])
    calcular = SubmitField("Calcular! ")
    
    def calcularItens(self, **kwargs):
        self.__dict__.update(kwargs)  
        try:
            if self.resistividade:
                if not self.resistencia:
                    self.resistencia = (self.condutividade* self.comprimento) / self.ar
                elif not self.comprimento:
                    self.comprimento = (self.ar * self.resistencia) / self.condutividade
                elif not self.resistencia:
                    self.resistencia = (self.condutividade * self.comprimento) / self.ar
            else:
                if self.condutividade:
                    self.resistividade = 1 / self.condutividade
                else:
                    self.resistividade = (self.ar * self.resistencia )/ self.comprimento
        except:
            pass
        try:
            if not self.condutividade:
                self.condutividade = 1 / self.resistividade 
        except:
            pass
        

        try:
            if self.condutividade < 1e-6:
                self.tipo_mat = "O material é isolante"
            elif self.condutividade >= 1e-6 and self.condutividade < 1e2:
                self.tipo_mat = "O material é semicondutor"
            elif self.condutividade >= 1e2:
                self.tipo_mat = "O material é um metal"
            else:
                self.tipo_mat = "Dados inválidos"
        except:
            pass
