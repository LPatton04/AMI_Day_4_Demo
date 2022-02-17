# Frame1.py
# Thorin Schmidt
# 02/16/22

'''
Frame Example
'''

import tkinter as tk

class Frame1(tk.Frame):
  """ A GUI Frame """

  def __init__(self, master):
    """ Initialize the Frame. """
    
    super(Frame1, self).__init__(master)

    self.master = master
    self.create_widgets()

  def create_widgets(self):
    """ Create a label, and a button that changes the frame. """
    
    # create the label
    msg = "Welcome to Frame 1!"
    self.lblOne = tk.Label(self, text = msg)
    self.lblOne.pack()
    self.btnOne = tk.Button(self, text = "Go to Frame 2", 
                             command = self.master.change_to_2)
    self.btnOne.pack()
