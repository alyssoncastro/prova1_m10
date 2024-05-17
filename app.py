from flask import Flask, request, jsonify, abort
from models import Pedido

app = Flask(__name__)


pedidos_db = {}
next_id = 1


@app.route('/novo', methods=['POST'])
def criar_pedido():
    global next_id
    dados = request.get_json()
    if not dados or 'nome' not in dados or 'email' not in dados or 'descricao' not in dados:
        abort(400, description="Dados do pedido incompletos")
    
    pedido = Pedido(next_id, dados['nome'], dados['email'], dados['descricao'])
    pedidos_db[next_id] = pedido
    next_id += 1
    return jsonify({"id": pedido.id}), 201

@app.route('/pedidos', methods=['GET'])
def listar_pedidos():
    return jsonify([pedido.to_dict() for pedido in pedidos_db.values()]), 200

@app.route('/pedidos/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def manipular_pedido(id):
    pedido = pedidos_db.get(id)
    if not pedido:
        abort(404, description="Pedido não encontrado")

    if request.method == 'GET':
        return jsonify(pedido.to_dict()), 200

    elif request.method == 'PUT':
        dados = request.get_json()
        if not dados:
            abort(400, description="Dados do pedido incompletos")
        pedido.nome = dados.get('nome', pedido.nome)
        pedido.email = dados.get('email', pedido.email)
        pedido.descricao = dados.get('descricao', pedido.descricao)
        return jsonify(pedido.to_dict()), 200

    elif request.method == 'DELETE':
        del pedidos_db[id]
        return '', 204

if __name__ == '__main__':
    app.run(debug=True)
