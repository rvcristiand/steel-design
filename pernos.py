from math import pi

def Ab(d):
    """
    Calcula el área nominal del vástago del perno sin roscas.

    Parameters
    ----------
    d : float
        Diámetro del perno.

    Returns
    -------
    float
        Área del perno.
    """
    return pi * d**2 / 4

def Fnv(perno):
    """
    Devuelve la resistencia nominal a cortante del perno en uniones tipo
    aplastamiento.

    Parameters
    ----------
    perno : string
        Descripción del perno.

    Returns
    -------
    int
        Resistencia nominal a cortante del perno.
    """
    resistencia_cortante = {}
    resistencia_cortante['A307'] = 188
    resistencia_cortante['A325N'] = 370
    resistencia_cortante['A325X'] = 460
    resistencia_cortante['A490N'] = 460
    resistencia_cortante['A490X'] = 580

    return resistencia_cortante[perno]

def φR_n(φ, Fnv, Ab):
    """
    Calcula la resistencia de diseño a cortante.

    Parameters
    ----------
    φ : float
        Factor de resistencia.
    Fnv : float
        Resistencia nominal a cortante.
    Ab : float
        Área nominal del vástago sin rosca.
    """
    return φ * Fnv * Ab

if __name__ == '__main__':
    # pernos 7/8"
    perno_7_8 = {}

    diameter = perno_7_8['diameter'] = 7/8 * 25.4  # mm
    area = perno_7_8['area'] = Ab(diameter)

    calidades = [
        'A307',
        'A325N',
        'A325X',
        'A490N',
        'A490X'
    ]

    print('Perno 7/8"')
    print(f"diámetro: {diameter:.3f} mm")
    print(f"área: {area:.3f} mm²")

    for calidad in calidades:
        print(calidad)
        print(f"Fnv: {Fnv(calidad)} MPa")
        v = φR_n(0.75, Fnv(calidad), area) / 1000
        print(f"cortante simple: {v:.3f} MPa")
        print(f"cortante doble: {2*v:.3f} MPa")

    # fnv = perno_7_8['Fnv'] = Fnv()
    # print('perno 7/8"')
