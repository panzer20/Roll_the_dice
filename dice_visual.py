import matplotlib.pyplot as plt

from dice import Dice

#Creating two D6 dice.
dice_1 = Dice()
dice_2 = Dice(10)

#Making a certain numbers of rolls and listing the results.
results = [dice_1.roll() + dice_2.roll() for _ in range(50_000)]

#Analysis of results.
max_result = dice_1.num_sides + dice_2.num_sides
poss_results = range(2, max_result+1)
frequencies = [results.count(value) for value in poss_results]

#Results visualization.
fig, ax = plt.subplots(figsize=(10,6))
ax.bar(poss_results, frequencies, color='blue', edgecolor='black')

#Defining the plot title and axis labels.
ax.set_title("Wynik rzucania kośćmi D6 i D10 pięćdziesiąt tysięcy razy", fontsize=24)
ax.set_xlabel("Wynik", fontsize=14)
ax.set_ylabel("Częstotliwość występowania wartości", fontsize=14)

#Defining labels size.
ax.tick_params(labelsize=14)

#Set the markers on the X-axis for each value.
ax.set_xticks(poss_results)

fig.savefig('dice_visual.png')
