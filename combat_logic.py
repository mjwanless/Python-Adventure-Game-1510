import random
import time

import generators
import spells


def level_up(character):
	print("You've leveled up!")
	# time.sleep(1)
	character["Current Level"] += 1
	character["Exp"] = 0
	character["Exp Needed"] += 20
	character["Max HP"] += 15
	character["Current HP"] = character["Max HP"]
	character["Max Mana"] += 25
	character["Current Mana"] = character["Max Mana"]
	spells.balance(character)
	print(f"""
	=====================================================================
	Character Stats: HP: {character['Current HP']}/{character['Max HP']}
					 Mana: {character['Current Mana']}/{character['Max Mana']}
	=====================================================================		
	""")


def combat(character, enemy):
	if enemy == "hen":
		enemy = generators.make_hen()
	elif enemy == "silkie":
		enemy = generators.make_silkie()
	elif enemy == "rooster":
		enemy = generators.make_rooster()
	elif enemy == "sanders":
		enemy = generators.make_sanders()

	peck_cooldown = 0
	feather_throw_cooldown = 0
	plumage_cooldown = 0
	talons_cooldown = 0
	herbs_and_spices_cooldown = 0
	breading_cooldown = 0
	flavour_blast_cooldown = 0

	print(f"Combat is happening between the character and a {enemy['name']}.")

	while character["Current HP"] > 0 and enemy["Current HP"] > 0:
		print(f"""
		==================================
		Character Stats:        HP: {character['Current HP']}/{character['Max HP']}
						        Mana: {character['Current Mana']}/{character['Max Mana']}
		----------------------------------
		{enemy['name']} Stats:              HP {enemy['Current HP']}/{enemy['Max HP']}
		==================================	
		""")

		while True:
			print(f"""
			================================================================================
			Your turn: What would you like to do? Type a number to cast that spell.
			
			1. Holy Blast  |  ({character["Current Level"]} * d6)             | Cost: 0 Mana
			2. Smite       |  ({character["Current Level"]} * d10)            | Cost: 15 Mana
			3. Judgment    |  ({character["Current Level"]} * (0, 4, or 8)))  | Cost: 30 Mana
			4. Heal        |  ({character["Current Level"]} * (3 - 10)))      | Cost: 20 Mana
			================================================================================
			""")

			try:
				user_choice = int(input("Make a choice from the above list: "))

				if 1 <= user_choice <= 4:
					if (
						(user_choice == 1) or
						(user_choice == 2 and character["Current Mana"] >= 15) or
						(user_choice == 3 and character["Current Mana"] >= 30) or
						(user_choice == 4 and character["Current Mana"] >= 20)
					):
						break
					else:
						print("Not enough mana to cast the selected spell. Please choose another.")
				else:
					print("That's not a valid value; Please enter an int between 1 and 4, inclusive.")
			except ValueError:
				print("Invalid input. Please enter a valid integer.")

		# ========================================================================
		# Need to check for if there is enough mana and to cast something else if not
		# ===========================================================================
		if user_choice == 1:
			damage = spells.holy_blast(character)
			enemy["Current HP"] -= damage
			print(f"You've done {damage} damage to {enemy['name']}")
		elif user_choice == 2 and character["Current Mana"] > 15:
			damage = spells.smite(character)
			enemy["Current HP"] -= damage
			print(f"You've done {damage} damage to {enemy['name']}")
		elif user_choice == 3:
			damage = spells.judgment(character)
			enemy["Current HP"] -= damage
			print(f"You've done {damage} damage to {enemy['name']}")
		elif user_choice == 4:
			heal = spells.heal(character)
			character["Current HP"] += heal
			print(f"You've healed {heal} HP.")

		# time.sleep(1)
		if enemy["Current HP"] <= 0:
			print(f"You've defeated the {enemy['name']}! ")
			spells.post_fight_heal(character)
			character["Exp"] += enemy["Exp Value"]
			print(f"You've gained {enemy['Exp Value']} xp. You have {character['Exp']} xp")
			break

		print(f"You've regenerated {7 + character['Current Level'] * 3} mana.")
		spells.regen_mana(character)

		spells.balance(character)

		print("It's now the enemy's turn.")

		# time.sleep(1)

		# ==================================================================================
		# ==================================================================================
		# ==================================================================================
		if enemy["name"] == "hen":
			while True:
				abilities = random.choice(("peck", "scratch"))
				if abilities == "peck" and not peck_cooldown:
					damage = spells.peck()
					character["Current HP"] -= damage
					print(f"{enemy['name']} did {damage} damage to you with peck!")
					peck_cooldown = 2
					break
				if abilities == "scratch":
					damage = spells.peck()
					character["Current HP"] -= damage
					print(f"{enemy['name']} did {damage} damage to you with scratch!")
					break

			if peck_cooldown > 0:
				peck_cooldown -= 1

		# ==================================================================================
		# ==================================================================================
		# ==================================================================================
		if enemy["name"] == "silkie":
			while True:
				abilities = random.choice(("peck", "scratch", "feather", "plumage"))
				if abilities == "peck" and not peck_cooldown:
					damage = spells.peck()
					character["Current HP"] -= damage
					print(f"{enemy['name']} did {damage} damage to you with peck!")
					peck_cooldown = 2
					break
				if abilities == "scratch":
					damage = spells.peck()
					character["Current HP"] -= damage
					print(f"{enemy['name']} did {damage} damage to you with scratch!")
					break
				if abilities == "feather" and not feather_throw_cooldown:
					damage = spells.feather_throw()
					character["Current HP"] -= damage
					print(f"{enemy['name']} did {damage} damage to you with feather throw!")
					feather_throw_cooldown = 3
					break
				if abilities == "plumage" and not plumage_cooldown:
					heal = spells.plumage()
					enemy["Current HP"] += heal
					print(f"{enemy['name']} healed {heal} damage to themselves with plumage!")
					plumage_cooldown = 2
					break

			if peck_cooldown > 0:
				peck_cooldown -= 1
			if feather_throw_cooldown > 0:
				peck_cooldown -= 1
			if plumage_cooldown > 0:
				plumage_cooldown -= 1

		# ==================================================================================
		# ==================================================================================
		# ==================================================================================
		if enemy["name"] == "rooster":
			while True:
				abilities = random.choice(("peck", "scratch", "feather", "plumage", "talons"))
				if abilities == "peck" and not peck_cooldown:
					damage = spells.peck()
					character["Current HP"] -= damage
					print(f"{enemy['name']} did {damage} damage to you with peck!")
					peck_cooldown = 2
					break
				if abilities == "scratch":
					damage = spells.peck()
					character["Current HP"] -= damage
					print(f"{enemy['name']} did {damage} damage to you with scratch!")
					break
				if abilities == "feather" and not feather_throw_cooldown:
					damage = spells.feather_throw()
					character["Current HP"] -= damage
					print(f"{enemy['name']} did {damage} damage to you with feather throw!")
					feather_throw_cooldown = 3
					break
				if abilities == "plumage" and not plumage_cooldown:
					heal = spells.plumage()
					enemy["Current HP"] += heal
					print(f"{enemy['name']} healed {heal} damage to themselves with plumage!")
					plumage_cooldown = 2
					break
				if abilities == "talons" and not talons_cooldown:
					damage = spells.talons()
					character["Current HP"] -= damage
					print(f"{enemy['name']} did {damage} damage to you with talons!")
					plumage_cooldown = 4
					break

			if peck_cooldown > 0:
				peck_cooldown -= 1
			if feather_throw_cooldown > 0:
				peck_cooldown -= 1
			if plumage_cooldown > 0:
				plumage_cooldown -= 1
			if talons_cooldown > 0:
				talons_cooldown -= 1

		# ==================================================================================
		# ==================================================================================
		# ==================================================================================
		if enemy["name"] == "sanders":
			while True:
				abilities = random.choice(("deep", "herbs", "breading", "flavour"))
				if abilities == "deep":
					damage = spells.deep_fry()
					character["Current HP"] -= damage
					print(f"{enemy['name']} did {damage} damage to you with Deep fry!")
					break
				if abilities == "herbs" and not herbs_and_spices_cooldown:
					damage = spells.herbs_and_spices()
					character["Current HP"] -= damage
					print(f"{enemy['name']} did {damage} damage to you 11 herbs and spices!")
					peck_cooldown = 2
					break
				if abilities == "breading" and not breading_cooldown:
					heal = spells.breading()
					enemy["Current HP"] += heal
					print(f"{enemy['name']} healed {heal} damage to themselves with breading!")
					breading_cooldown = 4
					break
				if abilities == "flavour" and not flavour_blast_cooldown:
					damage = spells.flavour_blast()
					character["Current HP"] -= damage
					print(f"{enemy['name']} did {damage} damage to you with flavour blast!")
					plumage_cooldown = 3
					break

			if herbs_and_spices_cooldown > 0:
				herbs_and_spices_cooldown -= 1
			if breading_cooldown > 0:
				breading_cooldown -= 1
			if flavour_blast_cooldown > 0:
				flavour_blast_cooldown -= 1

		if character["Current HP"] <= 0:
			print(f"Sorry; You've died to a {enemy['name']}")

	# time.sleep(1)
