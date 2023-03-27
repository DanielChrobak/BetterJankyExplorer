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

def place_home_screen():
    global on_home_screen
    welcome_frame_top.place(relx=0, rely=0, relwidth=.2, relheight=.25)
    home_button.place(relx=.01, rely=.018)
    welcome_label1.place(relx=.07, rely=.5)
    welcome_label2.place(relx=.07, rely=.6)
    welcome_label3.place(relx=.07, rely=.75)
    welcome_frame_bottom.place(relx=0, rely=.25, relwidth=.2, relheight=.75)
    hnt_frame.place(relx=.07, rely=.038, relwidth=.86, relheight=.18)
    hnt_logo.place(relx=.02, rely=.061, anchor="nw")
    hnt_price_label.place(relx=.95, rely=.1, anchor="ne")
    block_height_label.place(relx=.07, rely=.33, anchor="nw")
    block_height_value_label.place(relx=.07, rely=.48)
    block_height_change_label.place(relx=.07, rely=.73)
    hnt_frame_divider_frame.place(relx=.48, rely=.38, relheight=.37)
    validators_online_label.place(relx=.6, rely=.33, anchor="nw")
    validators_online_value_label.place(relx=.6, rely=.48)
    validators_online_change_label.place(relx=.6, rely=.73)
    iot_frame.place(relx=.07, rely=.24, relwidth=.86, relheight=.25)
    iot_logo.place(relx=.02, rely=.052, anchor="nw")
    iot_messages_sent_day_label.place(relx=.07, rely=.22, anchor="nw")
    iot_messages_sent_day_value_label.place(relx=.07, rely=.35)
    iot_frame_divider_frame.place(relx=.52, rely=.22, relheight=.215)
    iot_graph_label.place(relx=.87, rely=.9, anchor="se")
    iot_messages_sent_month_label.place(relx=.6, rely=.22, anchor="nw")
    iot_messages_sent_month_value_label.place(relx=.6, rely=.35)
    iot_hotspots_label.place(relx=.07, rely=.53, anchor="nw")
    iot_hotspots_value_label.place(relx=.07, rely=.65)
    iot_hotspots_value_change_label.place(relx=.07, rely=.83)
    mobile_frame.place(relx=.07, rely=.51, relwidth=.86, relheight=.16)
    mobile_logo.place(relx=.02, rely=.052, anchor="nw")
    mobile_label.place(relx=.07, rely=.32, anchor="nw")
    mobile_radio_value_label.place(relx=.07, rely=.48, anchor="nw")
    mobile_radio_value_change_label.place(relx=.07, rely=.74)
    mobile_graph_label.place(relx=.87, rely=.8, anchor="se")
    hnt_price_frame.place(relx=.07, rely=.69, relwidth=.41, relheight=.125)
    hnt_market_price_label_bottom.place(relx=.07, rely=.1, anchor="nw")
    hnt_price_label_value_bottom.place(relx=.07, rely=.37, anchor="nw")
    hnt_price_change_label_percentage_one_day.place(relx=.07, rely=.67, anchor="nw")
    hnt_market_cap_frame.place(relx=.52, rely=.69, relwidth=.41, relheight=.125)
    hnt_market_cap_label.place(relx=.07, rely=.1, anchor="nw")
    hnt_market_cap_value_label.place(relx=.07, rely=.37, anchor="nw")
    hnt_volume_value_label.place(relx=.07, rely=.65, anchor="nw")
    dc_spent_30_days_frame.place(relx=.07, rely=.835, relwidth=.41, relheight=.125)
    dc_spent_30_days_label.place(relx=.07, rely=.1, anchor="nw")
    dc_spent_30_days_value_label.place(relx=.07, rely=.37, anchor="nw")
    dc_spent_30_days_value_usd_label.place(relx=.07, rely=.67, anchor="nw")
    hnt_staked_frame.place(relx=.52, rely=.835, relwidth=.41, relheight=.125)
    hnt_staked_label.place(relx=.07, rely=.1, anchor="nw")
    hnt_staked_value_label.place(relx=.07, rely=.37, anchor="nw")
    hnt_staked_value_usd_label.place(relx=.07, rely=.67, anchor="nw")
    on_home_screen = True

