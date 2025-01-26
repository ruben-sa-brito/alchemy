from flask import Flask, jsonify, request
from entidades import Tema
from dao import TemaDAO
app =Flask(__name__)

dao_tema = TemaDAO()

@app.route('/tema')
def get_tema():
    temas = []
    for t in dao_tema.obterTodos():
        temas.append({"tema_id":t.tema_id, "tema_nome":t.tema_nome})
    return jsonify(temas)

@app.route('/tema', methods=['POST'])
def add_tema():
    tema_json = request.get_json()
    tema = Tema(tema_id=tema_json['tema_id'],
                tema_nome=tema_json['tema_nome'])
    dao_tema.incluir(tema)

    return '', 204

if __name__ == '__main__':
    app.run(debug=True)