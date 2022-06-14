#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tkinter as tk
from tkinter import ttk
import pandas as pd
import numpy as np
from tkinter.constants import CENTER
from frame_settings import*


# In[2]:


def start():
    global startCheck
    startCheck = 1
    frame_start.destroy()

def show_category(category, gram, category_frame, category_color, category_calorie, category_unit, frame_now):
    global show_x, show_y, startCheck    
    
    if(startCheck == 0):
        return
    elif((category == "") or (gram == "") or (counter == 15) or (clear_count == 5)):
        return
    elif((category_frame == new_frame) and unitSelec.get() == ""):
        return
    else:
        for i in category_calorie.keys():
            if(i == category):
                kcal = str(category_calorie[i])
        if(kcal.isdigit() == False or gram.isdigit() == False):
            digitOnly = tk.Label(category_frame, text = "請輸入數字！", font = ('Arial', 9), bg = category_color)
            if(category_frame == new_frame):
                digitOnly.place(x = 386, y = 17)
            else:
                digitOnly.place(x = 100, y = 125)
        elif(float(gram) > 99999):
            TooBig = tk.Label(category_frame, text = "請重新輸入！", font = ('Arial', 9), bg = category_color)
            if(category_frame == new_frame):
                TooBig.place(x = 386, y = 17)
            else:
                TooBig.place(x = 100, y = 125)
        else:
            correctInsert = tk.Label(category_frame, text = "已登記估算！", font = ('Arial', 9), bg = category_color)
            if(category_frame == new_frame):
                correctInsert.place(x = 386, y = 17)
            else:
                correctInsert.place(x = 100, y = 125) 
            for i in category_calorie.keys():
                if(i == category):
                    category_selec = tk.Label(frame_now, text = category, font = ('Arial', 10), fg = '#FFFFFF', bg = frame_color)
                    category_selec.place(x = show_x, y = show_y)
            
                    calorie_selec = tk.Label(frame_now, text = str(category_calorie[i]) + ' ' + str(category_unit[i]),
                                             font = ('Arial', 10), bg = frame_color, fg = '#FFFFFF')
                    calorie_selec.place(x = show_x + 250, y = show_y)
                    
                    if(str(category_unit[i]) == 'kcal/100g'):
                        unitShow = 'g'
                    else:
                        unitShow = 'ml'    
                    category_gram = tk.Label(frame_now, text = gram + ' ' + unitShow, font = ('Arial', 10), fg = '#FFFFFF', bg = frame_color)
                    category_gram.place(x = show_x + 400, y = show_y)
            
            show_x = 5
            show_y = show_y + 30
            calculate_calorie(category_calorie[category], float(gram))

def calculate_calorie(calorie, gram):
    global cal, calorie_arr, gram_arr, counter
    
    calorie_arr[counter][counter] = calorie
    gram_arr[counter] = gram
    cal_arr = calorie_arr.dot(gram_arr/100)
    cal_list = cal_arr.tolist()
    cal = sum(cal_list)
    
    counter = counter + 1
    
def show_calorie():
    frame_now = frame_NOW()
    cal_text.set("估計約" + " " + str(cal) + " " + "kcal")
    calorie_cal = tk.Label(frame_now, textvariable = cal_text, font = ('Arial', 10), bg = '#EBD6D6')
    calorie_cal.place(x = 231, y = 470, anchor = CENTER)
    
def clear_show():
    global cal, calorie_arr, gram_arr, counter, show_x, show_y, clear_count
    
    cal = 0
    calorie_arr = np.zeros((20, 20))
    gram_arr = np.zeros((20))
    counter = 0
    show_x = 5
    show_y = 5
    
    clear_count = clear_count + 1
    
    if(clear_count == 1):
        frame_show5.destroy()
    elif(clear_count == 2):
        frame_show4.destroy()
    elif(clear_count == 3):
        frame_show3.destroy()
    elif(clear_count == 4):
        frame_show2.destroy()
    elif(clear_count == 5):
        frame_show.destroy()
    else:
        return
    
def frame_NOW():
    global clear_count
    
    if(clear_count == 0):
        frame_now = frame_show5
    elif(clear_count == 1):
        frame_now = frame_show4
    elif(clear_count == 2):
        frame_now = frame_show3
    elif(clear_count == 3):
        frame_now = frame_show2
    elif(clear_count == 4):
        frame_now = frame_show
    else:
        return
    return frame_now


