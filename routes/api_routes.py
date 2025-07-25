from flask import Blueprint, jsonify
from dimensoes.dim_pivo import Pivo
from dimensoes.dim_cultura import Cultura

api_bp = Blueprint('api', __name__)

@api_bp.route('/api/pivos/<int:fazenda_id>')
def get_pivos_por_fazenda(fazenda_id):
    pivos = Pivo.query.filter_by(fazenda_id=fazenda_id).all()
    return jsonify([{'id': p.pivo_id, 'nome': p.nome_pivo} for p in pivos])

@api_bp.route('/api/variedades/<int:cultura_id>')
def get_variedades_por_cultura(cultura_id):
    culturas = Cultura.query.filter_by(cultura_id=cultura_id).all()
    return jsonify([{'id': c.cultura_id, 'variedade': c.variedade} for c in culturas])