def update_values():
    if on_home_screen == True:
        block_height_value_label.configure(text=f"{format(block_data['height'][len(block_data['height']) - 1]['value'], ',d')}")
        if int(block_data['height'][len(block_data['height']) - 1]['value']) - int(block_data['height'][0]['value']) > 0:
            block_height_change_label.configure(text=f"+{format(int(block_data['height'][len(block_data['height']) - 1]['value']) - int(block_data['height'][0]['value']), ',d')}", text_color="green")
        elif int(block_data['height'][len(block_data['height']) - 1]['value']) - int(block_data['height'][0]['value']) == 0:
            block_height_change_label.configure(text=f"+{format(int(block_data['height'][len(block_data['height']) - 1]['value']) - int(block_data['height'][0]['value']), ',d')}", color="grey")
        validators_online_value_label.configure(text=f"{format(validator_data['count'][len(validator_data['count']) - 1]['value'], ',d')}")
        if int(validator_data['count'][len(validator_data['count']) - 1]['value']) - int(validator_data['count'][0]['value']) > 0:
            validators_online_change_label.configure(text=f"+{format(int(validator_data['count'][len(validator_data['count']) - 1]['value']) - int(validator_data['count'][0]['value']), ',d')}", text_color="green")
        elif int(validator_data['count'][len(validator_data['count']) - 1]['value']) - int(validator_data['count'][0]['value']) < 0:
            validators_online_change_label.configure(text=f"{format(int(validator_data['count'][len(validator_data['count']) - 1]['value']) - int(validator_data['count'][0]['value']), ',d')}", text_color="blue")
        elif int(validator_data['count'][len(validator_data['count']) - 1]['value']) - int(validator_data['count'][0]['value']) == 0:
            validators_online_change_label.configure(text=f"{format(int(validator_data['count'][len(validator_data['count']) - 1]['value']) - int(validator_data['count'][0]['value']), ',d')}", text_color="grey")
        hnt_price_label.configure(text=f"${market_data['market_data']['current_price']['usd']:.2f}")
        iot_hotspots_value_label.configure(text=f"{format(hotspot_data['count'][len(hotspot_data['count']) - 1]['value'], ',d')}")
        if dc_burn_data['data']['last_day']['state_channel'] >= 10**9:
            iot_messages_sent_day_value_label.configure(text=f"{dc_burn_data['data']['last_day']['state_channel']/10**9:.3f}B")
        elif dc_burn_data['data']['last_day']['state_channel'] >= 10**6:
            iot_messages_sent_day_value_label.configure(text=f"{dc_burn_data['data']['last_day']['state_channel']/10**6:.3f}M")
        if dc_burn_data['data']['last_month']['state_channel'] >= 10**9:
            iot_messages_sent_month_value_label.configure(text=f"{dc_burn_data['data']['last_month']['state_channel']/10**9:.3f}B")
        elif dc_burn_data['data']['last_month']['state_channel'] >= 10**6:
            iot_messages_sent_month_value_label.configure(text=f"{dc_burn_data['data']['last_month']['state_channel']/10**6:.3f}M")  
        if int(hotspot_data['count'][len(hotspot_data['count']) - 1]['value']) - int(hotspot_data['count'][0]['value']) > 0:
            iot_hotspots_value_change_label.configure(text=f"+{format(int(hotspot_data['count'][len(hotspot_data['count']) - 1]['value']) - int(hotspot_data['count'][0]['value']), ',d')}", text_color="green")
        elif int(hotspot_data['count'][len(hotspot_data['count']) - 1]['value']) - int(hotspot_data['count'][0]['value']) == 0:
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
        if int(mobile_data['count'][len(mobile_data['count']) - 1]['value']) - int(mobile_data['count'][0]['value']) > 0:
            mobile_radio_value_change_label.configure(text=f"+{format(int(mobile_data['count'][len(mobile_data['count']) - 1]['value']) - int(mobile_data['count'][0]['value']), ',d')}", text_color="green")
        elif int(mobile_data['count'][len(mobile_data['count']) - 1]['value']) - int(mobile_data['count'][0]['value']) < 0:
            mobile_radio_value_change_label.configure(text=f"{format(int(mobile_data['count'][len(mobile_data['count']) - 1]['value']) - int(mobile_data['count'][0]['value']), ',d')}", text_color="blue")
        elif int(mobile_data['count'][len(mobile_data['count']) - 1]['value']) - int(mobile_data['count'][0]['value']) == 0:
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
        hnt_price_label_value_bottom.configure(text=f"${market_data['market_data']['current_price']['usd']:.2f}")
        if int(market_data['market_data']['price_change_percentage_24h_in_currency']['usd']) > 0:
            hnt_price_change_label_percentage_one_day.configure(text=f"+{market_data['market_data']['price_change_percentage_24h_in_currency']['usd']:.2f}%", text_color="green")
        elif int(market_data['market_data']['price_change_percentage_24h_in_currency']['usd']) < 0:
            hnt_price_change_label_percentage_one_day.configure(text=f"-{market_data['market_data']['price_change_percentage_24h_in_currency']['usd']:.2f}%", text_color="blue")
        elif int(market_data['market_data']['price_change_percentage_24h_in_currency']['usd']) == 0:
            hnt_price_change_label_percentage_one_day.configure(text=f"{market_data['market_data']['price_change_percentage_24h_in_currency']['usd']:.2f}%", text_color="grey")
        hnt_market_cap_value_label.configure(text=f"${market_data['market_data']['market_cap']['usd']:.2f}")
        if market_data['market_data']['market_cap']['usd'] >= 10**9:
            hnt_market_cap_value_label.configure(text=f"${market_data['market_data']['market_cap']['usd']/10**9:.3f}B")
        elif market_data['market_data']['market_cap']['usd'] >= 10**6:
            hnt_market_cap_value_label.configure(text=f"${market_data['market_data']['market_cap']['usd']/10**6:.3f}M")
        if market_data['market_data']['total_volume']['usd'] >= 10**9:
            hnt_volume_value_label.configure(text=f"Vol: ${market_data['market_data']['market_cap']['usd']/10**9:.3f}B")
        elif market_data['market_data']['total_volume']['usd'] >= 10**6:
            hnt_volume_value_label.configure(text=f"Vol: ${market_data['market_data']['market_cap']['usd']/10**6:.3f}M")
        if dc_burn_data['data']['last_month']['total'] >= 10**9:
            dc_spent_30_days_value_label.configure(text=f"{dc_burn_data['data']['last_month']['total']/10**9:.3f}B")
        elif dc_burn_data['data']['last_month']['total'] >= 10**6:
            dc_spent_30_days_value_label.configure(text=f"{dc_burn_data['data']['last_month']['total']/10**6:.3f}M")
        dc_spent_30_days_value_usd_label.configure(text=f"${int(dc_burn_data['data']['last_month']['total']) * .00001:,.2f}")
        hnt_staked_value_label.configure(text=f"{int(validator_data['count'][len(validator_data['count']) - 1]['value']) * 10000/10**6:.1f}M")  
        hnt_staked_value_usd_label.configure(text=f"${int(validator_data['count'][len(validator_data['count']) - 1]['value']) * 10000 * market_data['market_data']['current_price']['usd']:,.2f}")

