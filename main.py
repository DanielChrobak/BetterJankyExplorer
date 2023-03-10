from datetime import datetime
from threading import Thread
import customtkinter as CTk
from PIL import Image
import json
from time import sleep
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from multiprocessing import Process


black_hnt_logo_img = CTk.CTkImage(dark_image=Image.open(".\\helium_logo_black.png"))
blue_hnt_logo_img = CTk.CTkImage(light_image=Image.open(".\\helium_logo_blue.png"))
iot_logo_img = CTk.CTkImage(light_image=Image.open(".\\iot_logo.png"))
mobile_logo_img = CTk.CTkImage(light_image=Image.open(".\\mobile_logo.png"))

with open("market_data.json", "r") as file:
    market_data = json.loads(file.read())

with open("block_data.json", "r") as file:
    block_data = json.loads(file.read())

with open("validator_data.json", "r") as file:
    validator_data = json.loads(file.read())

with open("hotspot_data.json", "r") as file:
    hotspot_data = json.loads(file.read())

with open("dc_burn_data.json", "r") as file:
    dc_burn_data = json.loads(file.read())

with open("mobile_data.json", "r") as file:
    mobile_data = json.loads(file.read())

explorer = CTk.CTk()

def update_values():
    block_height_value_label.configure(text=f"{format(block_data['height'][len(block_data['height']) - 1]['value'], ',d')}")
    if (int(block_data['height'][len(block_data['height']) - 1]['value']) - int(block_data['height'][0]['value'])) > 0:
        block_height_change_label.configure(text=f"+{format(int(block_data['height'][len(block_data['height']) - 1]['value']) - int(block_data['height'][0]['value']), ',d')}", text_color="green")
    elif (int(block_data['height'][len(block_data['height']) - 1]['value']) - int(block_data['height'][0]['value'])) == 0:
        block_height_change_label.configure(text=f"+{format(int(block_data['height'][len(block_data['height']) - 1]['value']) - int(block_data['height'][0]['value']), ',d')}", color="grey")
    validators_online_value_label.configure(text=f"{format(validator_data['count'][len(validator_data['count']) - 1]['value'], ',d')}")
    if (int(validator_data['count'][len(validator_data['count']) - 1]['value']) - int(validator_data['count'][0]['value'])) > 0:
        validators_online_change_label.configure(text=f"+{format(int(validator_data['count'][len(validator_data['count']) - 1]['value']) - int(validator_data['count'][0]['value']), ',d')}", text_color="green")
    elif (int(validator_data['count'][len(validator_data['count']) - 1]['value']) - int(validator_data['count'][0]['value'])) < 0:
        validators_online_change_label.configure(text=f"{format(int(validator_data['count'][len(validator_data['count']) - 1]['value']) - int(validator_data['count'][0]['value']), ',d')}", text_color="blue")
    elif (int(validator_data['count'][len(validator_data['count']) - 1]['value']) - int(validator_data['count'][0]['value'])) == 0:
        validators_online_change_label.configure(text=f"{format(int(validator_data['count'][len(validator_data['count']) - 1]['value']) - int(validator_data['count'][0]['value']), ',d')}", text_color="grey")
    hnt_price_label.configure(text=f"${market_data['market_data']['current_price']['usd']:.2f}")
    iot_hotspots_value_label.configure(text=f"{format(hotspot_data['count'][len(hotspot_data['count']) - 1]['value'], ',d')}")
    try:
        if dc_burn_data['data']['last_day']['state_channel'] >= 10**9:
            iot_messages_sent_day_value_label.configure(text=f"{dc_burn_data['data']['last_day']['state_channel']/10**9:.3f}B")
        elif dc_burn_data['data']['last_day']['state_channel'] >= 10**6:
            iot_messages_sent_day_value_label.configure(text=f"{dc_burn_data['data']['last_day']['state_channel']/10**6:.3f}M")
        if dc_burn_data['data']['last_month']['state_channel'] >= 10**9:
            iot_messages_sent_month_value_label.configure(text=f"{dc_burn_data['data']['last_month']['state_channel']/10**9:.3f}B")
        elif dc_burn_data['data']['last_month']['state_channel'] >= 10**6:
            iot_messages_sent_month_value_label.configure(text=f"{dc_burn_data['data']['last_month']['state_channel']/10**6:.3f}M")
    except:
        pass    
    if (int(hotspot_data['count'][len(hotspot_data['count']) - 1]['value']) - int(hotspot_data['count'][0]['value'])) > 0:
        iot_hotspots_value_change_label.configure(text=f"+{format(int(hotspot_data['count'][len(hotspot_data['count']) - 1]['value']) - int(hotspot_data['count'][0]['value']), ',d')}", text_color="green")
    elif (int(hotspot_data['count'][len(hotspot_data['count']) - 1]['value']) - int(hotspot_data['count'][0]['value'])) == 0:
        iot_hotspots_value_change_label.configure(text=f"{format(int(hotspot_data['count'][len(hotspot_data['count']) - 1]['value']) - int(hotspot_data['count'][0]['value']), ',d')}", text_color="grey")
    iot_y.clear()
    iot_x.clear()
    for index in range(len(hotspot_data['count'])):
        iot_y.append(hotspot_data['count'][index]['value'])
    for index in range(len(hotspot_data['count'])):
        iot_x.append(index)
    ax.clear()
    ax.set_facecolor("#f9f9fb")
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.plot(iot_x, iot_y)
    iot_graph_label.configure(text=f"{len(hotspot_data['count'])} Day Trend")
    mobile_radio_value_label.configure(text=f"{format(mobile_data['count'][len(mobile_data['count']) - 1]['value'], ',d')}")
    if (int(mobile_data['count'][len(mobile_data['count']) - 1]['value']) - int(mobile_data['count'][0]['value'])) > 0:
        mobile_radio_value_change_label.configure(text=f"+{format(int(mobile_data['count'][len(mobile_data['count']) - 1]['value']) - int(mobile_data['count'][0]['value']), ',d')}", text_color="green")
    elif (int(mobile_data['count'][len(mobile_data['count']) - 1]['value']) - int(mobile_data['count'][0]['value'])) < 0:
        mobile_radio_value_change_label.configure(text=f"{format(int(mobile_data['count'][len(mobile_data['count']) - 1]['value']) - int(mobile_data['count'][0]['value']), ',d')}", text_color="blue")
    elif (int(mobile_data['count'][len(mobile_data['count']) - 1]['value']) - int(mobile_data['count'][0]['value'])) == 0:
        mobile_radio_value_change_label.configure(text=f"{format(int(mobile_data['count'][len(mobile_data['count']) - 1]['value']) - int(mobile_data['count'][0]['value']), ',d')}", text_color="grey")
    mobile_y.clear()
    mobile_x.clear()
    for index in range(len(mobile_data['count']) - 1):
        mobile_y.append(mobile_data['count'][index]['value'])
    for index in range(len(mobile_data['count']) - 1):
        mobile_x.append(index)
    bx.clear()
    bx.set_facecolor("#f9f9fb")
    bx.set_xticks([])
    bx.set_yticks([])
    bx.set_xticklabels([])
    bx.set_yticklabels([])
    bx.spines['top'].set_visible(False)
    bx.spines['right'].set_visible(False)
    bx.spines['bottom'].set_visible(False)
    bx.spines['left'].set_visible(False)
    bx.plot(mobile_x, mobile_y)
    mobile_graph_label.configure(text=f"{len(mobile_data['count'])} Day Trend")

