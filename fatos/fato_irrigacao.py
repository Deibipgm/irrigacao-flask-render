from db.extensoes import db
from datetime import date

class FatoIrrigacao(db.Model):
    __tablename__ = 'fato_irrigacao'
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.Date, default=date.today)
    fazenda_id = db.Column(db.Integer, nullable=False)
    pivo_id = db.Column(db.Integer, nullable=False)
    cultura_id = db.Column(db.Integer, nullable=False)
    safra = db.Column(db.String(20))
    ciclo = db.Column(db.Integer)
    et0_mm = db.Column(db.Float)
    chuva_mm = db.Column(db.Float)
    irrigado_mm = db.Column(db.Float)
    eficiencia = db.Column(db.Float, nullable=True)  # Calculado posteriormente

def inserir_irrigacao(data, fazenda, pivo, cultura, variedade, safra, ciclo, et0_mm, chuva_mm, irrigado_mm):
    novo = DadosIrrigacao(
        data=data,
        fazenda=fazenda,
        pivo=pivo,
        cultura=cultura,
        variedade=variedade,
        safra=safra,
        ciclo=ciclo,
        et0_mm=et0_mm,
        chuva_mm=chuva_mm,
        irrigado_mm=irrigado_mm
    )
    db.session.add(novo)
    db.session.commit()