def update_size(event):
    if on_home_screen == True:
        welcome_label1.configure(font=("Arial", (welcome_frame_top.winfo_width() + welcome_frame_top.winfo_height()) * .03))
        welcome_label2.configure(font=("Arial", (welcome_frame_top.winfo_width() + welcome_frame_top.winfo_height()) * .03, "bold"))
        welcome_label3.configure(font=("Arial", (welcome_frame_top.winfo_width() + welcome_frame_top.winfo_height()) * .02))
        hnt_logo.configure(font=("Arial", (welcome_frame_bottom.winfo_width() + welcome_frame_bottom.winfo_height()) * .015))
        hnt_price_label.configure(font=("Arial", (welcome_frame_bottom.winfo_width() + welcome_frame_bottom.winfo_height()) * .013))
        block_height_label.configure(font=("Arial", (welcome_frame_bottom.winfo_width() + welcome_frame_bottom.winfo_height()) * .011))
        block_height_value_label.configure(font=("Arial", (welcome_frame_bottom.winfo_width() + welcome_frame_bottom.winfo_height()) * .02))
        block_height_change_label.configure(font=("Arial", (welcome_frame_bottom.winfo_width() + welcome_frame_bottom.winfo_height()) * .013))
        validators_online_label.configure(font=("Arial", (welcome_frame_bottom.winfo_width() + welcome_frame_bottom.winfo_height()) * .011))
        validators_online_value_label.configure(font=("Arial", (welcome_frame_bottom.winfo_width() + welcome_frame_bottom.winfo_height()) * .02))
        validators_online_change_label.configure(font=("Arial", (welcome_frame_bottom.winfo_width() + welcome_frame_bottom.winfo_height()) * .013))
        iot_logo.configure(font=("Arial", (welcome_frame_bottom.winfo_width() + welcome_frame_bottom.winfo_height()) * .015))
        iot_messages_sent_day_label.configure(font=("Arial", (welcome_frame_bottom.winfo_width() + welcome_frame_bottom.winfo_height()) * .011))
        iot_messages_sent_day_value_label.configure(font=("Arial", (welcome_frame_bottom.winfo_width() + welcome_frame_bottom.winfo_height()) * .02))
        iot_graph_label.configure(font=("Arial", (welcome_frame_bottom.winfo_width() + welcome_frame_bottom.winfo_height()) * .01))
        iot_messages_sent_month_label.configure(font=("Arial", (welcome_frame_bottom.winfo_width() + welcome_frame_bottom.winfo_height()) * .011))
        iot_messages_sent_month_value_label.configure(font=("Arial", (welcome_frame_bottom.winfo_width() + welcome_frame_bottom.winfo_height()) * .02))
        iot_hotspots_label.configure(font=("Arial", (welcome_frame_bottom.winfo_width() + welcome_frame_bottom.winfo_height()) * .011))
        iot_hotspots_value_label.configure(font=("Arial", (welcome_frame_bottom.winfo_width() + welcome_frame_bottom.winfo_height()) * .02))
        iot_hotspots_value_change_label.configure(font=("Arial", (welcome_frame_bottom.winfo_width() + welcome_frame_bottom.winfo_height()) * .013))
        mobile_logo.configure(font=("Arial", (welcome_frame_bottom.winfo_width() + welcome_frame_bottom.winfo_height()) * .015))
        mobile_label.configure(font=("Arial", (welcome_frame_bottom.winfo_width() + welcome_frame_bottom.winfo_height()) * .011))
        mobile_radio_value_label.configure(font=("Arial", (welcome_frame_bottom.winfo_width() + welcome_frame_bottom.winfo_height()) * .02))
        mobile_radio_value_change_label.configure(font=("Arial", (welcome_frame_bottom.winfo_width() + welcome_frame_bottom.winfo_height()) * .013))
        mobile_graph_label.configure(font=("Arial", (welcome_frame_bottom.winfo_width() + welcome_frame_bottom.winfo_height()) * .01))
        updated_blue_hnt_img = CTk.CTkImage(light_image=blue_hnt_logo_img, size=((welcome_frame_bottom.winfo_width() + welcome_frame_bottom.winfo_height()) * .023, (welcome_frame_bottom.winfo_width() + welcome_frame_bottom.winfo_height()) * .023))
        updated_iot_img = CTk.CTkImage(light_image=iot_logo_img, size=((welcome_frame_bottom.winfo_width() + welcome_frame_bottom.winfo_height()) * .023, (welcome_frame_bottom.winfo_width() + welcome_frame_bottom.winfo_height()) * .023))
        update_mobile_img = CTk.CTkImage(light_image=mobile_logo_img, size=((welcome_frame_bottom.winfo_width() + welcome_frame_bottom.winfo_height()) * .023, (welcome_frame_bottom.winfo_width() + welcome_frame_bottom.winfo_height()) * .023))
        hnt_logo.configure(image=updated_blue_hnt_img)
        iot_logo.configure(image=updated_iot_img)
        mobile_logo.configure(image=update_mobile_img)
        hnt_market_price_label_bottom.configure(font=("Arial", (welcome_frame_bottom.winfo_width() + welcome_frame_bottom.winfo_height()) * .011))
        hnt_price_label_value_bottom.configure(font=("Arial", (welcome_frame_bottom.winfo_width() + welcome_frame_bottom.winfo_height()) * .015))
        hnt_price_change_label_percentage_one_day.configure(font=("Arial", (welcome_frame_bottom.winfo_width() + welcome_frame_bottom.winfo_height()) * .01))
        hnt_market_cap_label.configure(font=("Arial", (welcome_frame_bottom.winfo_width() + welcome_frame_bottom.winfo_height()) * .011))
        hnt_market_cap_value_label.configure(font=("Arial", (welcome_frame_bottom.winfo_width() + welcome_frame_bottom.winfo_height()) * .015))
        hnt_volume_value_label.configure(font=("Arial", (welcome_frame_bottom.winfo_width() + welcome_frame_bottom.winfo_height()) * .01))
        dc_spent_30_days_label.configure(font=("Arial", (welcome_frame_bottom.winfo_width() + welcome_frame_bottom.winfo_height()) * .011))
        dc_spent_30_days_value_label.configure(font=("Arial", (welcome_frame_bottom.winfo_width() + welcome_frame_bottom.winfo_height()) * .015))
        dc_spent_30_days_value_usd_label.configure(font=("Arial", (welcome_frame_bottom.winfo_width() + welcome_frame_bottom.winfo_height()) * .01))
        hnt_staked_label.configure(font=("Arial", (welcome_frame_bottom.winfo_width() + welcome_frame_bottom.winfo_height()) * .011))
        hnt_staked_value_label.configure(font=("Arial", (welcome_frame_bottom.winfo_width() + welcome_frame_bottom.winfo_height()) * .015))
        hnt_staked_value_usd_label.configure(font=("Arial", (welcome_frame_bottom.winfo_width() + welcome_frame_bottom.winfo_height()) * .01))
    if on_validators_screen == True:
        validators_screen_label.configure(font=("Arial", (validators_screen_top_frame.winfo_width() +validators_screen_top_frame.winfo_height()) * .045, "bold"))

    updated_black_hnt_img = CTk.CTkImage(dark_image=black_hnt_logo_img, size=((back_frame.winfo_width() + back_frame.winfo_height()) * .012, (back_frame.winfo_width() + back_frame.winfo_height()) * .012))
    home_button.configure(image=updated_black_hnt_img)