explorer.geometry(f"{explorer.winfo_width()}x{explorer.winfo_height()}")
explorer.title("Janky Explorer")
explorer.minsize(explorer.winfo_screenwidth() * .75, explorer.winfo_screenheight() * .75)
explorer.maxsize(explorer.winfo_screenwidth(), explorer.winfo_screenheight())

back_frame = CTk.CTkFrame(explorer, fg_color="#10182c")
back_frame.pack(fill='both', expand=True)

welcome_frame_top = CTk.CTkFrame(back_frame, fg_color="#10182c")
welcome_frame_top.place(x=0, y=0, relwidth=.2, relheight=1)
home_button = CTk.CTkButton(welcome_frame_top, state="DISABLED", image=black_hnt_logo_img, bg_color="#10182c", fg_color="#10182c", text="", width=0, height=0, command=update_values)
home_button.place(relx=.03, rely=.015)
welcome_label1 = CTk.CTkLabel(welcome_frame_top, text="Welcome to", width=0, height=0)
welcome_label1.place(relx=.07, rely=.136)
welcome_label2 = CTk.CTkLabel(welcome_frame_top, text="Janky Explorer", width=0, height=0)
welcome_label2.place(relx=.07, rely=.16)
welcome_label3 = CTk.CTkLabel(welcome_frame_top, text="Janky Explorer is a recreation of the Helium Explorer\nand is an Analytics App for Helium, a decentralized\nwireless connectivity platform.", justify="left", width=0, height=0)
welcome_label3.place(relx=.07, rely=.19)
welcome_frame_bottom = CTk.CTkFrame(back_frame, fg_color="#fefffe")
welcome_frame_bottom.place(relx=0, rely=.25, relwidth=.2, relheight=.75)

