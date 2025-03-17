import matplotlib.pyplot as plt

from dice import Dice

#Utworzenie dwóch kości do gry typu D6.
dice_1 = Dice()
dice_2 = Dice(10)

#Wykonanie pewnej liczby rzutów i umieszczenie wyników na liście.
results = [dice_1.roll() + dice_2.roll() for _ in range(50_000)]

#Analiza wyników.
max_result = dice_1.num_sides + dice_2.num_sides
poss_results = range(2, max_result+1)
frequencies = [results.count(value) for value in poss_results]

#Wizualizacja wyników.
fig, ax = plt.subplots(figsize=(10,6))
ax.bar(poss_results, frequencies, color='blue', edgecolor='black')

#Zdefiniowanie tytułu wykresu i etykiet osi.
ax.set_title("Wynik rzucania kośćmi D6 i D10 pięćdziesiąt tysięcy razy", fontsize=24)
ax.set_xlabel("Wynik", fontsize=14)
ax.set_ylabel("Częstotliwość występowania wartości", fontsize=14)

#Zdefiniowanie wielkości etykiet.
ax.tick_params(labelsize=14)

#Ustawienie znaczników na osi X dla każdej wartości.
ax.set_xticks(poss_results)

fig.savefig('dice_visual.png')