def place_validators_screen(none):
    global on_validators_screen
    forget_home_screen(none)
    home_button.lift()
    validators_screen_top_frame.place(relx=0, rely=0, relwidth=.2, relheight=.15)
    validators_screen_label.place(relx=.07, rely=.85)
    validators_screen_bottom_frame.place(relx=0, rely=.175, relwidth=.2, relheight=.825)
    on_validators_screen = True

def home_screen_button():
    forget_validators_screen()
    place_home_screen()
    update_values()

def forget_validators_screen():
    global on_validators_screen
    validators_screen_top_frame.place_forget()
    validators_screen_bottom_frame.place_forget()
    on_validators_screen = False


def forget_home_screen(none):
    global on_home_screen
    welcome_frame_top.place_forget()
    welcome_frame_bottom.place_forget()
    on_home_screen = False

def update_values_timer():
    while True:
        update_values()
        sleep(60)
        
on_home_screen = False
on_validators_screen = False

black_hnt_logo_img = Image.open(".\\helium_logo_black.png")
blue_hnt_logo_img = Image.open(".\\helium_logo_blue.png")
iot_logo_img = Image.open(".\\iot_logo.png")
mobile_logo_img = Image.open(".\\mobile_logo.png")

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

explorer.title("Janky Explorer")
explorer.minsize(explorer.winfo_screenwidth() * .75, explorer.winfo_screenheight() * .75)
explorer.maxsize(explorer.winfo_screenwidth(), explorer.winfo_screenheight())