# In[3]:


def show_flour():
    flour = flourSelec.get()
    gram = flourUse.get()
    
    frame_now = frame_NOW()
    show_category(flour, gram, flour_frame, flour_color, flour_calorie, flour_unit, frame_now)
            
def show_sugar():
    sugar = sugarSelec.get()
    gram = sugarUse.get()
    
    frame_now = frame_NOW()
    show_category(sugar, gram, sugar_frame, sugar_color, sugar_calorie, sugar_unit, frame_now)

def show_cheese():
    cheese = cheeseSelec.get()
    gram = cheeseUse.get()
    
    frame_now = frame_NOW()
    show_category(cheese, gram, cheese_frame, cheese_color, cheese_calorie, cheese_unit, frame_now)

def show_powder():
    powder = powderSelec.get()
    gram = powderUse.get()
    
    frame_now = frame_NOW()
    show_category(powder, gram, powder_frame, powder_color, powder_calorie, powder_unit, frame_now)

def show_dairy():
    dairy = dairySelec.get()
    gram = dairyUse.get()
    
    frame_now = frame_NOW()
    show_category(dairy, gram, dairy_frame, dairy_color, dairy_calorie, dairy_unit, frame_now)

def show_choco():
    choco = chocoSelec.get()
    gram = chocoUse.get()
    
    frame_now = frame_NOW()
    show_category(choco, gram, choco_frame, choco_color, choco_calorie, choco_unit, frame_now)

def show_gelling():
    gelling = gellingSelec.get()
    gram = gellingUse.get()
    
    frame_now = frame_NOW()
    show_category(gelling, gram, gelling_frame, gelling_color, gelling_calorie, gelling_unit, frame_now)
    
def show_other():
    other = otherSelec.get()
    gram = otherUse.get()
    
    frame_now = frame_NOW()
    show_category(other, gram, other_frame, other_color, other_calorie, other_unit, frame_now)
    
def show_new():
    global ingredient_list, calorie_list, unit_list
    
    new = ingredientInput.get()
    gram = gramInput.get()
    calorie = calorieInput.get()
    unit = unitSelec.get()
    
    ingredient_list[0] = new
    calorie_list[0] = calorie
    unit_list[0] = unit

    new_calorie[ingredient_list[0]] = calorie
    new_unit[ingredient_list[0]] = unit
    
    frame_now = frame_NOW()
    show_category(new, gram, new_frame, new_color, new_calorie, new_unit, frame_now)


# In[4]:


# 麵粉 (flour)

flour_data = pd.read_csv("csv/flour.csv")
flour_calorie = {}
flour_unit = {}

# create tuple of flour
flour_tuple = ('高筋麵粉 / bread flour', '中筋麵粉 / all-purpose flour', '低筋麵粉 / cake flour', '全麥粉 / whole wheat flour')

for i in range(4):
    flour_calorie[flour_tuple[i]] = flour_data.iloc[i][1]
    flour_unit[flour_tuple[i]] = flour_data.iloc[i][2]

flour_label = tk.Label(flour_frame, text = "麵粉 ( flour )", font = ('Arial', 11), bg = flour_color)
flour_label.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = 'w') 

comboFlour = tk.ttk.Combobox(flour_frame, textvariable = flourSelec, state = 'readonly',
                             values=['高筋麵粉 / bread flour', '中筋麵粉 / all-purpose flour', 
                                     '低筋麵粉 / cake flour', '全麥粉 / whole wheat flour'])
comboFlour.grid(row = 1, column = 0, padx = 10, pady = 5, sticky = 'w')

flour_use_label = tk.Label(flour_frame, text = "請輸入使用量（單位：g / ml）", font = ('Arial', 10), bg = flour_color)
flour_use_label.grid(row = 2, column = 0, padx = 10, pady = 5, sticky = 'w')
flour_use = tk.Entry(flour_frame, width = 12, textvariable = flourUse)
flour_use.grid(row = 3, column = 0, padx = 10, pady = 5, sticky = 'w') 

# flour enter button
flour_btn = tk.Button(flour_frame, text = 'Enter', font = ('Arial', 10), width = 5, height = 5, command = show_flour,
                      bg = flourEnter_color)