hnt_frame = CTk.CTkFrame(welcome_frame_bottom, fg_color="#f9f9fb")
hnt_frame.place(relx=.07, rely=.038, relwidth=.86, relheight=.18)
hnt_logo = CTk.CTkButton(hnt_frame, width=0, height=0, text="HNT", text_color="black", image=blue_hnt_logo_img, state="DISABLED", fg_color="#f9f9fb", bg_color="#f9f9fb")
hnt_logo.place(relx=.02, rely=.061, anchor="nw")
hnt_price_label = CTk.CTkLabel(hnt_frame, width=0, height=0, text_color="black", text="")
hnt_price_label.place(relx=.95, rely=.1, anchor="ne")
block_height_label = CTk.CTkLabel(hnt_frame, width=0, height=0, text="Block Height", text_color="grey")
block_height_label.place(relx=.07, rely=.33, anchor="nw")
block_height_value_label = CTk.CTkLabel(hnt_frame, width=0, height=0, text_color="black", text="")
block_height_value_label.place(relx=.07, rely=.48)
block_height_change_label = CTk.CTkLabel(hnt_frame, width=0, height=0, text="")
block_height_change_label.place(relx=.07, rely=.7)
hnt_frame_divider_frame = CTk.CTkFrame(hnt_frame, width=1, bg_color="grey")
hnt_frame_divider_frame.place(relx=.45, rely=.38, relheight=.37)
validators_online_label = CTk.CTkLabel(hnt_frame, width=0, height=0, text="Validators Online", text_color="grey")
validators_online_label.place(relx=.6, rely=.33, anchor="nw")
validators_online_value_label = CTk.CTkLabel(hnt_frame, width=0, height=0, text_color="black", text="")
validators_online_value_label.place(relx=.6, rely=.48)
validators_online_change_label = CTk.CTkLabel(hnt_frame, width=0, height=0, text="")
validators_online_change_label.place(relx=.6, rely=.7)

iot_frame = CTk.CTkFrame(welcome_frame_bottom, fg_color="#f9f9fb")
iot_frame.place(relx=.07, rely=.24, relwidth=.86, relheight=.25)
iot_logo = CTk.CTkButton(iot_frame, width=0, height=0, text="IOT", text_color="black", image=iot_logo_img, state="DISABLED", fg_color="#f9f9fb", bg_color="#f9f9fb")
iot_logo.place(relx=.02, rely=.052, anchor="nw")
iot_messages_sent_day_label = CTk.CTkLabel(iot_frame, text="Messages Sent (24h)", text_color="grey", width=0, height=0)
iot_messages_sent_day_label.place(relx=.07, rely=.22, anchor="nw")
iot_messages_sent_day_value_label = CTk.CTkLabel(iot_frame, text="", width=0, height=0, text_color="black")
iot_messages_sent_day_value_label.place(relx=.07, rely=.35)
iot_frame_divider_frame = CTk.CTkFrame(iot_frame, width=1, bg_color="grey")
iot_frame_divider_frame.place(relx=.505, rely=.22, relheight=.215)
iot_fig = plt.Figure(figsize=(4, 1), dpi=100)
iot_fig.patch.set_facecolor("#f9f9fb")
iot_graph_canvas = FigureCanvasTkAgg(iot_fig, iot_frame)
iot_graph_canvas.get_tk_widget().place(relx=.29, rely=.58, relwidth=.7, relheight=.32)
ax = iot_fig.add_subplot(111)
iot_x = []
iot_y = []
for index in range(len(hotspot_data['count'])):
    iot_y.append(hotspot_data['count'][index]['value'])
for index in range(len(hotspot_data['count'])):
    iot_x.append(index)
