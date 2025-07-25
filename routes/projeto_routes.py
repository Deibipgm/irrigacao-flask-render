from flask import Blueprint, render_template, request, redirect, url_for
from fatos.fato_projeto import Projeto
from dimensoes.dim_fazenda import Fazenda
from dimensoes.dim_pivo import Pivo
from dimensoes.dim_cultura import Cultura
from db.extensoes import db
from datetime import datetime

projeto_bp = Blueprint('projeto', __name__)

@projeto_bp.route('/projeto', methods=['GET', 'POST'])
def cadastrar_projeto():
    if request.method == 'POST':
        dados = request.form

        # Buscar o próximo ID disponível manualmente
        ultimo_projeto = Projeto.query.order_by(Projeto.projeto_id.desc()).first()
        proximo_id = 1 if not ultimo_projeto else ultimo_projeto.projeto_id + 1


        projeto = Projeto(
            projeto_id=proximo_id,
            fazenda_id=dados['fazenda_id'],
            pivo_id=dados['pivo_id'],
            cultura_id=dados['cultura_id'],
            safra=dados['safra'],
            data_inicio=datetime.strptime(dados['data_inicio'], '%Y-%m-%d'),
            ciclo=dados['ciclo'],
            variedade=dados['variedade'],
            profundidade_cm=dados['profundidade_cm'],
            densidade_aparente=dados['densidade_aparente'],
            cc_gg=dados['cc_gg'],
            pmp_gg=dados['pmp_gg'],
            saturacao_gg=dados['saturacao_gg'],
            fator_disponibilidade=dados['fator_disponibilidade'],
            cc_mm=dados['cc_mm'] if 'cc_mm' in dados else None,
            pm_mm=dados['pm_mm'] if 'pm_mm' in dados else None,
            sat_mm=dados['sat_mm'] if 'sat_mm' in dados else None,
            mi_mm=dados['mi_mm'] if 'mi_mm' in dados else None,
        )

        db.session.add(projeto)
        db.session.commit()
        return redirect(url_for('projeto.listar_projetos'))

    fazendas = Fazenda.query.all()
    pivos = Pivo.query.all()
    culturas = Cultura.query.all()
    return render_template('form_projeto.html', fazendas=fazendas, pivos=pivos, culturas=culturas)

@projeto_bp.route("/projeto/listar")
def listar_projetos():
    projetos = Projeto.query.all()
    return render_template("listar_projetos.html", projetos=projetos)