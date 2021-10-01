import matplotlib.pyplot as plt
from ..mainfolder.main import cwfdbstamHuTao, srdbstamHuTao

time = [i for i in range(0,181)]

cwf_dmg = []
sr_dmg = []

#cwf
a = cwfdbstamHuTao()
a.dmg_bonus += 15/100
current_damage = 0
for i in time:
	if a.energy < 60:
		a.energy += 1

	if i%16 == 0:
		a.parmita()
		a.effect_change()

	if a.skill:
		if a.skill_time > 0:
			a.skill_time -= 1
		else:
			a.parmita_revert()

	if a.effect:
		if a.effect_time > 0:
			a.effect_time -= 1
		else:
			a.effect_revert()

	if (a.energy >= 60) and (a.time_since_burst >= 15):
		current_damage += a.damage('burst')
		a.time_since_burst = 0
		a.energy = 0

	current_damage += a.damage('normal1')
	if a.stamina < 25:
		current_damage += a.damage('normal2')
		current_damage += a.damage('normal3')
		current_damage += a.damage('normal4')
		current_damage += a.damage('normal5')
		current_damage += a.damage('normal6')
	elif 25 < a.stamina < 50:
		current_damage += a.damage('normal2')
		current_damage += a.damage('normal3')
		current_damage += a.damage('normal4')
		current_damage += a.damage('charged')
		a.stamina -= 25
	elif a.stamina > 50:
		current_damage += a.damage('charged')*2
		a.stamina -= 50
		current_damage += a.damage('normal1')

	a.time_since_burst += 1
	a.stamina += 25
	cwf_dmg.append(current_damage)

#sr
b = srdbstamHuTao()
b.attack += 20/100
current_damage = 0
for i in time:
	if (b.energy >= 60) and (b.time_since_burst >= 15):
		current_damage += b.damage('burst')
		b.energy = 0
		b.time_since_burst = 0

	if b.energy < 60:
		b.energy += 1

	if (i%16 == 0):
		b.parmita()
		if b.energy >= 15:
			b.effect_change()

	if b.skill:
		if b.skill_time > 0:
			b.skill_time -= 1
		else:
			b.parmita_revert()

	if b.effect:
		if b.effect_time > 0:
			b.effect_time -= 1
		else:
			b.effect_revert()

	current_damage += b.damage('normal1')
	if b.stamina < 25:
		current_damage += b.damage('normal2')
		current_damage += b.damage('normal3')
		current_damage += b.damage('normal4')
		current_damage += b.damage('normal5')
		current_damage += b.damage('normal6')
	elif 25 < b.stamina < 50:
		current_damage += b.damage('normal2')
		current_damage += b.damage('normal3')
		current_damage += b.damage('normal4')
		current_damage += b.damage('charged')
		b.stamina -= 25
	elif b.stamina > 50:
		current_damage += b.damage('charged')*2
		b.stamina -= 50
		current_damage += b.damage('normal1')

	b.time_since_burst += 1
	a.stamina += 25
	sr_dmg.append(current_damage)

plt.plot(time, cwf_dmg, label="Crimson Witch of Flames build")
plt.plot(time, sr_dmg, label="Shimenawa Reminiscence build")
plt.xlabel('Time')
plt.ylabel('Damage')
plt.title('Hu Tao C0 SR vs CWF no vaporize')
plt.legend()
plt.show()

cwf_vape_dmg = []
sr_vape_dmg = []

#cwf vape