back_frame = CTk.CTkFrame(explorer, fg_color="#10182c")
back_frame.pack(fill='both', expand=True)

welcome_frame_top = CTk.CTkFrame(back_frame, fg_color="#10182c")
home_button = CTk.CTkButton(back_frame, bg_color="#10182c", fg_color="#10182c", text="", width=0, height=0, command=home_screen_button, image=CTk.CTkImage(light_image=black_hnt_logo_img), hover=False)
welcome_label1 = CTk.CTkLabel(welcome_frame_top, text="Welcome to", width=0, height=0)
welcome_label2 = CTk.CTkLabel(welcome_frame_top, text="Janky Explorer", width=0, height=0)
welcome_label3 = CTk.CTkLabel(welcome_frame_top, text="Janky Explorer is a recreation of the Helium Explorer\nand is an Analytics App for Helium, a decentralized\nwireless connectivity platform.", justify="left", width=0, height=0)

welcome_frame_bottom = CTk.CTkFrame(back_frame, fg_color="#fefffe")
hnt_frame = CTk.CTkFrame(welcome_frame_bottom, fg_color="#f9f9fb")
hnt_logo = CTk.CTkButton(hnt_frame, width=0, height=0, text="HNT", text_color="black", state="DISABLED", fg_color="#f9f9fb", bg_color="#f9f9fb", image=CTk.CTkImage(light_image=blue_hnt_logo_img))
hnt_price_label = CTk.CTkLabel(hnt_frame, width=0, height=0, text_color="black", text="")
block_height_label = CTk.CTkLabel(hnt_frame, width=0, height=0, text="Block Height", text_color="grey")
block_height_value_label = CTk.CTkLabel(hnt_frame, width=0, height=0, text_color="black", text="")
block_height_change_label = CTk.CTkLabel(hnt_frame, width=0, height=0, text="")
hnt_frame_divider_frame = CTk.CTkFrame(hnt_frame, width=1, bg_color="grey")
validators_online_label = CTk.CTkLabel(hnt_frame, width=0, height=0, text="Validators Online", text_color="grey")
validators_online_value_label = CTk.CTkLabel(hnt_frame, width=0, height=0, text_color="black", text="")
validators_online_change_label = CTk.CTkLabel(hnt_frame, width=0, height=0, text="")
for widget in hnt_frame.winfo_children():
    widget.bind("<Button-1>", place_validators_screen)
