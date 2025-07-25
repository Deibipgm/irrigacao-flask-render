from db.extensoes import db

class Projeto(db.Model):
    __tablename__ = 'fato_projeto'

    projeto_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fazenda_id = db.Column(db.Integer)
    pivo_id = db.Column(db.Integer)
    cultura_id = db.Column(db.Integer)
    safra = db.Column(db.String(20))
    ciclo = db.Column(db.String(50))
    data_inicio = db.Column(db.Date)
    profundidade_cm = db.Column(db.Float)
    densidade_aparente = db.Column(db.Float)
    cc_gg = db.Column(db.Float)
    pmp_gg = db.Column(db.Float)
    saturacao_gg = db.Column(db.Float)
    fator_disponibilidade = db.Column(db.Float)
    cc_mm = db.Column(db.Float)
    pm_mm = db.Column(db.Float)
    sat_mm = db.Column(db.Float)
    mi_mm = db.Column(db.Float)
    dta_mm = db.Column(db.Float)
    dra_mm = db.Column(db.Float)
    cta_mm = db.Column(db.Float)
    cra_mm = db.Column(db.Float)
    variedade = db.Column(db.String(100))