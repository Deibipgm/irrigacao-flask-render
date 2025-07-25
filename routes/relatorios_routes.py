
from flask import Blueprint, render_template, send_file, request
from db.extensoes import db
from sqlalchemy import text
import pandas as pd
from io import BytesIO
from datetime import datetime

relatorios_bp = Blueprint("relatorios", __name__)

@relatorios_bp.route("/relatorios", methods=["GET", "POST"])
def relatorios():
    tipo_relatorio = None
    fazendas = db.session.execute(text("SELECT fazenda_id, nome FROM dim_fazenda")).fetchall()

    if request.method == "POST":
        tipo_relatorio = request.form.get("tipo_relatorio")
        return render_template("relatorios.html", tipo_relatorio=tipo_relatorio, fazendas=fazendas)

    return render_template("relatorios.html", tipo_relatorio=None, fazendas=fazendas)


@relatorios_bp.route("/relatorios/irrigacao/excel", methods=["POST"])
def exportar_excel_irrigacao():
    fazenda_id = request.form.get("fazenda_id")
    safra = request.form.get("safra")
    data_inicio = request.form.get("data_inicio")
    data_fim = request.form.get("data_fim")

    filtros = []
    if fazenda_id:
        filtros.append(f"i.fazenda = {fazenda_id}")
    if safra:
        filtros.append(f"i.safra = '{safra}'")
    if data_inicio:
        filtros.append(f"i.data >= '{data_inicio}'")
    if data_fim:
        filtros.append(f"i.data <= '{data_fim}'")

    where_clause = " AND ".join(filtros)
    if where_clause:
        where_clause = "WHERE " + where_clause

    sql = text(f'''
        SELECT
            i.id_fato,
            f.nome AS fazenda,
            pv.nome_pivo AS pivo,
            c.nome AS cultura,
            i.data,
            i.safra,
            i.ciclo,
            i.et0_mm,
            i.chuva_mm,
            i.irrigado_mm,
            i.variedade
        FROM fato_irrigacao_diaria i
        JOIN dim_fazenda f ON i.fazenda = f.fazenda_id
        JOIN dim_pivo pv ON i.pivo = pv.pivo_id
        JOIN dim_cultura c ON i.cultura = c.cultura_id
        {where_clause}
    ''')

    with db.engine.connect() as conn:
        df = pd.read_sql(sql, conn)

    output = BytesIO()
    with pd.ExcelWriter(output, engine="xlsxwriter") as writer:
        df.to_excel(writer, index=False, sheet_name="Irrigacao")
    output.seek(0)
    return send_file(output, download_name=f"relatorio_irrigacao_{datetime.now().strftime('%Y-%m-%d')}.xlsx", as_attachment=True)


@relatorios_bp.route("/relatorios/projeto/excel")
def exportar_excel_projeto():
    sql = text("""
        SELECT
            p.projeto_id,
            f.nome AS fazenda,
            pv.nome_pivo AS pivo,
            c.nome AS cultura,
            p.data_inicio,
            p.safra,
            p.profundidade_cm,
            p.densidade_aparente,
            p.cc_gg,
            p.pmp_gg,
            p.saturacao_gg,
            p.cc_mm,
            p.pm_mm,
            p.sat_mm,
            p.mi_mm,
            p.variedade
        FROM fato_projeto p
        JOIN dim_fazenda f ON p.fazenda_id = f.fazenda_id
        JOIN dim_pivo pv ON p.pivo_id = pv.pivo_id
        JOIN dim_cultura c ON p.cultura_id = c.cultura_id
    """)
    with db.engine.connect() as conn:
        df = pd.read_sql(sql, conn)

    output = BytesIO()
    with pd.ExcelWriter(output, engine="xlsxwriter") as writer:
        df.to_excel(writer, index=False, sheet_name="Projeto")
    output.seek(0)
    return send_file(output, download_name=f"relatorio_projeto_{datetime.now().strftime('%Y-%m-%d')}.xlsx", as_attachment=True)