flour_btn.grid(row = 1, column = 3, rowspan = 3, padx = 10, pady = 10)


# In[5]:


# 糖/糖漿 (sugars/syrup)

sugar_data = pd.read_csv("csv/sugar.csv") 
sugar_calorie = {}
sugar_unit = {}

# create tuple of sugar
sugar_tuple = ('砂糖 / sugar', '麥芽糖 / maltose', '黑糖 / brown sugar', '黑糖蜜 / molasses', '楓糖 / maple sugar', 
               '海藻糖 / trehalose', '蜂蜜 / honey', '糖粉 / icing sugar','防潮糖粉 / Non-Melting powdered Sugar',
               '葡萄糖漿 / Glucose Syrup', '玉米糖漿 / Corn syrup', '轉化糖漿 / Golden syrup')

for i in range(12):
    sugar_calorie[sugar_tuple[i]] = sugar_data.iloc[i][1]
    sugar_unit[sugar_tuple[i]] = sugar_data.iloc[i][2]

sugar_label = tk.Label(sugar_frame, text = "糖/糖漿 ( sugars/syrup )", font = ('Arial', 11), bg = sugar_color)
sugar_label.grid(row = 2, column = 0, padx = 10, pady = 10, sticky = 'w') 

comboSugar = tk.ttk.Combobox(sugar_frame, textvariable = sugarSelec, state = 'readonly', 
                             values=['砂糖 / sugar', '麥芽糖 / maltose', '黑糖 / brown sugar', '黑糖蜜 / molasses', 
                                     '楓糖 / maple sugar', '海藻糖 / trehalose', '蜂蜜 / honey', '糖粉 / icing sugar',
                                     '防潮糖粉 / Non-Melting powdered Sugar', '葡萄糖漿 / Glucose Syrup', 
                                     '玉米糖漿 / Corn syrup', '轉化糖漿 / Golden syrup'])
comboSugar.grid(row = 3, column = 0, padx = 10, pady = 5, sticky = 'w')

sugar_use_label = tk.Label(sugar_frame, text = "請輸入使用量（單位：g / ml）", font = ('Arial', 10), bg = sugar_color)
sugar_use_label.grid(row = 4, column = 0, padx = 10, pady = 5, sticky = 'w')
sugar_use = tk.Entry(sugar_frame, width = 12, textvariable = sugarUse)
sugar_use.grid(row = 5, column = 0, padx = 10, pady = 5, sticky = 'w') 

# sugar enter button
sugar_btn = tk.Button(sugar_frame, text = 'Enter', font = ('Arial', 10), width = 5, height = 5, command = show_sugar,
                      bg = sugarEnter_color)
sugar_btn.grid(row = 3, column = 3, rowspan = 3, padx = 10, pady = 10)


# In[6]:


# 粉類 (powder)

powder_data = pd.read_csv("csv/powder.csv") 
powder_calorie = {}
powder_unit = {}

# create tuple of powder
powder_tuple = ('玉米粉 / corn starch', '木薯澱粉 / tapioca starch', '馬鈴薯澱粉 / potato starch', '葛粉 / arrowroot flour',
                '糯米粉 / glutinous rice flour', '泡打粉 / baking powder', '小蘇打粉 / baking soda',
                '黑芝麻粉 / black sesame powder', '抹茶粉 / matcha powder', '杏仁粉 / almond flour')

for i in range(10):
    powder_calorie[powder_tuple[i]] = powder_data.iloc[i][1]
    powder_unit[powder_tuple[i]] = powder_data.iloc[i][2]

powder_label = tk.Label(powder_frame, text = "粉類 ( powder )" , font = ('Arial', 11), bg = powder_color)
powder_label.grid(row = 4, column = 0, padx = 10, pady = 10, sticky = 'w') 

comboPowder = tk.ttk.Combobox(powder_frame, textvariable = powderSelec, state = 'readonly',
                             values=['玉米粉 / corn starch', '木薯澱粉 / tapioca starch', '馬鈴薯澱粉 / potato starch', 
                                     '葛粉 / arrowroot flour','糯米粉 / glutinous rice flour', '泡打粉 / baking powder',
                                     '小蘇打粉 / baking soda', '黑芝麻粉 / black sesame powder', '抹茶粉 / matcha powder',
                                     '杏仁粉 / almond flour'])
