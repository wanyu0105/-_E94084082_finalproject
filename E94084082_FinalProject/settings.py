#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tkinter as tk
import numpy as np
from color_settings import*


# In[2]:


startCheck = 0
cal = 0
calorie_arr = np.zeros((20, 20))
gram_arr = np.zeros((20))
counter = 0
clear_count = 0

show_x = 5
show_y = 5

ingredient_list = ['i']
calorie_list = ['c']
unit_list = ['u']


# In[ ]:


win = tk.Tk()
win.title('烘焙食品熱量估算器')
win.geometry('1080x680')   # width x height
win.configure(bg = win_color)
win.iconbitmap('sweet.ico')


# In[4]:


cal_text = tk.StringVar()

flourSelec = tk.StringVar()
flourUse = tk.StringVar()

sugarSelec = tk.StringVar()
sugarUse = tk.StringVar()

cheeseSelec = tk.StringVar()
cheeseUse = tk.StringVar()

powderSelec = tk.StringVar()
powderUse = tk.StringVar()

dairySelec = tk.StringVar()
dairyUse = tk.StringVar()

chocoSelec = tk.StringVar()
chocoUse = tk.StringVar()

gellingSelec = tk.StringVar()
gellingUse = tk.StringVar()

otherSelec = tk.StringVar()
otherUse = tk.StringVar()

ingredientInput = tk.StringVar()
calorieInput = tk.StringVar()
gramInput = tk.StringVar()
unitSelec = tk.StringVar()