hnt_frame.bind("<Button-1>", place_validators_screen)

iot_frame = CTk.CTkFrame(welcome_frame_bottom, fg_color="#f9f9fb")
iot_logo = CTk.CTkButton(iot_frame, width=0, height=0, text="IOT", text_color="black", state="DISABLED", fg_color="#f9f9fb", bg_color="#f9f9fb", image=CTk.CTkImage(light_image=iot_logo_img))
iot_messages_sent_day_label = CTk.CTkLabel(iot_frame, text="Messages Sent (24h)", text_color="grey", width=0, height=0)
iot_messages_sent_day_value_label = CTk.CTkLabel(iot_frame, text="", width=0, height=0, text_color="black")
iot_frame_divider_frame = CTk.CTkFrame(iot_frame, width=1, bg_color="grey")
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
iot_messages_sent_month_label = CTk.CTkLabel(iot_frame, text="Messages Sent (30d)", text_color="grey", width=0, height=0)
iot_messages_sent_month_value_label = CTk.CTkLabel(iot_frame, text="", width=0, height=0, text_color="black")
iot_hotspots_label = CTk.CTkLabel(iot_frame, width=0, height=0, text="Hotspots", text_color="grey")
iot_hotspots_value_label = CTk.CTkLabel(iot_frame, width=0, height=0, text="", text_color="black")
iot_hotspots_value_change_label = CTk.CTkLabel(iot_frame, width=0, height=0, text="")
for widget in iot_frame.winfo_children():
    widget.bind("<Button-1>", place_validators_screen)
iot_frame.bind("<Button-1>", place_validators_screen)