comboPowder.grid(row = 5, column = 0, padx = 10, pady = 5, sticky = 'w')

powder_use_label = tk.Label(powder_frame, text = "請輸入使用量（單位：g / ml）", font = ('Arial', 10), bg = powder_color)
powder_use_label.grid(row = 6, column = 0, padx = 10, pady = 5, sticky = 'w')
powder_use = tk.Entry(powder_frame, width = 12, textvariable = powderUse)
powder_use.grid(row = 7, column = 0, padx = 10, pady = 5, sticky = 'w') 

# powder enter button
powder_btn = tk.Button(powder_frame, text = 'Enter', font = ('Arial', 10), width = 5, height = 5, command = show_powder,
                       bg = powderEnter_color)
powder_btn.grid(row = 5, column = 3, rowspan = 3, padx = 10, pady = 10)


# In[7]:


# 巧克力 (chocolate)

choco_data = pd.read_csv("csv/chocolate.csv") 
choco_calorie = {}
choco_unit = {}

# create tuple of chocolate
choco_tuple = ('巧克力 / chocolate', '苦甜巧克力 / bittersweet chocolate', '白巧克力 / white chocolate',
               '可可粉 / cocoa powder', '耐高溫烘烤巧克力豆 / chocolate chips')

for i in range(5):
    choco_calorie[choco_tuple [i]] = choco_data.iloc[i][1]
    choco_unit[choco_tuple [i]] = choco_data.iloc[i][2]

choco_label = tk.Label(choco_frame, text = "巧克力 ( chocolate )", font = ('Arial', 11), bg = choco_color)
choco_label.grid(row = 2, column = 0, padx = 10, pady = 10, sticky = 'w') 

comboChoco = tk.ttk.Combobox(choco_frame, textvariable = chocoSelec, state = 'readonly',
                             values=['巧克力 / chocolate', '苦甜巧克力 / bittersweet chocolate', '白巧克力 / white chocolate',
                                     '可可粉 / cocoa powder', '耐高溫烘烤巧克力豆 / chocolate chips'])
comboChoco.grid(row = 3, column = 0, padx = 10, pady = 5, sticky = 'w')

choco_use_label = tk.Label(choco_frame, text = "請輸入使用量（單位：g / ml）", font = ('Arial', 10), bg = choco_color)
choco_use_label.grid(row = 4, column = 0, padx = 10, pady = 5, sticky = 'w')
choco_use = tk.Entry(choco_frame, width = 12, textvariable = chocoUse)
choco_use.grid(row = 5, column = 0, padx = 10, pady = 5, sticky = 'w') 

# sugar enter button
choco_btn = tk.Button(choco_frame, text = 'Enter', font = ('Arial', 10), width = 5, height = 5, command = show_choco,
                      bg = chocoEnter_color)
choco_btn.grid(row = 3, column = 3, rowspan = 3, padx = 10, pady = 10)


# In[8]:


# 乳製品 (dairy product)

dairy_data = pd.read_csv("csv/dairy product.csv") 
dairy_calorie = {}
dairy_unit = {}

# create tuple of dairy product
dairy_tuple = ('動物性鮮奶油 / whipping cream', '酸奶 / sour cream', '優格 / yogurt', '椰奶 / coconut milk', 
               '煉乳 / condensed milk', '奶水 / evaporated milk', '奶油 / butter', '發酵奶油 / cultured butter',
               '澄清奶油 / clarified butter', '植物性奶油（人工奶油） / margarine', '素食奶油 / vegan butter')

for i in range(11):
    dairy_calorie[dairy_tuple[i]] = dairy_data.iloc[i][1]
    dairy_unit[dairy_tuple[i]] = dairy_data.iloc[i][2]

dairy_label = tk.Label(dairy_frame, text = "乳製品 ( dairy product )" , font = ('Arial', 11), bg = dairy_color)
dairy_label.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = 'w')

comboDairy = tk.ttk.Combobox(dairy_frame, textvariable = dairySelec, state = 'readonly',
                             values=['動物性鮮奶油 / whipping cream', '酸奶 / sour cream', '優格 / yogurt', 
                                     '椰奶 / coconut milk', '煉乳 / condensed milk', '奶水 / evaporated milk', 
                                     '奶油 / butter', '發酵奶油 / cultured butter','澄清奶油 / clarified butter',
                                     '植物性奶油（人工奶油） / margarine', '素食奶油 / vegan butter'])
