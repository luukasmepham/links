import selenium

class Tile(object):

    def __init__(self):
        self.selected = 0
        self.tile_selector_first_part = "#layout > div:nth-child("
        self.tile_selector_second_part = ")"

    def create_selector(self, tile):
        self.selector = "css:" + self.tile_selector_first_part + tile + self.tile_selector_second_part

    def get_selector(self):
        return self.selector
    
    def add_to_selection_count(self):
        self.selected = +1

    def remove_from_selection_count(self):
        self.selected = -1

    def get_selection_count(self):
        return self.selected

    def set_tile_color(self, color):
        if color == "white_box":
            self.color = "white"
        if color == "green_box":
            self.color = "green"

    def get_tile_color(self):
        return self.color

class SelectionError(Exception):
    pass