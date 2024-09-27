measure = float(input('Digite uma distância em metros: '))

# Conversões
km = measure / 1000
hm = measure / 100
dam = measure / 10
dm = measure * 10
cm = measure * 100
mm = measure * 1000

print(f'A média de {measure}m corresponde a {cm}cm e {mm}mm')
print(f'Hectômetros: {hm} hm')
print(f'Decâmetros: {dam} dam')
print(f'Decímetros: {dm} dm')
print(f'Centímetros: {cm} cm')
print(f'Milímetros: {mm} mm')