c = cwfdbstamHuTao()
c.dmg_bonus += 15/100
current_damage = 0
for i in time:
	if c.energy < 60:
		c.energy += 1

	if i%16 == 0:
		c.parmita()
		c.effect_change()

	if c.skill:
		if c.skill_time > 0:
			c.skill_time -= 1
		else:
			c.parmita_revert()

	if c.effect:
		if c.effect_time > 0:
			c.effect_time -= 1
		else:
			c.effect_revert()

	if (c.energy >= 60) and (c.time_since_burst >= 15):
		current_damage += c.damage('burst')
		c.time_since_burst = 0
		c.energy = 0

	current_damage += c.damage('normal1')
	if c.stamina < 25:
		current_damage += c.damage('normal2')
		if len(cwf_vape_dmg)%2 == 0:
			current_damage += c.damage('normal3')*(1.5*(1 + (2.78*c.em/(1400 + c.em) + 15/100)))
		else:
			current_damage += c.damage('normal3')
		current_damage += c.damage('normal4')
		current_damage += c.damage('normal5')
		current_damage += c.damage('normal6')
	elif 25 < c.stamina < 50:
		current_damage += c.damage('normal2')
		current_damage += c.damage('normal3')
		current_damage += c.damage('normal4')
		if len(cwf_vape_dmg)%2 == 0:
			current_damage += c.damage('charged')*(1.5*(1 + (2.78*c.em/(1400 + c.em) + 15/100)))
		else:
			current_damage += c.damage('charged')
		c.stamina -= 25
	elif c.stamina > 50:
		current_damage += c.damage('charged')
		if len(cwf_vape_dmg)%2 == 0:
			current_damage += c.damage('charged')*(1.5*(1 + (2.78*c.em/(1400 + c.em) + 15/100)))
		else:
			current_damage += c.damage('charged')
		c.stamina -= 50
		current_damage += c.damage('normal1')

	c.time_since_burst += 1
	c.stamina += 25
	cwf_vape_dmg.append(current_damage)

#sr vape

d = srdbstamHuTao()
d.attack += 20/100
current_damage = 0
for i in time:
	if (d.energy >= 60) and (d.time_since_burst >= 15):
		current_damage += d.damage('burst')
		d.energy = 0
		d.time_since_burst = 0

	if d.energy < 60:
		d.energy += 1

	if (i%16 == 0):
		d.parmita()
		if d.energy >= 15:
			d.effect_change()

	if d.skill:
		if d.skill_time > 0:
			d.skill_time -= 1
		else:
			d.parmita_revert()

	if d.effect:
		if d.effect_time > 0:
			d.effect_time -= 1
		else:
			d.effect_revert()

	current_damage += d.damage('normal1')
	if d.stamina < 25:
		current_damage += d.damage('normal2')
		if len(sr_vape_dmg)%2 == 0:
			current_damage += d.damage('normal3')*(1.5*(1 + (2.78*d.em/(1400 +d.em))))
		else:
			current_damage += d.damage('normal3')
		current_damage += d.damage('normal4')
		current_damage += d.damage('normal5')
		current_damage += d.damage('normal6')
	elif 25 < d.stamina < 50:
		current_damage += d.damage('normal2')
		current_damage += d.damage('normal3')
		current_damage += d.damage('normal4')
		if len(sr_vape_dmg)%2 == 0:
			current_damage += d.damage('charged')*(1.5*(1 + (2.78*d.em/(1400 + d.em))))
		else:
			current_damage += d.damage('charged')
		d.stamina -= 25
	elif d.stamina > 50:
		current_damage += d.damage('charged')
		if len(sr_vape_dmg)%2 == 0:
			current_damage += d.damage('charged')*(1.5*(1 + (2.78*d.em/(1400 + d.em))))
		else:
			current_damage += d.damage('charged')
		d.stamina -= 50
		current_damage += d.damage('normal1')

	d.time_since_burst += 1
	d.stamina += 25
	sr_vape_dmg.append(current_damage)

plt.plot(time, cwf_vape_dmg, label="Crimson Witch of Flames build")
plt.plot(time, sr_vape_dmg, label="Shimenawa Reminiscence build")
plt.xlabel('Time')
plt.ylabel('Damage')
plt.title('Hu Tao C0 SR vs CWF vaporize/melt build')
plt.legend()
plt.show()
