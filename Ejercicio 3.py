nota = input("digite la nota de 1 a 5")
nota = float(nota)

if nota >=5.0:
    print("su nota es excelente")
    print("tienes 20% de descuento")
elif nota >=4.0:
    print("su nota es sobresaliente")

elif nota >=3.1:
    print("su nota es bueno")

elif nota >=1.0:
    print("su nota es insuficiente")

else:
    print("su nota es invalida")