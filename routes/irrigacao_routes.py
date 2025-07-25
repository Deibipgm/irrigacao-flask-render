
from flask import Blueprint, render_template, request, redirect, url_for, flash
from datetime import datetime
from fatos.fato_irrigacao import inserir_irrigacao
from fatos.fato_projeto import Projeto
from dimensoes.dim_fazenda import Fazenda
from dimensoes.dim_pivo import Pivo
from dimensoes.dim_cultura import Cultura

irrigacao_bp = Blueprint('irrigacao', __name__)

@irrigacao_bp.route('/irrigacao', methods=['GET'])
def form_irrigacao():
    fazendas = Fazenda.query.all()
    pivos = Pivo.query.all()
    culturas = Cultura.query.all()
    return render_template('irrigacao_form.html', fazendas=fazendas, pivos=pivos, culturas=culturas)

@irrigacao_bp.route('/irrigacao', methods=['POST'])
def criar_irrigacao():
    data = request.form
    data_lancamento = datetime.strptime(data['data'], '%Y-%m-%d').date()

    fazenda = Fazenda.query.filter_by(fazenda_id=data['fazenda']).first()
    if not fazenda:
        flash("Fazenda não encontrada.", "danger")
        return redirect(url_for("irrigacao.form_irrigacao"))

    pivo = Pivo.query.filter_by(pivo_id=data['pivo']).first()
    if not pivo:
        flash("Pivô não encontrado.", "danger")
        return redirect(url_for("irrigacao.form_irrigacao"))

    cultura = Cultura.query.filter_by(cultura_id=data['cultura']).first()
    if not cultura:
        flash("Cultura não encontrada.", "danger")
        return redirect(url_for("irrigacao.form_irrigacao"))

    projeto = Projeto.query.filter_by(
        fazenda_id=fazenda.fazenda_id,
        pivo_id=pivo.pivo_id,
        cultura_id=cultura.cultura_id,
        safra=data['safra']
    ).first()

    if not projeto:
        flash("Projeto não encontrado para os dados informados.", "danger")
        return redirect(url_for("irrigacao.form_irrigacao"))

    ciclo = (data_lancamento - projeto.data_inicio).days + 1

    inserir_irrigacao(
        data['data'],
        fazenda.fazenda_id,
        pivo.pivo_id,
        cultura.cultura_id,
        data['safra'],
        ciclo,
        float(data.get('et0_mm') or 0),
        float(data.get('chuva_mm') or 0),
        float(data.get('irrigado_mm') or 0)
    )

    flash("Registro de irrigação salvo com sucesso!", "success")
    return redirect(url_for('irrigacao.form_irrigacao'))