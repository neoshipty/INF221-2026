import json

with open("uefa_champions_league_2011_2020.json", "r", encoding="utf-8") as archivo:
    datos_a = json.load(archivo)
    
with open("premier_league_2011_2020.json", "r", encoding="utf-8") as archivo:
    datos_b = json.load(archivo)
    
#print(datos_a)
#print(datos_b)

A = {registro["campeon"] for registro in datos_a} #CHAMPIONS
B = {registro["campeon"] for registro in datos_b} #PREMIER

U = A | B

print(A) #CHAMPIONS
print(B) #PREMIER
print(U) #TODOS

#1. Concepto de conjunto
print("Registros Champions:", len(datos_a))
print("Equipos diferentes:", len(A))
print("Registros Premier:", len(datos_b))
print("Equipos diferentes:", len(B))

orden_inverso = {registro["campeon"].strip() for registro in datos_a[::-1]}
print("Mismo conjunto:", A == orden_inverso)

#2. Notación y Pertenencia
print('Chelsea' in A)
print('Barcelona' not in B)

#3. Extension y comprension
print("Por extension:", A)

C = {x for x in A if x == "Real Madrid"}
print("Por comprension:", C)

#4. Conjunto vacio y universo
vacio = set()
print(len(vacio))
print(type(set()))
print(type({}))

#5. Conjuntos numericos
N = {0, 1, 2, 3}
Z = {-2, -1, 0, 1, 2}
Q = {0.5, 1.5, -2.5}
R = {2.0, 3.14}
Complejos = {2+3j, 1+2j}

print(N)
print(Z)
print(Q)
print(R)
print(Complejos)

#6. Subconjuntos y subconjuntos propios
C = {x for x in A if x == 'FC Barcelona' or x == 'Bayern Munich' or x == 'Real Madrid'} #Equipos no ingleses
print(C <= A)
print(C < A)
print(A < A)

#7. Igualdad y conjuntos disjuntos
print("A y B iguales:", A == B)
print("A y B disjuntos:", A.isdisjoint(B))
print("Igualdad:", A == A)

C = A - B
print("Disjuntos:", C.isdisjoint(B))

#8. Cardinalidad de conjuntos finitos
print(len(A))
print(len(B))
print(len(A & B))

#9. Creacion y modificacion
C = A.copy()
print("Original:", C)

C.add("Manchester City")
print("Agregado:", C)

C.discard("Manchester City")
print("Descartado:", C)

C.remove("Chelsea")
print("Eliminado:", C)

# discard no da error si no existe.
C.discard("Arsenal")
# remove si da error cuando no existe.

'''#10. Elementos hashables y conjuntos inmutables
D = frozenset(A)
B.add(D)
print(B)'''

#11. Union
print("Union:", A | B)
print("Metodo union:", A.union(B))
print("Son iguales:", (A | B) == A.union(B))

#12. Itersección
print(A & B)
print(A.intersection(B))

#13. Diferencia
print("Solo Champions:", A - B)
print("Solo Premier:", B - A)

#14. Diferencia simétrica
print(A ^ B)
#print(A.symmetric_difference(B))
print((A - B) | (B - A))

#15. Complemento
print("A pertenece a U:", A <= U)
print("Complemento de A:", U - A)

#16. Propiedades de las operaciones
C = {x for x in B if x == 'Manchester United' or x == 'Manchester City'} #Equipos de la ciudad de Manchester
print(C)

#Conmutatividad
assert (A | B) == (B | A)
#Asociatividad
assert ((A | B) | C) == (A | (B | C))
# Idempotencia
assert (A & A) == A
# Distributividad
assert (A & (B | C)) == ((A & B) | (A & C))