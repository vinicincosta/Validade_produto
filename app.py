from flask import Flask, jsonify
from flask_pydantic_spec import FlaskPydanticSpec
from datetime import datetime
from dateutil.relativedelta import relativedelta


app = Flask(__name__)
spec = FlaskPydanticSpec('flask', title='API de Validade de Produtos', version='1.0.0')
spec.register(app)
tempo = datetime.now()



@app.route('/', methods=['GET'])
def pagina_inicial():
    return 'Página de Validade de Produtos'


@app.route("/validade/<data_str>/<valor>/<unidade>", methods=["GET"])
def calcular_validade(data_str, valor, unidade, ):
    """
    Calcula a data de validade de um produto com base na data de fabricação e no tempo informado.

    :param data_str: Ano da data de fabricação./ Mês da data de fabricação./Dia da data de fabricação.
    :param valor: Quantidade de tempo a adicionar.
    :param unidade: Unidade de tempo (dias, semanas, meses, anos).

    :return: JSON contendo a data de cadastro, validade em diferentes unidades e data de vencimento.
    """
    try:
        data_entrada = datetime.strptime(data_str, '%d-%m-%Y')

        # Criar a data de fabricação
        data_fabricacao = datetime(data_entrada.year, data_entrada.month, data_entrada.day)

        # Definir os incrementos com base na unidade fornecida
        unidades_validas = {
            "dias": relativedelta(days=int(valor)),
            "semanas": relativedelta(weeks=int(valor)),
            "meses": relativedelta(months=int(valor)),
            "anos": relativedelta(years=int(valor)),
        }

        # data atual
        data_atual = datetime.now()

        # Calcular a data de validade
        data_validade = data_fabricacao + unidades_validas[unidade]

        # Calcular validade em todas as unidades
        diferenca_dias = (data_validade - data_fabricacao).days
        diferenca_semanas = diferenca_dias // 7
        diferenca_meses = diferenca_dias // 30
        diferenca_anos = diferenca_dias // 365

        # Retornar resposta JSON
        return jsonify({
            'data_atual': data_atual.strftime("%d/%m/%Y | %H:%M:%S"),
            "data_validade": data_validade.strftime("%d/%m/%Y"),
            'data de cadastro': data_fabricacao.strftime("%d/%m/%Y | %H:%M:%S"),
            "validade": {
                "dias": diferenca_dias,
                "semanas": diferenca_semanas,
                "meses": diferenca_meses,
                "anos": diferenca_anos
            },

        })

    except ValueError:
        return jsonify({"erro": "Os parâmetros inseridos são inválidos!"}), 400

if __name__ == '__main__':
    app.run(debug=True)