mobile_frame = CTk.CTkFrame(welcome_frame_bottom, fg_color="#f9f9fb")
mobile_logo = CTk.CTkButton(mobile_frame, width=0, height=0, text="MOBILE", text_color="black", state="DISABLED", fg_color="#f9f9fb", bg_color="#f9f9fb", image=CTk.CTkImage(light_image=mobile_logo_img))
mobile_label = CTk.CTkLabel(mobile_frame, text="5G Radios", text_color="grey", width=0, height=0)
mobile_radio_value_label = CTk.CTkLabel(mobile_frame, text_color="black", width=0, height=0)
mobile_radio_value_change_label = CTk.CTkLabel(mobile_frame, width=0, height=0)
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
for widget in mobile_frame.winfo_children():
    widget.bind("<Button-1>", place_validators_screen)
mobile_frame.bind("<Button-1>", place_validators_screen)

hnt_price_frame = CTk.CTkFrame(welcome_frame_bottom, fg_color="#f9f9fb")
hnt_market_price_label_bottom = CTk.CTkLabel(hnt_price_frame, fg_color="#f9f9fb", text="HNT Market Price", text_color="grey")
hnt_price_label_value_bottom = CTk.CTkLabel(hnt_price_frame, fg_color="#f9f9fb", text_color="black")
hnt_price_change_label_percentage_one_day = CTk.CTkLabel(hnt_price_frame, fg_color="#f9f9fb", text_color="grey")
for widget in hnt_price_frame.winfo_children():
    widget.bind("<Button-1>", place_validators_screen)
hnt_price_frame.bind("<Button-1>", place_validators_screen)

hnt_market_cap_frame = CTk.CTkFrame(welcome_frame_bottom, fg_color="#f9f9fb")
hnt_market_cap_label = CTk.CTkLabel(hnt_market_cap_frame, fg_color="#f9f9fb", text="HNT Market Cap", text_color="grey")
hnt_market_cap_value_label = CTk.CTkLabel(hnt_market_cap_frame, fg_color="#f9f9fb", text_color="black")
hnt_volume_value_label = CTk.CTkLabel(hnt_market_cap_frame, fg_color="#f9f9fb", text_color="grey")
for widget in hnt_market_cap_frame.winfo_children():
    widget.bind("<Button-1>", place_validators_screen)
hnt_market_cap_frame.bind("<Button-1>", place_validators_screen)

dc_spent_30_days_frame = CTk.CTkFrame(welcome_frame_bottom, fg_color="#f9f9fb")
dc_spent_30_days_label = CTk.CTkLabel(dc_spent_30_days_frame, fg_color="#f9f9fb", text="DC Spent (30d)", text_color="grey")
dc_spent_30_days_value_label = CTk.CTkLabel(dc_spent_30_days_frame, fg_color="#f9f9fb", text_color="black")
dc_spent_30_days_value_usd_label = CTk.CTkLabel(dc_spent_30_days_frame, fg_color="#f9f9fb", text_color="grey")
for widget in dc_spent_30_days_frame.winfo_children():
    widget.bind("<Button-1>", place_validators_screen)
dc_spent_30_days_frame.bind("<Button-1>", place_validators_screen)

hnt_staked_frame = CTk.CTkFrame(welcome_frame_bottom, fg_color="#f9f9fb")
hnt_staked_label = CTk.CTkLabel(hnt_staked_frame, fg_color="#f9f9fb", text="HNT Staked", text_color="grey")
hnt_staked_value_label = CTk.CTkLabel(hnt_staked_frame, fg_color="#f9f9fb", text_color="black")
hnt_staked_value_usd_label = CTk.CTkLabel(hnt_staked_frame, fg_color="#f9f9fb", text_color="grey")
for widget in hnt_staked_frame.winfo_children():
    widget.bind("<Button-1>", place_validators_screen)
hnt_staked_frame.bind("<Button-1>", place_validators_screen)

validators_screen_top_frame = CTk.CTkFrame(back_frame, fg_color="#10182c")
validators_screen_label = CTk.CTkLabel(validators_screen_top_frame, text="Validators", text_color="white")
validators_screen_bottom_frame = CTk.CTkFrame(back_frame, fg_color="#fefffe")




place_home_screen()

explorer.bind('<Configure>', update_size)

Thread(target=update_values_timer).start()

explorer.mainloop()
