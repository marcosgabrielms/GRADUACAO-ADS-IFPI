# -*- coding: utf-8 -*-

def ler_entrada():
    try:
        return tuple(map(int, input().split()))
    except (ValueError, EOFError):
        return (0, 0, 0)

soma_m_total = 0.0
contador_casos = 0

w1, w2, r = ler_entrada()

while w1 != 0 or w2 != 0 or r != 0:
    m = ((w1 + w2) / 2.0) * (1 + (r / 30.0))
    
    soma_m_total += m
    contador_casos += 1

    if m > 60:
        print("AQUI E BODYBUILDER!!")
    elif m >= 40:
        print("Ta saindo da jaula o monstro!")
    elif m >= 14:
        print("Bora, hora do show! BIIR!")
    elif m >= 13:
        print("E 13")
    else:
        print("Nao vai da nao")

    w1, w2, r = ler_entrada()

if contador_casos > 0:
    media_geral = soma_m_total / contador_casos
    
    if media_geral > 40:
        print()
        print("Aqui nois constroi fibra rapaz! Nao e agua com musculo!")