comboDairy.grid(row = 1, column = 0, padx = 10, pady = 5, sticky = 'w')

dairy_use_label = tk.Label(dairy_frame, text = "請輸入使用量（單位：g / ml）", font = ('Arial', 10), bg = dairy_color)
dairy_use_label.grid(row = 2, column = 0, padx = 10, pady = 5, sticky = 'w')
dairy_use = tk.Entry(dairy_frame, width = 12, textvariable = dairyUse)
dairy_use.grid(row = 3, column = 0, padx = 10, pady = 5, sticky = 'w') 

# dairy product enter button
dairy_btn = tk.Button(dairy_frame, text = 'Enter', font = ('Arial', 10), width = 5, height = 5, command = show_dairy,
                      bg = dairyEnter_color)
dairy_btn.grid(row = 1, column = 3, rowspan = 3, padx = 10, pady = 10)


# In[9]:


# 起士 (cheese)

cheese_data = pd.read_csv("csv/cheese.csv") 
cheese_calorie = {}
cheese_unit = {}

cheese_frame = tk.Frame(win, width = 300, height = 300, bg = cheese_color, relief = 'groove', bd = 2)
cheese_frame.grid(row = 3, column = 3, rowspan = 3, columnspan = 3, padx = 5, pady = 5, sticky = 'w')
cheese_frame.propagate(0)

# create tuple of cheese
cheese_tuple = ('奶油乳酪 / cream cheese', '帕瑪森起士 / parmesan', '莫札瑞拉起士 / mozzarella cheese',
                '馬斯卡彭起士 / mascarpone cheese', '切達起士 / cheddar cheese', '瑞可達起士 / ricotta cheese',
                '高熔點乳酪 / processed cheese')

for i in range(7):
    cheese_calorie[cheese_tuple [i]] = cheese_data.iloc[i][1]
    cheese_unit[cheese_tuple [i]] = cheese_data.iloc[i][2]

cheese_label = tk.Label(cheese_frame, text = "起士 ( cheese )" , font = ('Arial', 11), bg = cheese_color)
cheese_label.grid(row = 3, column = 0, padx = 10, pady = 10, sticky = 'w')

comboCheese = tk.ttk.Combobox(cheese_frame, textvariable = cheeseSelec, state = 'readonly',
                             values=['奶油乳酪 / cream cheese', '帕瑪森起士 / parmesan', '莫札瑞拉起士 / mozzarella cheese',
                                     '馬斯卡彭起士 / mascarpone cheese', '切達起士 / cheddar cheese', 
                                     '瑞可達起士 / ricotta cheese', '高熔點乳酪 / processed cheese'])
comboCheese.grid(row = 4, column = 0, padx = 10, pady = 5, sticky = 'w')

cheese_use_label = tk.Label(cheese_frame, text = "請輸入使用量（單位：g / ml）", font = ('Arial', 10), bg = cheese_color)
cheese_use_label.grid(row = 5, column = 0, padx = 10, pady = 5, sticky = 'w')
cheese_use = tk.Entry(cheese_frame, width = 12, textvariable = cheeseUse)
cheese_use.grid(row = 6, column = 0, padx = 10, pady = 5, sticky = 'w') 

# cheese enter button
cheese_btn = tk.Button(cheese_frame, text = 'Enter', font = ('Arial', 10), width = 5, height = 5, command = show_cheese,
                       bg = cheeseEnter_color)
cheese_btn.grid(row = 4, column = 3, rowspan = 3, padx = 10, pady = 10)


# In[10]:


# 膠凝劑 (gelling agent)

gelling_data = pd.read_csv("csv/gelling agent.csv") 
gelling_calorie = {}
gelling_unit = {}

# create tuple of gelling agent
gelling_tuple = ('吉利丁 / gelatin', '吉利T / pectin', '蒟蒻果凍粉 / konnyaku jelly powder', '寒天粉 / kanten powder')

for i in range(4):
    gelling_calorie[gelling_tuple [i]] = gelling_data.iloc[i][1]
    gelling_unit[gelling_tuple [i]] = gelling_data.iloc[i][2]

