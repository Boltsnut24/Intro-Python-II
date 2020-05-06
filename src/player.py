# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
  def __init__(self, name: str, current_room, items: List[str] = []):
    self.name = name
    self.current_room = current_room
    self.items = items
  
  def __str__(self) -> str:
    return "{self.name} is in the {self.current_room.name} \n{self.current_room.description}"