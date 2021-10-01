import random

class HuTao():
	def __init__(self):
		self.hp = 30000
		self.normal_attack = 74.06/100
		self.charged_attack = 214.76/100
		self.burst_attack = 558.42/100
		self.atk_character = 106
		self.atk_weapon = 454
		self.attack = 20/100
		self.flat_attack = 1000
		self.dmg_bonus = 76.4/100
		self.energy = 60
		self.skill_time = 9
		self.skill = False
		self.time_since_burst = 15
		self.em = 100
		self.stamina = 310
		self.normal1 = 74.06/100
		self.normal2 = 76.22/100
		self.normal3 = 96.43/100
		self.normal4 = 103.68/100
		self.normal5 = 108.16/100
		self.normal6 = 135.78/100
		self.crit_d = 150/100
		self.crit_r = 35/100

	def parmita(self):
		self.skill = True
		self.flat_attack += 5.66*self.hp/100

	def parmita_revert(self):
		self.flat_attack = 1000
		self.skill = False
		self.skill_time = 9
		self.energy += 40

class cwfHuTao(HuTao):
	def __init__(self):
		super().__init__()
		self.dmg_bonus += 15/100
		self.effect_time = 10
		self.effect = False

	def damage(self, type):
		if type == 'normal':
			talent = self.normal_attack
		if type == 'charged':
			talent = self.charged_attack
		if type == 'burst':
			talent = self.burst_attack

		return talent*(((self.atk_character + self.atk_weapon)*(1 + self.attack)) + self.flat_attack)*(1 + self.dmg_bonus)

	def effect_change(self):
		self.dmg_bonus += 7.5/100
		self.effect = True

	def effect_revert(self):
		self.dmg_bonus -= 7.5/100
		self.effect = False
		self.effect_time = 10

class srHuTao(HuTao):
	def __init__(self):
		super().__init__()
		self.effect_time = 10
		self.effect = False
		self.normal_dmg_bonus = self.dmg_bonus
		self.charged_dmg_bonus = self.dmg_bonus
		self.burst_dmg_bonus = self.dmg_bonus

	def effect_change(self):
		self.energy -= 15
		self.normal_dmg_bonus = self.dmg_bonus
		self.charged_dmg_bonus = self.dmg_bonus
		self.burst_dmg_bonus = self.dmg_bonus
		self.normal_dmg_bonus += 50/100
		self.charged_dmg_bonus += 50/100

	def effect_revert(self):
		self.normal_dmg_bonus -= 50/100
		self.charged_dmg_bonus -= 50/100
		self.effect_time = 10

	def damage(self, type):
		if type == 'normal':
			talent = self.normal_attack
			s_dmg_bonus = self.normal_dmg_bonus
		if type == 'charged':
			talent = self.charged_attack
			s_dmg_bonus = self.charged_dmg_bonus
		if type == 'burst':
			talent = self.burst_attack
			s_dmg_bonus = self.burst_dmg_bonus

		return talent*(((self.atk_character + self.atk_weapon)*(1 + self.attack)) + self.flat_attack)*(1 + s_dmg_bonus)

class cwfdbHuTao(cwfHuTao):
	def __init__(self):
		super().__init__()

	def parmita(self):
		self.skill = True
		self.flat_attack += 5.66*self.hp/100
		self.dmg_bonus += 36/100

	def parmita_revert(self):
		self.flat_attack = 1000
		self.skill = False
		self.skill_time = 9
		self.energy += 40
		self.dmg_bonus -= 36/100

class srdbHuTao(srHuTao):
	def __init__(self):
		super().__init__()

	def parmita(self):
		self.skill = True
		self.flat_attack += 5.66*self.hp/100
		self.dmg_bonus += 36/100

	def parmita_revert(self):
		self.flat_attack = 1000
		self.skill = False
		self.skill_time = 9
		self.energy += 40
		self.dmg_bonus -= 36/100

class cwfdbstamHuTao(cwfdbHuTao):
	def __init__(self):
		super().__init__()

	def damage(self, type):
		if type == 'normal1':
			talent = self.normal1
		if type == 'normal2':
			talent = self.normal2
		if type == 'normal3':
			talent = self.normal3
		if type == 'normal4':
			talent = self.normal4
		if type == 'normal5':
			talent = self.normal5
		if type == 'normal6':
			talent = self.normal6
		if type == 'charged':
			talent = self.charged_attack
		if type == 'burst':
			talent = self.burst_attack

		return talent*(((self.atk_character + self.atk_weapon)*(1 + self.attack)) + self.flat_attack)*(1 + self.dmg_bonus)

class srdbstamHuTao(srdbHuTao):
	def __init__(self):
		super().__init__()

	def damage(self, type):
		if type == 'normal1':
			talent = self.normal1
			s_dmg_bonus = self.normal_dmg_bonus
		if type == 'normal2':
			talent = self.normal2
			s_dmg_bonus = self.normal_dmg_bonus
		if type == 'normal3':
			talent = self.normal3
			s_dmg_bonus = self.normal_dmg_bonus
		if type == 'normal4':
			talent = self.normal4
			s_dmg_bonus = self.normal_dmg_bonus
		if type == 'normal5':
			talent = self.normal5
			s_dmg_bonus = self.normal_dmg_bonus
		if type == 'normal6':
			talent = self.normal6
			s_dmg_bonus = self.normal_dmg_bonus
		if type == 'charged':
			talent = self.charged_attack
			s_dmg_bonus = self.charged_dmg_bonus
		if type == 'burst':
			talent = self.burst_attack
			s_dmg_bonus = self.burst_dmg_bonus

		return talent*(((self.atk_character + self.atk_weapon)*(1 + self.attack)) + self.flat_attack)*(1 + s_dmg_bonus)

