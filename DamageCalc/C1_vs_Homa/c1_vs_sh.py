import matplotlib.pyplot as plt
from ..mainfolder.main import bpHuTao, shHuTao

time = [i for i in range(0,1810)]

a = bpHuTao(3)
bp_dmg = []
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
	current_damage += a.damage('charged')
	if (len(bp_dmg)%2 == 0) and (a.skill):
		current_damage += a.damage('charged')*(1.5*(1 + (2.78*a.em/(1400 + a.em))))
	else:
		current_damage += a.damage('charged')
	current_damage += a.damage('normal1')

	a.time_since_burst += 1
	bp_dmg.append(current_damage)

a = shHuTao()
sh_dmg = []

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
		if (len(bp_dmg)%2 == 0) and (a.skill):
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
		if (len(bp_dmg)%2 == 0) and (a.skill):
			current_damage += a.damage('charged')*(1.5*(1 + (2.78*a.em/(1400 + a.em))))
		else:
			current_damage += a.damage('charged')
		a.stamina -= 25
	elif a.stamina > 50:
		current_damage += a.damage('charged')
		if (len(bp_dmg)%2 == 0) and (a.skill):
			current_damage += a.damage('charged')*(1.5*(1 + (2.78*a.em/(1400 + a.em))))
		else:
			current_damage += a.damage('charged')
		a.stamina -= 50
		current_damage += a.damage('normal1')

	a.time_since_burst += 1
	a.stamina += 25
	sh_dmg.append(current_damage)

plt.plot(time, sh_dmg, label="Staff of Homa C0")
plt.plot(time, bp_dmg, label="Blackcliff Pole C1")
plt.xlabel('Time')
plt.ylabel('Damage')
plt.title('Hu Tao C1 Blackcliff Pole vs C0 Staff of Homa vaporize')
plt.legend()
plt.show()
