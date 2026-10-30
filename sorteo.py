"""Asigna las 24 tareas a línea base / ciclo 1 / ciclo 2 / repuesto, estratificando por tamaño.

Uso: python sorteo.py <semilla>   (registrar la semilla en un acta: el sorteo es reproducible)
"""
import random
import sys

TAMANO = {"t01": "S", "t02": "S", "t03": "M", "t04": "S", "t05": "S", "t06": "M", "t07": "M", "t08": "M",
          "t09": "S", "t10": "M", "t11": "M", "t12": "L", "t13": "M", "t14": "S", "t15": "S", "t16": "M",
          "t17": "S", "t18": "M", "t19": "M", "t20": "S", "t21": "M", "t22": "L", "t23": "S", "t24": "S"}
DIFICIL = {"t03", "t07", "t08", "t12", "t13", "t18", "t19", "t20", "t21", "t22"}
# Tareas que alguno ya implementó en CAMEIA: van con agente y las hace la otra persona.
AUTOR = {"t10": "Juan José", "t11": "Juan José", "t12": "Juan José", "t23": "Juan José", "t15": "Ana Sofía"}
OTRA = {"Juan José": "Ana Sofía", "Ana Sofía": "Juan José"}
# Cupos fijos por tamaño (incluyen las tareas forzadas): así la línea base (10) y la condición con
# agente (12) reciben casi la misma mezcla. Línea base: 1 L, 4 M, 5 S · Agente: 1 L, 6 M, 5 S.
# (v1 repartía en ronda y, al llenarse primero los ciclos, la línea base se quedaba con casi todas las S.)
CUPOS = {"L": {"Línea base": 1, "Agente": 1, "Repuesto": 0},
         "M": {"Línea base": 4, "Agente": 6, "Repuesto": 1},
         "S": {"Línea base": 5, "Agente": 5, "Repuesto": 1}}

sys.stdout.reconfigure(encoding="utf-8")
semilla = int(sys.argv[1]) if len(sys.argv) > 1 else sys.exit("Falta la semilla: python sorteo.py 30102026")
rng = random.Random(semilla)

asignacion = {}
agente = {tam: [t for t in sorted(AUTOR) if TAMANO[t] == tam] for tam in ("L", "M", "S")}
for tam in ("L", "M", "S"):
    # Dentro de cada tamaño: primero las difíciles y luego las demás (cada grupo barajado), repartidas
    # alternando línea base / agente, para que las difíciles también queden parejas entre condiciones.
    dificiles = sorted(t for t in TAMANO if TAMANO[t] == tam and t not in AUTOR and t in DIFICIL)
    faciles = sorted(t for t in TAMANO if TAMANO[t] == tam and t not in AUTOR and t not in DIFICIL)
    rng.shuffle(dificiles)
    rng.shuffle(faciles)
    cupo = {"Línea base": CUPOS[tam]["Línea base"], "Agente": CUPOS[tam]["Agente"] - len(agente[tam]),
            "Repuesto": CUPOS[tam]["Repuesto"]}
    turno = rng.choice(["Línea base", "Agente"])
    for t in dificiles + faciles:
        if cupo[turno] == 0:
            turno = "Agente" if turno == "Línea base" else "Línea base"
        c = turno if cupo[turno] > 0 else "Repuesto"
        cupo[c] -= 1
        if c == "Agente":
            agente[tam].append(t)
        else:
            asignacion[t] = (c, "Pareja humana" if c == "Línea base" else "—")
        turno = "Agente" if turno == "Línea base" else "Línea base"

# Las tareas con agente se reparten entre los dos ciclos alternando dentro de cada tamaño (6 y 6).
i = 0
for tam in ("L", "M", "S"):
    grupo = agente[tam]
    rng.shuffle(grupo)
    for t in grupo:
        asignacion[t] = ("Ciclo 1" if i % 2 == 0 else "Ciclo 2", OTRA[AUTOR[t]] if t in AUTOR else None)
        i += 1

# Quién conduce las tareas con agente que no están forzadas: a quien lleve menos, para quedar 6 y 6.
carga = {p: sum(1 for c, q in asignacion.values() if q == p) for p in OTRA}
libres_agente = sorted(t for t in asignacion if asignacion[t][1] is None)
rng.shuffle(libres_agente)
for t in libres_agente:
    persona = min(sorted(carga), key=lambda p: (carga[p], rng.random()))
    asignacion[t] = (asignacion[t][0], persona)
    carga[persona] += 1

print(f"Semilla: {semilla}\n")
for c in ("Línea base", "Ciclo 1", "Ciclo 2", "Repuesto"):
    ts = sorted(t for t in asignacion if asignacion[t][0] == c)
    mezcla = " · ".join(f"{sum(TAMANO[t] == tam for t in ts)} {tam}" for tam in ("S", "M", "L"))
    print(f"{c} ({len(ts)}: {mezcla} · {sum(t in DIFICIL for t in ts)} difíciles):")
    for t in ts:
        print(f"  {t} [{TAMANO[t]}]{' ⚠️' if t in DIFICIL else ''}  quién: {asignacion[t][1]}")
    if c != "Repuesto":
        # El orden también se sortea: así el aprendizaje entre tareas no favorece siempre a las mismas.
        orden = ts[:]
        rng.shuffle(orden)
        print(f"  Orden para hacerlas: {' → '.join(orden)}")