ax.set_facecolor("#f9f9fb")
ax.set_xticks([])
ax.set_yticks([])
ax.set_xticklabels([])
ax.set_yticklabels([])
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.plot(iot_x, iot_y)
iot_graph_label = CTk.CTkLabel(iot_frame, width=0, height=0, text_color="grey", fg_color="#f9f9fb")
iot_graph_label.place(relx=.87, rely=.9, anchor="se")
iot_messages_sent_month_label = CTk.CTkLabel(iot_frame, text="Messages Sent (30d)", text_color="grey", width=0, height=0)
iot_messages_sent_month_label.place(relx=.6, rely=.22, anchor="nw")
iot_messages_sent_month_value_label = CTk.CTkLabel(iot_frame, text="", width=0, height=0, text_color="black")
iot_messages_sent_month_value_label.place(relx=.6, rely=.35)
iot_hotspots_label = CTk.CTkLabel(iot_frame, width=0, height=0, text="Hotspots", text_color="grey")
iot_hotspots_label.place(relx=.07, rely=.53, anchor="nw")
iot_hotspots_value_label = CTk.CTkLabel(iot_frame, width=0, height=0, text="", text_color="black")
iot_hotspots_value_label.place(relx=.07, rely=.65)
iot_hotspots_value_change_label = CTk.CTkLabel(iot_frame, width=0, height=0, text="")
iot_hotspots_value_change_label.place(relx=.07, rely=.83)

mobile_frame = CTk.CTkFrame(welcome_frame_bottom, fg_color="#f9f9fb")
mobile_frame.place(relx=.07, rely=.51, relwidth=.86, relheight=.16)
mobile_logo = CTk.CTkButton(mobile_frame, width=0, height=0, text="MOBILE", text_color="black", image=mobile_logo_img, state="DISABLED", fg_color="#f9f9fb", bg_color="#f9f9fb")
mobile_logo.place(relx=.02, rely=.052, anchor="nw")
mobile_label = CTk.CTkLabel(mobile_frame, text="5G Radios", text_color="grey", width=0, height=0)
mobile_label.place(relx=.07, rely=.32, anchor="nw")
mobile_radio_value_label = CTk.CTkLabel(mobile_frame, text_color="black", width=0, height=0)
mobile_radio_value_label.place(relx=.07, rely=.48, anchor="nw")
mobile_radio_value_change_label = CTk.CTkLabel(mobile_frame, width=0, height=0)
mobile_radio_value_change_label.place(relx=.07, rely=.74)
mobile_fig = plt.Figure(figsize=(4, 1), dpi=100)
mobile_fig.patch.set_facecolor("#f9f9fb")
mobile_graph_canvas = FigureCanvasTkAgg(mobile_fig, mobile_frame)
mobile_graph_canvas.get_tk_widget().place(relx=.25, rely=.33, relwidth=.75, relheight=.4)
bx = mobile_fig.add_subplot(111)
mobile_x = []
mobile_y = []
for index in range(len(mobile_data['count']) - 1):
    mobile_y.append(mobile_data['count'][index]['value'])
for index in range(len(mobile_data['count']) - 1):
    mobile_x.append(index)
bx.set_facecolor("#f9f9fb")
bx.set_xticks([])
bx.set_yticks([])
bx.set_xticklabels([])
bx.set_yticklabels([])
bx.spines['top'].set_visible(False)
bx.spines['right'].set_visible(False)
bx.spines['bottom'].set_visible(False)
bx.spines['left'].set_visible(False)
bx.plot(mobile_x, mobile_y)
mobile_graph_label = CTk.CTkLabel(mobile_frame, width=0, height=0, text_color="grey", fg_color="#f9f9fb")
mobile_graph_label.place(relx=.87, rely=.8, anchor="se")

hnt_price_frame = CTk.CTkFrame(welcome_frame_bottom, fg_color="#f9f9fb")
hnt_price_frame.place(relx=.07, rely=.69, relwidth=.4, relheight=.125)
hnt_market_cap_frame = CTk.CTkFrame(welcome_frame_bottom, fg_color="#f9f9fb")
hnt_market_cap_frame.place(relx=.5, rely=.69, relwidth=.4, relheight=.125)