gelling_label = tk.Label(gelling_frame, text = "膠凝劑 ( gelling agent )" , font = ('Arial', 11), bg = gelling_color)
gelling_label.grid(row = 3, column = 0, padx = 10, pady = 10, sticky = 'w')

comboGelling = tk.ttk.Combobox(gelling_frame, textvariable = gellingSelec, state = 'readonly',
                             values=['吉利丁 / gelatin', '吉利T / pectin', '蒟蒻果凍粉 / konnyaku jelly powder', '寒天粉 / kanten powder'])
comboGelling.grid(row = 4, column = 0, padx = 10, pady = 5, sticky = 'w')

gelling_use_label = tk.Label(gelling_frame, text = "請輸入使用量（單位：g / ml）", font = ('Arial', 10), bg = gelling_color)
gelling_use_label.grid(row = 5, column = 0, columnspan = 3, padx = 10, pady = 5, sticky = 'w')
gelling_use = tk.Entry(gelling_frame, width = 12, textvariable = gellingUse)
gelling_use.grid(row = 6, column = 0, padx = 10, pady = 5, sticky = 'w') 

# gelling agent enter button
gelling_btn = tk.Button(gelling_frame, text = 'Enter', font = ('Arial', 10), width = 5, height = 5, command = show_gelling,
                        bg = gellingEnter_color)
gelling_btn.grid(row = 4, column = 3, rowspan = 3, padx = 10, pady = 10)


# In[11]:


# 其他 (other)

other_data = pd.read_csv("csv/other.csv") 
other_calorie = {}
other_unit = {}

# create tuple of other
other_tuple = ('香草精 / vanilla extract', '蘭姆酒 / rum', '伏特加 / vodka')

for i in range(3):
    other_calorie[other_tuple [i]] = other_data.iloc[i][1]
    other_unit[other_tuple [i]] = other_data.iloc[i][2]

other_label = tk.Label(other_frame, text = "其他 ( other )" , font = ('Arial', 11), bg = other_color)
other_label.grid(row = 4, column = 0, padx = 10, pady = 10, sticky = 'w') 

comboOther = tk.ttk.Combobox(other_frame, textvariable = otherSelec, 
                             values=['香草精 / vanilla extract', '蘭姆酒 / rum', '伏特加 / vodka'])
comboOther.grid(row = 5, column = 0, padx = 10, pady = 5, sticky = 'w')

other_use_label = tk.Label(other_frame, text = "請輸入使用量（單位：g / ml）", font = ('Arial', 10), bg = other_color)
other_use_label.grid(row = 6, column = 0, padx = 10, pady = 5, sticky = 'w')
other_use = tk.Entry(other_frame, width = 12, textvariable = otherUse)
other_use.grid(row = 7, column = 0, padx = 10, pady = 5, sticky = 'w') 

# other enter button
other_btn = tk.Button(other_frame, text = 'Enter', font = ('Arial', 10), width = 5, height = 5, command = show_other,
                      bg = otherEnter_color)
other_btn.grid(row = 5, column = 3, rowspan = 3, padx = 10, pady = 10)


# In[12]:


# 新增的材料與熱量

new_calorie = {}
new_unit = {}

new_label = tk.Label(new_frame, text = "自行輸入 ( Enter yourself )" , font = ('Arial', 11), bg = new_color)
new_label.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = 'w') 

NewIngredient = tk.Label(new_frame, text = " 使用材料", font = ('Arial', 10), bg = new_color)
NewIngredient.grid(row = 1, column = 0, columnspan = 2, padx = 5, pady = 13, sticky = 'w')
input_ingredient = tk.Entry(new_frame, width = 17, textvariable = ingredientInput)
input_ingredient.place(x = 75, y = 68)

new_gram = tk.Label(new_frame, text = "使用量（單位：g / ml）", font = ('Arial', 10), bg = new_color)
new_gram.place(x = 210, y = 68)
input_gram = tk.Entry(new_frame, width = 12, textvariable = gramInput)
input_gram.place(x = 360, y = 68)

NewCalorie = tk.Label(new_frame, text = " 材料熱量", font = ('Arial', 10), bg = new_color)
NewCalorie.grid(row = 2, column = 0, columnspan = 2, padx = 5, pady = 13, sticky = 'w')
input_calorie = tk.Entry(new_frame, width = 17, textvariable = calorieInput)
input_calorie.place(x = 75, y = 116)

