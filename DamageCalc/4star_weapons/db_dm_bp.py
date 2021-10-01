import matplotlib.pyplot as plt
from ..mainfolder.main import dbHuTao, dmHuTao1, dmHuTao2, bpHuTao

time = [i for i in range(0,1810)]

a = dbHuTao()
db_dmg = []
current_damage = 0

for i in time:
	if a.energy < 60:
		a.energy += 1

	if i%16 == 0:
		a.parmita()

	if a.skill:
		if a.skill_time > 0:
			a.skill_time -= 1
		else:
			a.parmita_revert()

	if (a.energy >= 60) and (a.time_since_burst >= 15):
		current_damage += a.damage('burst')
		a.time_since_burst = 0
		a.energy = 0

	current_damage += a.damage('normal1')
	if a.stamina < 25:
		current_damage += a.damage('normal2')
		if len(db_dmg)%2 == 0:
			current_damage += a.damage('normal3')*(1.5*(1 + (2.78*a.em/(1400 +a.em))))
		else:
			current_damage += a.damage('normal3')
		current_damage += a.damage('normal4')
		current_damage += a.damage('normal5')
		current_damage += a.damage('normal6')
	elif 25 < a.stamina < 50:
		current_damage += a.damage('normal2')
		current_damage += a.damage('normal3')
		current_damage += a.damage('normal4')
		if len(db_dmg)%2 == 0:
			current_damage += a.damage('charged')*(1.5*(1 + (2.78*a.em/(1400 + a.em))))
		else:
			current_damage += a.damage('charged')
		a.stamina -= 25
	elif a.stamina > 50:
		current_damage += a.damage('charged')
		if len(db_dmg)%2 == 0:
			current_damage += a.damage('charged')*(1.5*(1 + (2.78*a.em/(1400 + a.em))))
		else:
			current_damage += a.damage('charged')
		a.stamina -= 50
		current_damage += a.damage('normal1')

	a.time_since_burst += 1
	a.stamina += 25
	db_dmg.append(current_damage)

a = dmHuTao1()
dm1_dmg = []
current_damage = 0

for i in time:
	if a.energy < 60:
		a.energy += 1

	if i%16 == 0:
		a.parmita()

	if a.skill:
		if a.skill_time > 0:
			a.skill_time -= 1
		else:
			a.parmita_revert()

	if (a.energy >= 60) and (a.time_since_burst >= 15):
		current_damage += a.damage('burst')
		a.time_since_burst = 0
		a.energy = 0

	current_damage += a.damage('normal1')
	if a.stamina < 25:
		current_damage += a.damage('normal2')
		if len(dm1_dmg)%2 == 0:
			current_damage += a.damage('normal3')*(1.5*(1 + (2.78*a.em/(1400 +a.em))))
		else:
			current_damage += a.damage('normal3')
		current_damage += a.damage('normal4')
		current_damage += a.damage('normal5')
		current_damage += a.damage('normal6')
	elif 25 < a.stamina < 50:
		current_damage += a.damage('normal2')
		current_damage += a.damage('normal3')
		current_damage += a.damage('normal4')
		if len(dm1_dmg)%2 == 0:
			current_damage += a.damage('charged')*(1.5*(1 + (2.78*a.em/(1400 + a.em))))
		else:
			current_damage += a.damage('charged')
		a.stamina -= 25
	elif a.stamina > 50:
		current_damage += a.damage('charged')
		if len(dm1_dmg)%2 == 0:
			current_damage += a.damage('charged')*(1.5*(1 + (2.78*a.em/(1400 + a.em))))
		else:
			current_damage += a.damage('charged')
		a.stamina -= 50
		current_damage += a.damage('normal1')

	a.time_since_burst += 1
	a.stamina += 25
	dm1_dmg.append(current_damage)

a = dmHuTao2()
dm2_dmg = []
current_damage = 0

for i in time:
	if a.energy < 60:
		a.energy += 1

	if i%16 == 0:
		a.parmita()

	if a.skill:
		if a.skill_time > 0:
			a.skill_time -= 1
		else:
			a.parmita_revert()

	if (a.energy >= 60) and (a.time_since_burst >= 15):
		current_damage += a.damage('burst')
		a.time_since_burst = 0
		a.energy = 0

	current_damage += a.damage('normal1')
	if a.stamina < 25:
		current_damage += a.damage('normal2')
		if len(dm2_dmg)%2 == 0:
			current_damage += a.damage('normal3')*(1.5*(1 + (2.78*a.em/(1400 +a.em))))
		else:
			current_damage += a.damage('normal3')
		current_damage += a.damage('normal4')
		current_damage += a.damage('normal5')
		current_damage += a.damage('normal6')
	elif 25 < a.stamina < 50:
		current_damage += a.damage('normal2')
		current_damage += a.damage('normal3')
		current_damage += a.damage('normal4')
		if len(dm2_dmg)%2 == 0:
			current_damage += a.damage('charged')*(1.5*(1 + (2.78*a.em/(1400 + a.em))))
		else:
			current_damage += a.damage('charged')
		a.stamina -= 25
	elif a.stamina > 50:
		current_damage += a.damage('charged')
		if len(dm2_dmg)%2 == 0:
			current_damage += a.damage('charged')*(1.5*(1 + (2.78*a.em/(1400 + a.em))))
		else:
			current_damage += a.damage('charged')
		a.stamina -= 50
		current_damage += a.damage('normal1')

	a.time_since_burst += 1
	a.stamina += 25
	dm2_dmg.append(current_damage)

a = bpHuTao(1)
bp1_dmg = []
current_damage = 0

