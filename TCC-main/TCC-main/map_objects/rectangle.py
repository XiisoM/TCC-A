class Rect:
    def __init__(self, x, y, w, h):
        self.x1 = x
        self.y1 = y
        self.x2 = x + w
        self.y2 = y + h
        
    def center(self):
       center_x = int((self.x1 + self.x2) / 2)
       center_y = int((self.y1 + self.y2) / 2)
       return (center_x, center_y)
   
    def center(self):
       center_x = int((self.x1 + self.x2) / 2)
       center_y = int((self.y1 + self.y2) / 2)
       return (center_x, center_y)