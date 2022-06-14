#!/usr/bin/env python
# coding: utf-8

# In[1]:


from settings import*


# In[2]:


# create a frame on win
frame_end = tk.Frame(win, width = 470, height = 495, bg = frame_color, relief = 'groove', bd = 2)
frame_end.grid(row = 3, column = 6, rowspan = 12, padx = 5, pady = 5, sticky = 'w')
frame_end.propagate(0)

frame_EndText = tk.Label(frame_end, text = "Please close the GUI and open again.", font = ('Arial', 15), bg = frame_color, fg = '#FFFFFF')
frame_EndText.place(x = 65, y = 235)

# create frame to show the data
frame_show = tk.Frame(win, width = 470, height = 495, bg = frame_color, relief = 'groove', bd = 2)
frame_show.grid(row = 3, column = 6, rowspan = 12, padx = 5, pady = 5, sticky = 'w')
frame_show.propagate(0)

frame_show2 = tk.Frame(win, width = 470, height = 495, bg = frame_color, relief = 'groove', bd = 2)
frame_show2.grid(row = 3, column = 6, rowspan = 12, padx = 5, pady = 5, sticky = 'w')
frame_show2.propagate(0)

frame_show3 = tk.Frame(win, width = 470, height = 495, bg = frame_color, relief = 'groove', bd = 2)
frame_show3.grid(row = 3, column = 6, rowspan = 12, padx = 5, pady = 5, sticky = 'w')
frame_show3.propagate(0)

frame_show4 = tk.Frame(win, width = 470, height = 495, bg = frame_color, relief = 'groove', bd = 2)
frame_show4.grid(row = 3, column = 6, rowspan = 12, padx = 5, pady = 5, sticky = 'w')
frame_show4.propagate(0)

frame_show5 = tk.Frame(win, width = 470, height = 495, bg = frame_color, relief = 'groove', bd = 2)
frame_show5.grid(row = 3, column = 6, rowspan = 12, padx = 5, pady = 5, sticky = 'w')
frame_show5.propagate(0)

# start frame
frame_start = tk.Frame(win, width = 470, height = 495, bg = frame_color, relief = 'groove', bd = 2)
frame_start.grid(row = 3, column = 6, rowspan = 12, padx = 5, pady = 5, sticky = 'w')
frame_start.propagate(0)

frame_StartText = tk.Label(frame_start, text = "共可估算 5 次，一次至多能計算 15 個輸入項目。", font = ('Arial', 13), bg = frame_color, fg = '#FFFFFF')
frame_StartText.place(x = 40, y = 70)

frame_StartText2 = tk.Label(frame_start, text = "可被計算的使用量最大值為 99999 ，超過即須重新輸入。", font = ('Arial', 12), bg = frame_color, fg = '#FFFFFF')
frame_StartText2.place(x = 30, y = 100)

frame_StartText3 = tk.Label(frame_start, text = "點擊右下角 ' Calculate ' ，計算當下輸入項目合計熱量值。", font = ('Arial', 12), bg = frame_color, fg = '#FFFFFF')
frame_StartText3.place(x = 30, y = 130)

frame_StartText4 = tk.Label(frame_start, text = "點擊左下角 ' Clear ' ，清除已輸入的項目並將熱量值歸零。", font = ('Arial', 12), bg = frame_color, fg = '#FFFFFF')
frame_StartText4.place(x = 30, y = 160)

frame_StartText4 = tk.Label(frame_start, text = "所有材料的熱量值會因品牌不同而不同，請多加留意。", font = ('Arial', 12), bg = frame_color, fg = '#FFFFFF')
frame_StartText4.place(x = 40, y = 190)

frame_startLabel = tk.Label(frame_start, text = '點擊 START 開始使用', font = ('Arial', 9), bg = '#EBD6D6')
frame_startLabel.place(x = 172, y = 310)


# In[3]:


# flour
flour_frame = tk.Frame(win, width = 300, height = 300, bg = flour_color, relief = 'groove', bd = 2)
flour_frame.grid(row = 0, column = 0, rowspan = 3, columnspan = 3, padx = 5, pady = 5, sticky = 'w')
flour_frame.propagate(0)

# sugar
sugar_frame = tk.Frame(win, width = 300, height = 300, bg = sugar_color, relief = 'groove', bd = 2)
sugar_frame.grid(row = 3, column = 0, rowspan = 3, columnspan = 3, padx = 5, pady = 5, sticky = 'w')
sugar_frame.propagate(0)

# powder
powder_frame = tk.Frame(win, width = 300, height = 300, bg = powder_color, relief = 'groove', bd = 2)
powder_frame.grid(row = 6, column = 0, rowspan = 3, columnspan = 3, padx = 5, pady = 5, sticky = 'w')
powder_frame.propagate(0)

# chocolate
choco_frame = tk.Frame(win, width = 300, height = 300, bg = choco_color, relief = 'groove', bd = 2)
choco_frame.grid(row = 9, column = 0, rowspan = 3, columnspan = 3, padx = 5, pady = 5, sticky = 'w')
choco_frame.propagate(0)

# dairy product
dairy_frame = tk.Frame(win, width = 300, height = 300, bg = dairy_color, relief = 'groove', bd = 2)
dairy_frame.grid(row = 0, column = 3, rowspan = 3, columnspan = 3, padx = 5, pady = 5, sticky = 'w')
dairy_frame.propagate(0)

# gelling agent
gelling_frame = tk.Frame(win, width = 300, height = 300, bg = gelling_color, relief = 'groove', bd = 2)
gelling_frame.grid(row = 6, column = 3, rowspan = 3, columnspan = 3, padx = 5, pady = 5, sticky = 'w')
gelling_frame.propagate(0)

# other
other_frame = tk.Frame(win, width = 300, height = 300, bg = other_color, relief = 'groove', bd = 2)
other_frame.grid(row = 9, column = 3, rowspan = 3, columnspan = 3, padx = 5, pady = 5, sticky = 'w')
other_frame.propagate(0)

#new
new_frame = tk.Frame(win, width = 475, height = 300, bg = new_color, relief = 'groove', bd = 2)
new_frame.grid(row = 0, column = 6, rowspan = 3, columnspan = 2, padx = 5, pady = 5, sticky = 'w')
new_frame.propagate(0)

