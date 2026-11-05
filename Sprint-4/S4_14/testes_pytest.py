def classificar_cvss(nota):
    if nota >= 9:
        return 'Crítica'
    if nota >= 7:
        return 'Alta'
    return 'Demais níveis'

def test_cvss_critico():
    assert classificar_cvss(9.8) == 'Crítica'

def test_cvss_alto():
    assert classificar_cvss(7.0) == 'Alta'

# A prova integrada da simulação está em test_risco.py no projeto principal.
