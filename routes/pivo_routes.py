from flask import Blueprint, request, jsonify, render_template, redirect, url_for
from models.dim_pivo import inserir_pivo, listar_pivos
from models.dim_fazenda import Fazenda  # novo import
from extensoes import db

pivo_bp = Blueprint('pivo', __name__)

@pivo_bp.route('/pivo', methods=['GET'])
def form_pivo():
    fazendas = Fazenda.query.order_by(Fazenda.nome).all()  # consulta para popular o select
    return render_template('pivo_form.html', fazendas=fazendas)

@pivo_bp.route('/pivo', methods=['POST'])
def criar_pivo():
    data = request.form
    inserir_pivo(
        data['nome_pivo'],
        int(data['fazenda_id']),
        float(data['area_ha']),
        data['tipo_sistema'],
        data['status']
    )
    return redirect(url_for('pivo.form_pivo'))

@pivo_bp.route('/pivo/json', methods=['GET'])
def obter_pivos():
    return jsonify(listar_pivos())

