"""Think Python Ejercicios 1-2 Utilizando Lambda"""
#How many seconds are there in 42 minutes 42 seconds?
SECONDS = (lambda x: (x*60)+42)(42)

print("Segundos en 42min 42 seg:", SECONDS)

#How many miles are there in 10 kilometers? Hint: there are 1.61 kilometers in a mile.
MILES = (lambda x: x/1.61)(10)
print("Millas en 10km:", MILES)

#If you run a 10 kilometer race in 42 minutes 42 seconds, what is your average pace(time per mile in minutes and seconds)? What is your average speed in miles per hour?
PROMEDIO = (lambda x, y: x / y)(MILES, (SECONDS/3600))
print("Velocidad promedio en millas/hora:", PROMEDIO)
