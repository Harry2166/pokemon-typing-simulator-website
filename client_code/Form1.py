from ._anvil_designer import Form1Template
from anvil import *

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.    
    self.init_components(**properties)
    types = ['Bug', 'Dark', 'Dragon',
        'Electric', 'Fairy', 'Fighting',
        'Fire',	'Flying',	'Ghost',
        'Grass', 'Ground',	'Ice',
       'Normal', 'Poison',	'Psychic',
        'Rock', 'Steel', 'Water']
    
    self.type_colors = {
	'Normal': '#A8A77A',
	'Fire': '#EE8130',
	'Water': '#6390F0',
	'Electric': '#F7D02C',
	'Grass': '#7AC74C',
	'Ice': '#96D9D6',
	'Fighting': '#C22E28',
	'Poison': '#A33EA1',
	'Ground': '#E2BF65',
	'Flying': '#A98FF3',
	'Psychic': '#F95587',
	'Bug': '#A6B91A',
	'Rock': '#B6A136',
	'Ghost': '#735797',
	'Dragon': '#6F35FC',
	'Dark': '#705746',
	'Steel': '#B7B7CE',
	'Fairy': '#D685AD' }
    
    self.strength = {
            "Bug" : ['Dark','Grass', 'Psychic'], 
            'Dark' : ['Ghost', 'Psychic'], 
            "Dragon" : ['Dragon'], 
            "Electric" : ['Flying', 'Water'], 
            "Fairy" : ['Dark', 'Dragon', 'Fighting'], 
            "Fighting" : ['Dark', 'Ice', 'Normal', 'Rock', 'Steel'], 
            "Fire" : ['Bug', 'Grass', 'Ice', 'Steel'], 
            "Flying" : ['Bug', 'Fighting', 'Grass'], 
            "Ghost" : ['Ghost', 'Psychic'], 
            "Grass" : ['Ground', 'Rock', 'Water' ], 
            "Ground" : ['Electric', 'Fire', 'Poison', 'Rock', 'Steel'],
            "Ice" : ['Dragon', 'Flying', 'Grass', 'Ground'], 
            "Normal" : [], 
            "Poison" : ['Fairy', 'Grass'], 
            "Psychic" : ['Fighting', 'Poison'], 
            "Rock" : ['Bug', 'Fire', 'Flying', 'Ice'], 
            "Steel" : ['Fairy', 'Ice', 'Rock'], 
            "Water" : ['Fire', 'Ground', 'Rock']} # List of all the strenghts that each pokemon typing has against each other arranged in alphabetical order

    self.weakness = {
                  "Bug" : ['Fire', 'Flying', 'Rock'], 
                  'Dark' : ['Bug','Fairy','Fighting'], 
                  "Dragon" : ['Dragon', 'Fairy', 'Ice'], 
                  "Electric" : ['Ground'], 
                  "Fairy" : ['Poison', 'Steel'], 
                  "Fighting" : ['Fairy', 'Flying', 'Psychic'], 
                  "Fire" : ['Ground', 'Rock', 'Water'], 
                  "Flying" : ['Electric', 'Ice', 'Rock'], 
                  "Ghost" : ['Dark', 'Ghost'], 
                  "Grass" : ['Bug', 'Fire', 'Flying', 'Ice', 'Poison'], 
                  "Ground" : ['Grass', 'Ice', 'Water'],
                  "Ice" : ['Fighting', 'Fire', 'Rock', 'Steel'], 
                  "Normal" : ['Fighting'], 
                  "Poison" : ['Ground', 'Psychic'], 
                  "Psychic" : ['Bug', 'Dark', 'Ghost'], 
                  "Rock" : ['Fighting', 'Grass', 'Ground', 'Steel', 'Water'], 
                  "Steel" : ['Fighting', 'Fire', 'Ground'], 
                  "Water" : ['Electric', 'Grass']} 

    self.resistances = {"Bug" : ['Fighting', 'Grass', 'Ground'], 
            'Dark' : ['Dark', 'Ghost'], 
            "Dragon" : ['Electric', 'Fire', 'Grass', 'Water'], 
            "Electric" : ['Electric', 'Flying', 'Steel'], 
            "Fairy" : ['Bug', 'Dark', 'Fighting'], 
            "Fighting" : ['Bug', 'Dark', 'Rock'], 
            "Fire" : ['Bug', 'Fairy', 'Fire', 'Grass', 'Ice', 'Steel'], 
            "Flying" : ['Bug', 'Fighting', 'Grass'], 
            "Ghost" : ['Bug', 'Poison'], 
            "Grass" : ['Electric', 'Grass', 'Ground', 'Water'], 
            "Ground" : ['Poison', 'Rock'],
            "Ice" : ['Ice'], 
            "Normal" : [], 
            "Poison" : ['Fighting', 'Poison', 'Bug', 'Grass', 'Fairy'], 
            "Psychic" : ['Fighting', 'Psychic'], 
            "Rock" : ['Fire', 'Flying', 'Normal', 'Poison'], 
            "Steel" : ['Bug', 'Fairy', 'Dragon', 'Grass', 'Ice', 'Flying', 'Normal', 'Psychic', 'Rock', 'Steel'], 
            "Water" : ['Fire', 'Ice', 'Steel', 'Water']}

    self.immunities = {"Bug" : [], 
            'Dark' : ['Psychic'], 
            "Dragon" : [], 
            "Electric" : [], 
            "Fairy" : ['Dragon'], 
            "Fighting" : [], 
            "Fire" : [], 
            "Flying" : ['Ground'], 
            "Ghost" : ['Normal', 'Fighting'], 
            "Grass" : [], 
            "Ground" : ['Electric'],
            "Ice" : [], 
            "Normal" : ['Ghost'], 
            "Poison" : [], 
            "Psychic" : [], 
            "Rock" : [], 
            "Steel" : ['Poison'], 
            "Water" : []}
    
    self.btn = {}
    gp = GridPanel()
    
    for idx, typing in enumerate(types):
      clr = self.type_colors[typing]
      if idx < 6:
        row = "A"
      elif 6 <= idx < 12:
        row = "B"
      else:
        row = "C"
      self.btn[typing] = Button(
                                text=typing, 
                                width=100,
                                font="Consolas",
                                bold=True,
                                foreground="white",
                                background=clr
      )
      self.btn[typing].tag.name = typing
      self.btn[typing].set_event_handler('click', self.click)
      gp.add_component(self.btn[typing], row=row, col_xs=3,width_xs=1)
    self.add_component(gp)
    
    self.label_strengths = Label(text="Strengths: ", foreground="black", font="Consolas", align="left",
                                 font_size=25)    
    self.label_weaknesses = Label(text="Weaknesses: ", foreground="black", font="Consolas", align="left",
                                 font_size=25)
    self.label_types = Label(text="Type(s) Selected: ", foreground="black", font="Consolas", align="left",
                                 font_size=25)
    self.lower_card = ColumnPanel(background="#f44336", col_spacing="medium", wrap_on="tablet", role="card", 
                                  visible=True, spacing_above="none", spacing_below="none")
    self.name = Link(text="Made by Harry2166", url="https://github.com/Harry2166", align="center", 
                     font_size=12, italic=True, underline=True,
                     foreground="white", spacing_above = "none", spacing_below="none")
    self.label_resistances = Label(text="Resistances: ", foreground="black", font="Consolas", align="left",
                                 font_size=25)
    self.label_immunities = Label(text="Immunities: ", foreground="black", font="Consolas", align="left",
                                 font_size=25)   
    
    self.add_component((self.label_types))
    self.add_component((self.label_strengths))    
    self.add_component((self.label_weaknesses))
    self.add_component((self.label_resistances))
    self.add_component((self.label_immunities))
    self.add_component(self.lower_card)
    self.lower_card.add_component(self.name, y=10)
    
    
  def click(self, **event_args):
    
    val = event_args['sender'].tag.name
    
    if self.pokemon_type_1.background not in self.type_colors.values():
      self.pokemon_type_1.text += val
      self.pokemon_type_1.foreground = "white"
      self.pokemon_type_1.background = self.type_colors[val]
      self.pokemon_type_1.align = "center"      
      self.pokemon_type_1.font = "Consolas"
      self.pokemon_type_1.enabled = False
    
    elif self.pokemon_type_2.background not in self.type_colors.values():
      self.pokemon_type_2.text += val
      self.pokemon_type_2.foreground = "white"
      self.pokemon_type_2.background = self.type_colors[val]      
      self.pokemon_type_2.align = "center"      
      self.pokemon_type_2.font = "Consolas"
      self.pokemon_type_2.enabled = False

  def simulate_click(self, **event_args):
    """This method is called when the button is clicked"""

    if self.pokemon_type_2.text == self.pokemon_type_1.text:
      alert("Please have two separate typings.")
    else:
      self.label_strengths.remove_from_parent()
      self.label_weaknesses.remove_from_parent()
      self.label_immunities.remove_from_parent()
      self.label_resistances.remove_from_parent()
      self.label_types.remove_from_parent()
      self.lower_card.remove_from_parent()
      
      self.label_strengths.text=self.show_strengths(self.pokemon_type_1.text, self.pokemon_type_2.text)
      self.label_strengths.foreground="black"
      self.label_strengths.font="Consolas"
      self.label_strengths.align="left"
      self.label_strengths.font_size=25
      self.label_strengths.enabled=False
      
      self.label_weaknesses.text=self.show_weaknesses(self.pokemon_type_1.text, self.pokemon_type_2.text)
      self.label_weaknesses.foreground="black"
      self.label_weaknesses.font="Consolas"
      self.label_weaknesses.align="left"
      self.label_weaknesses.font_size=25
      self.label_weaknesses.enabled=False

      self.label_resistances.text=self.show_resistances(self.pokemon_type_1.text, self.pokemon_type_2.text)
      self.label_resistances.foreground="black"
      self.label_resistances.font="Consolas"
      self.label_resistances.align="left"
      self.label_resistances.font_size=25
      self.label_resistances.enabled=False

      self.label_immunities.text=self.show_immunities(self.pokemon_type_1.text, self.pokemon_type_2.text)
      self.label_immunities.foreground="black"
      self.label_immunities.font="Consolas"
      self.label_immunities.align="left"
      self.label_immunities.font_size=25
      self.label_immunities.enabled=False
      
      self.label_types.text=f"Type(s) Selected: {self.pokemon_type_1.text}, {self.pokemon_type_2.text}"
      self.label_types.foreground="black"
      self.label_types.font="Consolas"
      self.label_types.align="left"
      self.label_types.font_size=25
      self.label_types.enabled=False
      
      self.add_component((self.label_types))
      self.add_component((self.label_strengths))
      #self.label_strengths.remove_from_parent()
      self.add_component((self.label_weaknesses))    
      self.add_component((self.label_resistances))
      self.add_component((self.label_immunities))
      #self.label_weaknesses.remove_from_parent()
      self.add_component(self.lower_card)

    self.pokemon_type_1.text = ""
    self.pokemon_type_2.text = ""
    self.pokemon_type_1.foreground = ""
    self.pokemon_type_1.background = ""
    self.pokemon_type_2.foreground = ""
    self.pokemon_type_2.background = ""
    
  def show_strengths(self, first_type, second_type):
      if not second_type:
        monotype = first_type
        monotype_strengths = self.strength.get(monotype)
        return f"Strengths: {', '.join(list(monotype_strengths))}"
      else:
        overall_strength = []
        
        dualtype1 = first_type        
        dualtype2 = second_type
        
        dualtype1_strengths = self.strength.get(dualtype1)
        dualtype2_strengths = self.strength.get(dualtype2)
        
        for typing in dualtype1_strengths: # loop that adds all strengths from the primary type to the overall strengths list
            overall_strength.append(typing)

        for typing in dualtype2_strengths: # loop that adds all strengths from the primary type to the overall strengths list
            overall_strength.append(typing)

        return f"Strengths: {', '.join(list((set(overall_strength))))}"
        
  def show_weaknesses(self, first_type, second_type):
      if not second_type:
        monotype = first_type
        monotype_weaknesses = self.weakness.get(monotype)
        return f"Weaknesses: {', '.join(list(monotype_weaknesses))}"
      else:
        overall_weakness = []
        resistance_immunities = []
        
        dualtype1 = first_type        
        dualtype2 = second_type
        
        dualtype1_weaknesses = self.weakness.get(dualtype1)
        dualtype2_weaknesses = self.weakness.get(dualtype2)
        
        for typing in dualtype1_weaknesses: # loop that adds all weaknesses from the primary type to the overall weaknesses list
            overall_weakness.append(typing) 

        for typing in dualtype2_weaknesses: # loop that adds all weaknesses from the primary type to the overall weaknesses list
            overall_weakness.append(typing)
        
        immunities_dualtype1 = self.immunities.get(dualtype1)
        immunities_dualtype2 = self.immunities.get(dualtype2)
        resistances_dualtype1 = self.resistances.get(dualtype1)
        resistances_dualtype2 = self.resistances.get(dualtype2)
        
        for typing in overall_weakness: # this for loop goes through all typings in the overall_weakness list and checks out the resistances and immunities that each
            if typing in immunities_dualtype1 or typing in immunities_dualtype2: # types has. If it is present in the resistances or immunities, then it
                resistance_immunities.append(typing) # would be added to the resistances and immunities list
            elif typing in resistances_dualtype1 or typing in resistances_dualtype2:
                resistance_immunities.append(typing)

        return f"Weaknesses: {', '.join(list((set(overall_weakness)) - set(resistance_immunities)))}"
  def show_immunities(self, first_type, second_type):
      if not second_type:
        monotype = first_type
        monotype_immunities = self.immunities.get(monotype)
        return f"Immunities: {', '.join(list(monotype_immunities))}"
      else:
        overall_immunities = []
        
        dualtype1 = first_type        
        dualtype2 = second_type
        
        dualtype1_immunities = self.immunities.get(dualtype1)
        dualtype2_immunities = self.immunities.get(dualtype2)
        
        for typing in dualtype1_immunities: # loop that adds all immunities from the primary type to the overall immunities list
            overall_immunities.append(typing)

        for typing in dualtype2_immunities: # loop that adds all immunities from the primary type to the overall immunities list
            overall_immunities.append(typing)

        return f"Immunities: {', '.join(list((set(overall_immunities))))}"

  def show_resistances(self, first_type, second_type):
      if not second_type:
        monotype = first_type
        monotype_resistances = self.resistances.get(monotype)
        return f"Resistances: {', '.join(list(monotype_resistances))}"
      else:
        overall_resistance = []
        
        dualtype1 = first_type        
        dualtype2 = second_type
        
        dualtype1_resistances = self.resistances.get(dualtype1)
        dualtype2_resistances = self.resistances.get(dualtype2)

        dualtype1_weaknesses = self.weakness.get(dualtype1)
        dualtype2_weaknesses = self.weakness.get(dualtype2)
        
        for typing in dualtype1_resistances: # loop that adds all resistances from the primary type to the overall resistances list
            if typing not in dualtype1_weaknesses: overall_resistance.append(typing)

        for typing in dualtype2_resistances: # loop that adds all resistances from the primary type to the overall resistances list
            if typing not in dualtype2_weaknesses: overall_resistance.append(typing)

        return f"Resistances: {', '.join(list((set(overall_resistance))))}"




