from db.extensoes import db


class Fazenda(db.Model):
    __tablename__ = 'dim_fazenda'
    __table_args__ = {'extend_existing': True}

    fazenda_id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    grupo = db.Column(db.String(100), nullable=True)
    proprietario = db.Column(db.String(100), nullable=True)
    municipio = db.Column(db.String(100), nullable=False)
    estado = db.Column(db.String(2), nullable=False)
    area_total_ha = db.Column(db.Float, nullable=False)

def inserir_fazenda(nome, grupo, proprietario, municipio, estado, area_total_ha):
    nova_fazenda = Fazenda(
        nome=nome,
        grupo=grupo,
        proprietario=proprietario,
        municipio=municipio,
        estado=estado,
        area_total_ha=area_total_ha
    )
    db.session.add(nova_fazenda)
    db.session.commit()

def listar_fazendas():
    return Fazenda.query.all()