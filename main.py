from trigonometry.triangle import Triangle

# Cria uma instâncias da classe Triangle
t1 = Triangle()
t2 = Triangle(3, 4, 5)
t3 = Triangle(3, 4, 5, 6)

# Mostra o perímetro de t1
print(f"Perímetro do t1: {t1.perimeter()}")
# Mostra a área de t2
print(f"Área do t2: {t2.area()}")
# Mostra o tipo de t3
print(f"Tipo do t3: {t3.get_triangle_type()}")

# Cria uma cópia de t3
t_copy = Triangle(t3)
print(f"Cópia de t3: {t_copy}")