for i in time:
	if a.energy < 60:
		a.energy += 1

	if i%16 == 0:
		a.parmita()

	if a.skill:
		if a.skill_time > 0:
			a.skill_time -= 1
		else:
			a.parmita_revert()

	if (a.energy >= 60) and (a.time_since_burst >= 15):
		current_damage += a.damage('burst')
		a.time_since_burst = 0
		a.energy = 0

	current_damage += a.damage('normal1')
	if a.stamina < 25:
		current_damage += a.damage('normal2')
		if len(bp1_dmg)%2 == 0:
			current_damage += a.damage('normal3')*(1.5*(1 + (2.78*a.em/(1400 +a.em))))
		else:
			current_damage += a.damage('normal3')
		current_damage += a.damage('normal4')
		current_damage += a.damage('normal5')
		current_damage += a.damage('normal6')
	elif 25 < a.stamina < 50:
		current_damage += a.damage('normal2')
		current_damage += a.damage('normal3')
		current_damage += a.damage('normal4')
		if len(bp1_dmg)%2 == 0:
			current_damage += a.damage('charged')*(1.5*(1 + (2.78*a.em/(1400 + a.em))))
		else:
			current_damage += a.damage('charged')
		a.stamina -= 25
	elif a.stamina > 50:
		current_damage += a.damage('charged')
		if len(bp1_dmg)%2 == 0:
			current_damage += a.damage('charged')*(1.5*(1 + (2.78*a.em/(1400 + a.em))))
		else:
			current_damage += a.damage('charged')
		a.stamina -= 50
		current_damage += a.damage('normal1')

	a.time_since_burst += 1
	a.stamina += 25
	bp1_dmg.append(current_damage)

a = bpHuTao(2)
bp2_dmg = []
current_damage = 0

for i in time:
	if a.energy < 60:
		a.energy += 1

	if i%16 == 0:
		a.parmita()

	if a.skill:
		if a.skill_time > 0:
			a.skill_time -= 1
		else:
			a.parmita_revert()

	if (a.energy >= 60) and (a.time_since_burst >= 15):
		current_damage += a.damage('burst')
		a.time_since_burst = 0
		a.energy = 0

	current_damage += a.damage('normal1')
	if a.stamina < 25:
		current_damage += a.damage('normal2')
		if len(bp2_dmg)%2 == 0:
			current_damage += a.damage('normal3')*(1.5*(1 + (2.78*a.em/(1400 +a.em))))
		else:
			current_damage += a.damage('normal3')
		current_damage += a.damage('normal4')
		current_damage += a.damage('normal5')
		current_damage += a.damage('normal6')
	elif 25 < a.stamina < 50:
		current_damage += a.damage('normal2')
		current_damage += a.damage('normal3')
		current_damage += a.damage('normal4')
		if len(bp2_dmg)%2 == 0:
			current_damage += a.damage('charged')*(1.5*(1 + (2.78*a.em/(1400 + a.em))))
		else:
			current_damage += a.damage('charged')
		a.stamina -= 25
	elif a.stamina > 50:
		current_damage += a.damage('charged')
		if len(bp2_dmg)%2 == 0:
			current_damage += a.damage('charged')*(1.5*(1 + (2.78*a.em/(1400 + a.em))))
		else:
			current_damage += a.damage('charged')
		a.stamina -= 50
		current_damage += a.damage('normal1')

	a.time_since_burst += 1
	a.stamina += 25
	bp2_dmg.append(current_damage)

a = bpHuTao(3)
bp3_dmg = []
current_damage = 0

for i in time:
	if a.energy < 60:
		a.energy += 1

	if i%16 == 0:
		a.parmita()

	if a.skill:
		if a.skill_time > 0:
			a.skill_time -= 1
		else:
			a.parmita_revert()

	if (a.energy >= 60) and (a.time_since_burst >= 15):
		current_damage += a.damage('burst')
		a.time_since_burst = 0
		a.energy = 0

	current_damage += a.damage('normal1')
	if a.stamina < 25:
		current_damage += a.damage('normal2')
		if len(bp3_dmg)%2 == 0:
			current_damage += a.damage('normal3')*(1.5*(1 + (2.78*a.em/(1400 +a.em))))
		else:
			current_damage += a.damage('normal3')
		current_damage += a.damage('normal4')
		current_damage += a.damage('normal5')
		current_damage += a.damage('normal6')
	elif 25 < a.stamina < 50:
		current_damage += a.damage('normal2')
		current_damage += a.damage('normal3')
		current_damage += a.damage('normal4')
		if len(bp3_dmg)%2 == 0:
			current_damage += a.damage('charged')*(1.5*(1 + (2.78*a.em/(1400 + a.em))))
		else:
			current_damage += a.damage('charged')
		a.stamina -= 25
	elif a.stamina > 50:
		current_damage += a.damage('charged')
		if len(bp3_dmg)%2 == 0:
			current_damage += a.damage('charged')*(1.5*(1 + (2.78*a.em/(1400 + a.em))))
		else:
			current_damage += a.damage('charged')
		a.stamina -= 50
		current_damage += a.damage('normal1')

	a.time_since_burst += 1
	a.stamina += 25
	bp3_dmg.append(current_damage)

plt.plot(time, db_dmg, label="Dragon's Bane")
plt.plot(time, dm1_dmg, label="Deathmatch: 1 enemy")
plt.plot(time, dm2_dmg, label="Deathmatch: 2 enemies")
plt.plot(time, bp1_dmg, label="Blackcliff Pole: 1 stack")
plt.plot(time, bp2_dmg, label="Blackcliff Pole: 2 stacks")
plt.plot(time, bp3_dmg, label="Blackcliff Pole: 3 stacks")
plt.xlabel('Time')
plt.ylabel('Damage')
plt.title('Hu Tao 4 star Weapon Comparision (vaporize) low crit')
plt.legend()
plt.show()
