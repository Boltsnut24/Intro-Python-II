# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
  def __init__(self, name: str, current_room, items: List[str] = []):
    self.name = name
    self.current_room = current_room
    self.items = items
  
  def __str__(self) -> str:
    return "{self.name} is in the {self.current_room.name} \n{self.current_room.description}"

  def show_items():
    pass

  def move_player(self, direction):
    if(direction == 'N'):
      self.current_room = current_room.n_to
    elif(direction == 'S'):
      self.current_room = current_room.s_to
    elif(direction == 'E'):
      self.current_room = current_room.e_to
    elif(direction == 'W'):
      self.current_room = current_room.w_to


