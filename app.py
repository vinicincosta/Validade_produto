# Importar bibliotecas
import datetime

from flask import Flask, jsonify
from flask_pydantic_spec import FlaskPydanticSpec
from datetime import datetime
from dateutil.relativedelta import relativedelta

# Criar a variável para receber a classe Flask
app = Flask(__name__)
tempo = datetime.now()
# Documentação OpenAPI
spec = FlaskPydanticSpec('flask',
                         title='First API - SENAI',
                         version='1.0.0')
spec.register(app)


@app.route('/validadealunos/ano/mes/dia')
def validade_alunos(dia,mes,ano):
    dia_ = int(dia)
    mes_ = int(mes)
    ano_ = int(ano)
    data_informada = datetime.datetime(ano,mes, dia)

    prazo_em_meses = 12  # Prazo de validade em meses
    hoje = datetime.today()  # Data de hoje
    validade = hoje + relativedelta(months=prazo_em_meses)  # Data futura após o prazo

    # Calculos
    delta = validade - hoje
    dias = delta.days  # Total de dias
    semanas = dias // 7  # Total de semanas
    anos = delta.days // 365  # Aproximação do número de anos


    return jsonify ({
        "data_atual": hoje.strftime("%d-%m-%Y"),
        "data_validade": validade.strftime("%d-%m-%Y"),
        "dias": dias,
        "semanas": semanas,
        "meses": prazo_em_meses,
        "anos": anos
    })


if __name__ == '__main__':
    app.run(debug=True)
