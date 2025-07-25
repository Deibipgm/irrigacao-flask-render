from flask import Blueprint, request, jsonify, render_template, redirect, url_for
from dimensoes.dim_fazenda import Fazenda, inserir_fazenda
from dimensoes.dim_pivo import Pivo
from db.extensoes import db

fazenda_bp = Blueprint('fazenda', __name__)

@fazenda_bp.route('/fazenda', methods=['GET'])
def form_fazenda():
    return render_template('fazenda_form.html')

@fazenda_bp.route('/fazenda', methods=['POST'])
def criar_fazenda():
    try:
        data = request.form

        nome = data.get('nome')
        grupo = data.get('grupo')
        proprietario = data.get('proprietario')
        municipio = data.get('municipio')
        estado = data.get('estado')
        area_total_ha = data.get('area_total_ha')

        if not all([nome, municipio, estado, area_total_ha]):
            return jsonify({'error': 'Campos obrigatórios ausentes'}), 400

        area_total_ha = float(area_total_ha)
        if area_total_ha < 0:
            return jsonify({'error': 'Área total deve ser não-negativa'}), 400

        nova_fazenda = Fazenda(
            nome=nome,
            grupo=grupo,
            proprietario=proprietario,
            municipio=municipio,
            estado=estado,
            area_total_ha=area_total_ha
        )
        db.session.add(nova_fazenda)
        db.session.flush()

        nomes_pivo = data.getlist('pivo_nome[]')
        areas_ha = data.getlist('area_ha[]')
        status_list = data.getlist('status[]')

        for nome_pivo, area, status in zip(nomes_pivo, areas_ha, status_list):
            if nome_pivo.strip() and area.strip():
                novo_pivo = Pivo(
                    nome_pivo=nome_pivo,
                    area_ha=float(area),
                    status=status,
                    fazenda_id=nova_fazenda.fazenda_id
                )
                db.session.add(novo_pivo)

        db.session.commit()
        return redirect(url_for('fazenda.form_fazenda'))

    except ValueError as ve:
        db.session.rollback()
        return jsonify({'error': f'Erro de valor: {str(ve)}'}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': f'Erro interno: {str(e)}'}), 500