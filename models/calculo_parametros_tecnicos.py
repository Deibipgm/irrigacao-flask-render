# calculos_irrigacao.py

def calcular_umidade_disponivel(cc, pm, densidade, profundidade_cm):
    """
    Calcula a Umidade Disponível (UA) no solo.

    Fórmula:
        UA = (CC - PM) * Densidade * 10 * Profundidade

    Parâmetros:
        cc (float): Capacidade de Campo (g/g)
        pm (float): Ponto de Murcha (g/g)
        densidade (float): Densidade aparente do solo (g/cm³)
        profundidade_cm (float): Profundidade efetiva das raízes (cm)

    Retorna:
        float: Umidade Disponível (mm)
    """
    return (cc - pm) * densidade * 10 * profundidade_cm


def calcular_lamina_irrigacao(umidade_disponivel, fator_disponibilidade):
    """
    Calcula a Lâmina de Irrigação (LI).

    Fórmula:
        LI = UA * FD

    Parâmetros:
        umidade_disponivel (float): Umidade Disponível (mm)
        fator_disponibilidade (float): Fator de disponibilidade (0 a 1)

    Retorna:
        float: Lâmina líquida de irrigação (mm)
    """
    return umidade_disponivel * fator_disponibilidade


def calcular_etc(eto, kc):
    """
    Calcula a Evapotranspiração da Cultura (ETc).

    Fórmula:
        ETc = ET0 * Kc

    Parâmetros:
        eto (float): Evapotranspiração de referência (mm/dia)
        kc (float): Coeficiente da cultura

    Retorna:
        float: ETc (mm/dia)
    """
    return eto * kc


def calcular_turno_irrigacao(lamina_liquida, etc):
    """
    Calcula o Turno de Irrigação.

    Fórmula:
        Turno = LI / ETc

    Parâmetros:
        lamina_liquida (float): Lâmina de irrigação líquida (mm)
        etc (float): ETc da cultura (mm/dia)

    Retorna:
        float: Turno (dias)
    """
    return round(lamina_liquida / etc, 2) if etc > 0 else 0


def calcular_lamina_bruta(lamina_liquida, eficiencia):
    """
    Calcula a Lâmina Bruta Aplicada.

    Fórmula:
        LB = LI / Eficiência

    Parâmetros:
        lamina_liquida (float): Lâmina líquida de irrigação (mm)
        eficiencia (float): Eficiência do sistema (0 a 1)

    Retorna:
        float: Lâmina bruta (mm)
    """
    return round(lamina_liquida / eficiencia, 2) if eficiencia > 0 else 0


# Exemplo de uso isolado
if __name__ == "__main__":
    # Parâmetros simulados
    cc = 0.32
    pm = 0.18
    densidade = 1.35
    profundidade = 30  # cm
    fator_disponibilidade = 0.5
    eficiencia = 0.85
    eto = 5.2
    kc = 1.1

    ua = calcular_umidade_disponivel(cc, pm, densidade, profundidade)
    li = calcular_lamina_irrigacao(ua, fator_disponibilidade)
    etc = calcular_etc(eto, kc)
    turno = calcular_turno_irrigacao(li, etc)
    lb = calcular_lamina_bruta(li, eficiencia)

    print("Umidade Disponível:", round(ua, 2), "mm")
    print("Lâmina de Irrigação:", round(li, 2), "mm")
    print("ETc:", round(etc, 2), "mm")
    print("Turno de Irrigação:", turno, "dias")
    print("Lâmina Bruta:", lb, "mm")

