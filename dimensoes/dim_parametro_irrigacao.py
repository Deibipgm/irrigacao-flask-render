def inserir_parametro(profundidade, cc, pm, sat, fd, densidade, eto, kc, eficiencia, umidade_disp, lamina_liquida, lamina_bruta, turno_rega, etc):
    novo = Parametro(
        profundidade=profundidade,
        cc=cc,
        pm=pm,
        sat=sat,
        fd=fd,
        densidade=densidade,
        eto=eto,
        kc=kc,
        eficiencia=eficiencia,
        umidade_disp=umidade_disp,
        lamina_liquida=lamina_liquida,
        lamina_bruta=lamina_bruta,
        turno_rega=turno_rega,
        etc=etc
    )
    db.session.add(novo)
    db.session.commit()

def listar_parametros():
    return Parametro.query.all()
