#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 01:12:46 2023

@author: ned
"""

from tkinter import *
import time
import matplotlib.pyplot as plt

# calculate time left to live
lifespan = 79 # average lifespan in years
birth_date = input("Enter your birth date (YYYY-MM-DD): ")
birth_timestamp = time.mktime(time.strptime(birth_date, "%Y-%m-%d"))
lifespan_seconds = lifespan * 365.25 * 24 * 60 * 60 # average lifespan in seconds
time_left = int(birth_timestamp + lifespan_seconds - time.time())

# create tkinter window
root = Tk()
root.title("Motivational Clock")

# create clock label
clock_label = Label(root, font=("Arial", 32))
clock_label.pack(pady=20)

# create countdown label
countdown_label = Label(root, font=("Arial", 16))
countdown_label.pack()

# create total hours label
total_hours_label = Label(root, font=("Arial", 16))
total_hours_label.pack()

# create total seconds label
total_seconds_label = Label(root, font=("Arial", 16))
total_seconds_label.pack()

# create percentage label
percentage_label = Label(root, font=("Arial", 16))
percentage_label.pack()

# create canvas for donut chart
chart_canvas = Canvas(root, width=300, height=300)
chart_canvas.pack(pady=20)

# define function to update labels and chart
def update_labels():
    global time_left
    
    # update clock label
    current_time = time.strftime("%H:%M:%S")
    clock_label.config(text=current_time)
    
    # calculate percentage of life completed
    life_elapsed = int((time.time() - birth_timestamp) / lifespan_seconds * 100)
    life_remaining = 100 - life_elapsed
    
    # update percentage label
    percentage_label.config(text=f"{life_elapsed}% of your life has elapsed, {life_remaining}% remaining.")
    
    # update donut chart
    chart_canvas.delete("all")
    chart_canvas.create_text(150, 150, text=f"{life_elapsed}%", font=("Arial", 24), fill="white")
    chart_canvas.create_oval(50, 50, 250, 250, fill="gray", outline="")
    chart_canvas.create_arc(50, 50, 250, 250, start=90, extent=-life_elapsed*3.6, fill="red", outline="")
    
    # update countdown label
    if time_left > 0:
        days_left = int(time_left / (24 * 60 * 60))
        hours_left = int((time_left % (24 * 60 * 60)) / (60 * 60))
        seconds_left = int(time_left % 60)
        countdown_label.config(text=f"You have {days_left} days, {hours_left} hours, and {seconds_left} seconds left to live.")
        
        # update total hours label
        total_hours_left = int(time_left / 3600)
        total_hours_label.config(text=f"Total hours left: {total_hours_left:,d}")
        
        # update total seconds label
        total_seconds_left = int(time_left)
        total_seconds_label.config(text=f"Total seconds left: {total_seconds_left:,d}")
        
    else:
        countdown_label.config(text="Your time is up!")
        total_hours_label.config(text="")
        total_seconds_label.config(text="")
        percentage_label.config(text="")
    
    # update time_left variable
    time_left -= 1
    
    # call function again after 1 second
    root.after(1000, update_labels)
# call function to update labels
update_labels()

# run tkinter window
root.mainloop()
