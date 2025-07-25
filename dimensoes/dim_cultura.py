from db.extensoes import db

class Cultura(db.Model):
    __tablename__ = 'dim_cultura'
    __table_args__ = {'extend_existing': True}

    cultura_id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    variedade = db.Column(db.String(100), nullable=True)
    ciclo = db.Column(db.Integer, nullable=True)
    kc = db.Column(db.Float, nullable=True)

def inserir_cultura(nome, variedade, ciclo, kc):
    nova_cultura = Cultura(
        nome=nome,
        variedade=variedade,
        ciclo=ciclo,
        kc=kc
    )
    db.session.add(nova_cultura)
    db.session.commit()

def listar_culturas():
    return [
        {
            'cultura_id': cultura.cultura_id,
            'nome': cultura.nome,
            'variedade': cultura.variedade,
            'ciclo': cultura.ciclo,
            'kc': cultura.kc
        }
        for cultura in Cultura.query.order_by(Cultura.nome).all()
    ]