class dbHuTao(HuTao):
	def __init__(self):
		super().__init__()
		self.em = 270
		self.atk_weapon = 454

	def parmita(self):
		self.skill = True
		self.flat_attack += 5.66*self.hp/100
		self.dmg_bonus += 20/100

	def parmita_revert(self):
		self.flat_attack = 1000
		self.skill = False
		self.skill_time = 9
		self.energy += 40
		self.dmg_bonus -= 20/100

	def damage(self, type):
		if type == 'normal1':
			talent = self.normal1
		if type == 'normal2':
			talent = self.normal2
		if type == 'normal3':
			talent = self.normal3
		if type == 'normal4':
			talent = self.normal4
		if type == 'normal5':
			talent = self.normal5
		if type == 'normal6':
			talent = self.normal6
		if type == 'charged':
			talent = self.charged_attack
		if type == 'burst':
			talent = self.burst_attack
		if self.crit_r >= random.random():
			return talent*(((self.atk_character + self.atk_weapon)*(1 + self.attack)) + self.flat_attack)*(1 + self.dmg_bonus)*self.crit_d
		else:
			return talent*(((self.atk_character + self.atk_weapon)*(1 + self.attack)) + self.flat_attack)*(1 + self.dmg_bonus)

class dmHuTao1(HuTao):
	def __init__(self):
		super().__init__()
		self.atk_weapon = 454
		self.crit_r += 36.8/100
		self.attack += 24/100

	def damage(self, type):
		if type == 'normal1':
			talent = self.normal1
		if type == 'normal2':
			talent = self.normal2
		if type == 'normal3':
			talent = self.normal3
		if type == 'normal4':
			talent = self.normal4
		if type == 'normal5':
			talent = self.normal5
		if type == 'normal6':
			talent = self.normal6
		if type == 'charged':
			talent = self.charged_attack
		if type == 'burst':
			talent = self.burst_attack
		if self.crit_r >= random.random():
			return talent*(((self.atk_character + self.atk_weapon)*(1 + self.attack)) + self.flat_attack)*(1 + self.dmg_bonus)*self.crit_d
		else:
			return talent*(((self.atk_character + self.atk_weapon)*(1 + self.attack)) + self.flat_attack)*(1 + self.dmg_bonus)

class dmHuTao2(HuTao):
	def __init__(self):
		super().__init__()
		self.atk_weapon = 454
		self.crit_r += 36.8/100
		self.attack += 16/100

	def damage(self, type):
		if type == 'normal1':
			talent = self.normal1
		if type == 'normal2':
			talent = self.normal2
		if type == 'normal3':
			talent = self.normal3
		if type == 'normal4':
			talent = self.normal4
		if type == 'normal5':
			talent = self.normal5
		if type == 'normal6':
			talent = self.normal6
		if type == 'charged':
			talent = self.charged_attack
		if type == 'burst':
			talent = self.burst_attack
		if self.crit_r >= random.random():
			return talent*(((self.atk_character + self.atk_weapon)*(1 + self.attack)) + self.flat_attack)*(1 + self.dmg_bonus)*self.crit_d
		else:
			return talent*(((self.atk_character + self.atk_weapon)*(1 + self.attack)) + self.flat_attack)*(1 + self.dmg_bonus)

class bpHuTao(HuTao):
	def __init__(self, stack):
		super().__init__()
		self.atk_weapon = 510
		self.crit_d += 55.1/100
		self.attack += (12*stack)/100

	def damage(self, type):
		if type == 'normal1':
			talent = self.normal1
		if type == 'normal2':
			talent = self.normal2
		if type == 'normal3':
			talent = self.normal3
		if type == 'normal4':
			talent = self.normal4
		if type == 'normal5':
			talent = self.normal5
		if type == 'normal6':
			talent = self.normal6
		if type == 'charged':
			talent = self.charged_attack
		if type == 'burst':
			talent = self.burst_attack
		if self.crit_r >= random.random():
			return talent*(((self.atk_character + self.atk_weapon)*(1 + self.attack)) + self.flat_attack)*(1 + self.dmg_bonus)*self.crit_d
		else:
			return talent*(((self.atk_character + self.atk_weapon)*(1 + self.attack)) + self.flat_attack)*(1 + self.dmg_bonus)

class shHuTao(HuTao):
	def __init__(self):
		super().__init__()
		self.hp += self.hp*20/100
		self.flat_attack += self.hp*0.8/100
		self.flat_attack += self.hp/100

	def damage(self, type):
		if type == 'normal1':
			talent = self.normal1
		if type == 'normal2':
			talent = self.normal2
		if type == 'normal3':
			talent = self.normal3
		if type == 'normal4':
			talent = self.normal4
		if type == 'normal5':
			talent = self.normal5
		if type == 'normal6':
			talent = self.normal6
		if type == 'charged':
			talent = self.charged_attack
		if type == 'burst':
			talent = self.burst_attack
		if self.crit_r >= random.random():
			return talent*(((self.atk_character + self.atk_weapon)*(1 + self.attack)) + self.flat_attack)*(1 + self.dmg_bonus)*self.crit_d
		else:
			return talent*(((self.atk_character + self.atk_weapon)*(1 + self.attack)) + self.flat_attack)*(1 + self.dmg_bonus)