def update_width_height(event):
    welcome_frame_top_width = welcome_frame_top.winfo_width()
    welcome_frame_top_height = welcome_frame_top.winfo_height()
    hnt_frame_width = hnt_frame.winfo_width()
    hnt_frame_height = hnt_frame.winfo_height()
    iot_frame_width = iot_frame.winfo_width()
    iot_frame_height = iot_frame.winfo_height()
    welcome_frame_top_width = welcome_frame_top.winfo_width()
    welcome_frame_top_height = welcome_frame_top.winfo_height()
    welcome_label1.configure(font=("Arial", (welcome_frame_top_height + welcome_frame_top_width) * .015))
    welcome_label2.configure(font=("Arial", (welcome_frame_top_height + welcome_frame_top_width) * .015, "bold"))
    welcome_label3.configure(font=("Arial", (welcome_frame_top_height + welcome_frame_top_width) * .009))
    hnt_logo.configure(font=("Arial", (hnt_frame_width + hnt_frame_height) * .025))
    block_height_label.configure(font=("Arial", (hnt_frame_width + hnt_frame_height) * .023))
    block_height_value_label.configure(font=("Arial", (hnt_frame_width + hnt_frame_height) * .04))
    block_height_change_label.configure(font=("Arial", (hnt_frame_width + hnt_frame_height) * .025))
    validators_online_label.configure(font=("Arial", (hnt_frame_width + hnt_frame_height) * .023))
    validators_online_value_label.configure(font=("Arial", (hnt_frame_width + hnt_frame_height) * .04))
    validators_online_change_label.configure(font=("Arial", (hnt_frame_width + hnt_frame_height) * .025))
    iot_logo.configure(font=("Arial", (iot_frame_width + iot_frame_height) * .025))
    iot_messages_sent_day_label.configure(font=("Arial", (iot_frame_width + iot_frame_height) * .022))
    iot_messages_sent_day_value_label.configure(font=("Arial", (iot_frame_width + iot_frame_height) * .046))
    iot_messages_sent_day_label.configure(font=("Arial", (iot_frame_width + iot_frame_height) * .022))
    iot_messages_sent_day_value_label.configure(font=("Arial", (iot_frame_width + iot_frame_height) * .032))
    iot_graph_label.configure(font=("Arial", (iot_frame_width + iot_frame_height) * .017))
    iot_messages_sent_month_label.configure(font=("Arial", (iot_frame_width + iot_frame_height) * .022))
    iot_messages_sent_month_value_label.configure(font=("Arial", (iot_frame_width + iot_frame_height) * .032))
    iot_hotspots_label.configure(font=("Arial", (iot_frame_width + iot_frame_height) * .022))
    iot_hotspots_value_label.configure(font=("Arial", (iot_frame_width + iot_frame_height) * .04))
    iot_hotspots_value_change_label.configure(font=("Arial", (iot_frame_width + iot_frame_height) * .0223))
    mobile_logo.configure(font=("Arial", (hnt_frame_width + hnt_frame_height) * .025))
    mobile_label.configure(font=("Arial", (hnt_frame_width + hnt_frame_height) * .024))
    mobile_radio_value_label.configure(font=("Arial", (hnt_frame_width + hnt_frame_height) * .044))
    mobile_radio_value_change_label.configure(font=("Arial", (iot_frame_width + iot_frame_height) * .0223))
    mobile_graph_label.configure(font=("Arial", (iot_frame_width + iot_frame_height) * .017))
    black_hnt_logo_img = CTk.CTkImage(dark_image=Image.open(".\\helium_logo_black.png"), size=((welcome_frame_top_width + welcome_frame_top_height) * .019, (welcome_frame_top_width + welcome_frame_top_height) * .019))
    blue_hnt_logo_img = CTk.CTkImage(dark_image=Image.open(".\\helium_logo_blue.png"), size=((welcome_frame_top_width + welcome_frame_top_height) * .016, (welcome_frame_top_width + welcome_frame_top_height) * .016))
    iot_logo_img = CTk.CTkImage(light_image=Image.open(".\\iot_logo.png"), size=((welcome_frame_top_width + welcome_frame_top_height) * .016, (welcome_frame_top_width + welcome_frame_top_height) * .016))
    mobile_logo_img = CTk.CTkImage(light_image=Image.open(".\\mobile_logo.png"), size=((welcome_frame_top_width + welcome_frame_top_height) * .016, (welcome_frame_top_width + welcome_frame_top_height) * .016))
    try:
        home_button.configure(image=black_hnt_logo_img)
        hnt_logo.configure(image=blue_hnt_logo_img)
        iot_logo.configure(image=iot_logo_img)
        mobile_logo.configure(image=mobile_logo_img)
    except:
        pass
    
explorer.bind('<Configure>', update_width_height)

def update_values_timer():
    update_values()
    explorer.after(300000, update_values_timer)

Thread(target=update_values_timer).start()

explorer.mainloop()
