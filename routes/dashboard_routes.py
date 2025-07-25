from flask import Blueprint, render_template
from db.extensoes import db
from sqlalchemy import text

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/dashboard')
def dashboard():
    conn = db.engine.connect()

    # ✅ Pivôs Ativos (corrigido uso de aspas)
    ativos = conn.execute(text("SELECT COUNT(*) FROM dim_pivo WHERE status = 'Ativo'")).scalar()

    # ✅ Área Plantada (ha) considerando apenas pivôs ativos
    area_ha = conn.execute(text("SELECT SUM(area_ha) FROM dim_pivo WHERE status = 'Ativo'")).scalar()
    area_ha = area_ha if area_ha else 0

    # ⚠️ Eficiência Média (Exemplo: 0% até fórmula real ser definida)
    eficiencia = 0  # TODO: calcular eficiência média real com base em dados disponíveis

    # ✅ Demanda Hídrica média dos últimos 7 dias
    demanda_hidrica = conn.execute(text(
        "SELECT ROUND(AVG(et0_mm), 2) FROM fato_irrigacao_diaria WHERE data >= CURDATE() - INTERVAL 7 DAY"
    )).scalar()
    demanda_hidrica = demanda_hidrica if demanda_hidrica else 0

    return render_template('dashboard.html', 
        ativos=ativos,
        area_ha=area_ha,
        eficiencia=eficiencia,
        demanda_hidrica=demanda_hidrica
    )
