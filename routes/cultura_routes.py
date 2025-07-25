from flask import Blueprint, request, jsonify, render_template, redirect, url_for
from dimensoes.dim_cultura import inserir_cultura, listar_culturas

cultura_bp = Blueprint('cultura', __name__)

@cultura_bp.route('/cultura', methods=['GET'])
def form_cultura():
    return render_template('cultura_form.html')

@cultura_bp.route('/cultura', methods=['POST'])
def criar_cultura():
    data = request.get_json() if request.is_json else request.form

    inserir_cultura(
        data['nome'],
        data['variedade'],
        int(data['ciclo']),
        float(str(data['kc']).replace(',', '.'))
    )
    return redirect(url_for('cultura.form_cultura'))

@cultura_bp.route('/cultura/json', methods=['GET'])
def obter_culturas():
    return jsonify(listar_culturas())