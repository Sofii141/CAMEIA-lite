"""Asigna las 24 tareas a línea base / ciclo 1 / ciclo 2 / repuesto, estratificando por tamaño.

Uso: python sorteo.py <semilla>   (registrar la semilla en un acta: el sorteo es reproducible)
"""
import random
import sys

TAMANO = {"t01": "S", "t02": "S", "t03": "M", "t04": "S", "t05": "S", "t06": "M", "t07": "M", "t08": "M",
          "t09": "S", "t10": "M", "t11": "M", "t12": "L", "t13": "M", "t14": "S", "t15": "S", "t16": "M",
          "t17": "S", "t18": "M", "t19": "M", "t20": "S", "t21": "M", "t22": "L", "t23": "S", "t24": "S"}
# Tareas que alguno ya implementó en CAMEIA: van con agente y las hace la otra persona.
AUTOR = {"t10": "Juan José", "t11": "Juan José", "t12": "Juan José", "t23": "Juan José", "t15": "Ana Sofía"}
OTRA = {"Juan José": "Ana Sofía", "Ana Sofía": "Juan José"}

sys.stdout.reconfigure(encoding="utf-8")
semilla = int(sys.argv[1]) if len(sys.argv) > 1 else sys.exit("Falta la semilla: python sorteo.py 30102026")
rng = random.Random(semilla)

asignacion = {}
forzadas = sorted(AUTOR)
rng.shuffle(forzadas)
for i, t in enumerate(forzadas):
    asignacion[t] = ("Ciclo 1" if i % 2 == 0 else "Ciclo 2", OTRA[AUTOR[t]])

libres = [t for t in TAMANO if t not in AUTOR]
cupos = {"Línea base": 10, "Ciclo 1": 6 - sum(1 for c, _ in asignacion.values() if c == "Ciclo 1"),
         "Ciclo 2": 6 - sum(1 for c, _ in asignacion.values() if c == "Ciclo 2")}
cupos["Repuesto"] = len(libres) - sum(cupos.values())
# Estratificación: se reparte por tamaño en ronda, para que cada condición reciba una mezcla parecida.
orden = []
for tam in ("L", "M", "S"):
    grupo = [t for t in libres if TAMANO[t] == tam]
    rng.shuffle(grupo)
    orden += grupo
condiciones = [c for c in ("Línea base", "Ciclo 1", "Ciclo 2", "Repuesto")]
i = 0
for t in orden:
    while cupos[condiciones[i % 4]] == 0:
        i += 1
    c = condiciones[i % 4]
    cupos[c] -= 1
    asignacion[t] = (c, "Pareja humana" if c == "Línea base" else ("—" if c == "Repuesto" else "por definir"))
    i += 1

print(f"Semilla: {semilla}\n")
for c in condiciones:
    ts = sorted(t for t in asignacion if asignacion[t][0] == c)
    print(f"{c} ({len(ts)}):")
    for t in ts:
        print(f"  {t} [{TAMANO[t]}]  quién: {asignacion[t][1]}")
