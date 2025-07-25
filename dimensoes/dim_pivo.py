from db.extensoes import db
from dimensoes.dim_fazenda import Fazenda

class Pivo(db.Model):
    __tablename__ = 'dim_pivo'
    __table_args__ = {'extend_existing': True}

    pivo_id = db.Column(db.Integer, primary_key=True)
    nome_pivo = db.Column(db.String(100), nullable=False)
    area_ha = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(20), nullable=False)
    fazenda_id = db.Column(db.Integer, db.ForeignKey('dim_fazenda.fazenda_id'), nullable=False)

    fazenda = db.relationship('Fazenda')  # relacionamento sem back_populates