new_unitUse = tk.Label(new_frame, text = "請選擇使用單位", font = ('Arial', 10), bg = new_color)
new_unitUse.place(x = 210, y = 116)
comboNewUnit = tk.ttk.Combobox(new_frame, textvariable = unitSelec, values=['kcal/100g', 'kcal/100ml'], width = 9)
comboNewUnit.place(x = 360, y = 116)

# new enter button
new_btn = tk.Button(new_frame, text = 'Enter', font = ('Arial', 10), width = 11, height = 2, command = show_new,
                    bg = newEnter_color)
new_btn.grid(row = 0, column = 3, columnspan = 1, padx = 82, pady = 5, sticky = 'e')


# In[13]:


# buttons on start frame
start_btn = tk.Button(frame_start, text = 'S T A R T', font = ('Arial', 13), width = 10, height = 2, command = start,
                      bg = frame_color , fg = '#FFFFFF')
start_btn.place(x = 182, y = 250)

startCalculate_btn = tk.Button(frame_start, text = 'Calculate', font = ('Arial', 10), width = 7, height = 1,
                               bg = frame_color , fg = '#FFFFFF')
startCalculate_btn.place(x = 392, y = 455)

startClear_btn = tk.Button(frame_start, text = 'Clear', font = ('Arial', 10), width = 7, height = 1,
                           bg = frame_color , fg = '#FFFFFF')
startClear_btn.place(x = 8, y = 455)


# In[14]:


# buttons show on the frame_show ~ frame_show5

# 1
calorie_btn = tk.Button(frame_show, text = 'Calculate', font = ('Arial', 10), width = 7, height = 1, command = show_calorie,
                        bg = frame_color , fg = '#FFFFFF')
calorie_btn.place(x = 392, y = 455)

clear_btn = tk.Button(frame_show, text = 'Clear', font = ('Arial', 10), width = 7, height = 1, command = clear_show,
                      bg = frame_color , fg = '#FFFFFF')
clear_btn.place(x = 8, y = 455)

# 2
calorie_btn2 = tk.Button(frame_show2, text = 'Calculate', font = ('Arial', 10), width = 7, height = 1, command = show_calorie,
                         bg = frame_color , fg = '#FFFFFF')
calorie_btn2.place(x = 392, y = 455)

clear_btn2 = tk.Button(frame_show2, text = 'Clear', font = ('Arial', 10), width = 7, height = 1, command = clear_show,
                       bg = frame_color , fg = '#FFFFFF')
clear_btn2.place(x = 8, y = 455)

# 3
calorie_btn3 = tk.Button(frame_show3, text = 'Calculate', font = ('Arial', 10), width = 7, height = 1, command = show_calorie,
                         bg = frame_color , fg = '#FFFFFF')
calorie_btn3.place(x = 392, y = 455)

clear_btn3 = tk.Button(frame_show3, text = 'Clear', font = ('Arial', 10), width = 7, height = 1, command = clear_show,
                       bg = frame_color , fg = '#FFFFFF')
clear_btn3.place(x = 8, y = 455)

# 4
calorie_btn4 = tk.Button(frame_show4, text = 'Calculate', font = ('Arial', 10), width = 7, height = 1, command = show_calorie,
                         bg = frame_color , fg = '#FFFFFF')
calorie_btn4.place(x = 392, y = 455)

clear_btn4 = tk.Button(frame_show4, text = 'Clear', font = ('Arial', 10), width = 7, height = 1, command = clear_show,
                       bg = frame_color , fg = '#FFFFFF')
clear_btn4.place(x = 8, y = 455)

# 5
calorie_btn5 = tk.Button(frame_show5, text = 'Calculate', font = ('Arial', 10), width = 7, height = 1, command = show_calorie,
                         bg = frame_color , fg = '#FFFFFF')
calorie_btn5.place(x = 392, y = 455)

clear_btn5 = tk.Button(frame_show5, text = 'Clear', font = ('Arial', 10), width = 7, height = 1, command = clear_show,
                      bg = frame_color , fg = '#FFFFFF')
clear_btn5.place(x = 8, y = 455)


# In[15]:


win.mainloop()

