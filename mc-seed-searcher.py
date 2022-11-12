import time
from ctypes import create_unicode_buffer, windll, wintypes
from typing import Optional

import re

import math

#import win32gui

SEARCH_DURATION = 3*60*60
targets = {
        "overworld": [ 
                ["biome", "ancient_city", 1000, 0],  
                ["structure", "pillager_outpost", 800, 0], 
                ], 
        "nether": [ 
                ["structure", "fortress", 300, 0], 
                ["biome", "warped_forrest", 400, 1],
        ],
}
seedReport = [
        "seed", [
            ["name", "x-coord", "y-coord"], 
            ["name", "x_coord", "y-coord"],
        ]
]


#functions to manage the active window
class WindowOps():
    
    #Gets name of current active window.
    #   Not my code. Source: https://stackoverflow.com/a/58355052
    def getForegroundWindowTitle() -> Optional[str]:
        hWnd = windll.user32.GetForegroundWindow()
        length = windll.user32.GetWindowTextLengthW(hWnd)
        buf = create_unicode_buffer(length + 1)
        windll.user32.GetWindowTextW(hWnd, buf, length + 1)
    
        # 1-liner alternative: return buf.value if buf.value else None
        if buf.value:
            return buf.value
        else:
            return None
    
    #moves active window to the argument (the "alt-tab" function)
    def select_window(
            window : str):
        if WindowOps.getForegroundWindowTitle() != window:
            int=0
            
#sheet interface commands
class SheetOps():
    
    def get_targets():
        temp=1
    
    def add_line(
            seedReport : str):
        temp=1

#minecraft interface commands
class MCOps():
    
    def create_new_world():
        int=1
    
    def chat(message: str):
        print(message)
    
    def read_last_chat():
        print("I read you")

#PSEUDO

#goals:
#   prep requirements
#   >start looping
#   create a world
#   construct a new line item for this seed
#   delete world
#   add new line item to SheetOps
#   check loop condition
#   >loop
#   end

#prep requirements
def Load_Parameters():
    WindowOps.select_window("sheet")
    SheetOps.get_targets
()
#   put targets
# into list format for easy reference

# Start looping
def Start_Search(
        targets
    :list):
    
    seedReport.clear()
    
    # Reset the loop condition
    start_time = time.localtime()
    
    # Single-world search loop.
    while (start_time <= time.localtime() + SEARCH_DURATION):
        
        MCOps.create_new_world()
        # Wait until loaded
        
        # Get the world seed.
        MCOps.chat("/seed")
        # Filter out only the seed int from the string.
        seed = int(filter(str.isdigit(MCOps.read_last_chat())))
        # Add seed to the report string.
        seedReport.append(seed)
    
        # Loop through targets
    
        for dimension in targets:
            for item in targets[dimension]:
                MCOps.chat("/locate " + item[0] + " #minecraft:" + item[1])
                
                item_location = MCOps.read_last_chat()
                # Not mine. Source: https://www.delftstack.com/howto/python/extract-substring-from-a-string-in-python/
                try:
                    coordinates = re.search('[(.+?)]', item_location).group(1)
                except AttributeError:
                    pass
                #
                (x_coordinate, y_coordinate, z_coordinate) = (coordinates)
                direct_distance = pow(x_coordinate^2+z_coordinate^2, 0.5)
                
                
                
                
        # Create new line item
        
    
    

    

