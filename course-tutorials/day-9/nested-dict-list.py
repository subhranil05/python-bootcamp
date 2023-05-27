capitals = {
  "India": "New Delhi",
  "Sri Lanka": "Colombo"
}

# Nesting list inside a dictionary

travel_log = {
  "India": ["Kolakata", "Kerala", "Noida", "Indore"],
  "Europe": ["England", "Spain", "Italy"]
}

# Nesting dictionary inside a dictionary

nested_dict = {
  "India": {"cities_visted": ["Kolakata", "Kerala", "Noida", "Indore"], "total_visit": 10},
  "Europe":{"cities_visted": ["England", "Spain", "Italy"], "total_visit": 5}
}


# Nesting dictionary inside a dictionary

nested_list = [
  {
   "country": "India", 
   "cities_visted": ["Kolakata", "Kerala", "Noida", "Indore"], 
   "total_visit": 10
  },
  {
   "country": "England", 
   "cities_visted": ["Manchester", "Liverpool", "London"], 
   "total_visit": 5
  }
]