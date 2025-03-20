# importar biblioteca
from flask import Flask, jsonify, render_template
# importe para documentacao
from flask_pydantic_spec import FlaskPydanticSpec
import datetime
from datetime import datetime
from dateutil.relativedelta import relativedelta

# [flask routes] para listar rotas da api

# criar variavel para receber a classe Flask
app = Flask(__name__)

#   documentacao OpenAPI
spec = FlaskPydanticSpec('flask',
                         title='First API - SENAI',
                         version='1.0.0')
spec.register(app)

@app.route('/validadealunos')
def validado():
    prazo = 12
    meses = datetime.today()+relativedelta(months=prazo)
    # years=
    anos = ''
    # weeks=
    semanas = ''
    # days=
    dias = ''

    return (f'"antes" - {datetime.today().strftime("%d-%m-%Y")}, '
            f'"dias"- {dias}, '
            f'"semanas"- {semanas}, '
            f'"meses"- {meses},'
            f'"anos"- {anos}')


# iniciar servidor
if __name__ == '__main__':
    app.run(debug=True)
