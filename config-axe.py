import tkinter as tk
from tkinter import messagebox
import requests

# Variable to store the base API URL (starts empty to allow for full user configuration)
api_url = ""

# Function to set the API URL based on user input
def set_api_url():
    global api_url
    base_url = api_url_entry.get().strip()
    if base_url.startswith("http://"):
        api_url = base_url
        messagebox.showinfo("Success", f"API URL set to {api_url}")
    else:
        messagebox.showerror("Error", "Please enter a valid HTTP URL starting with 'http://'")

# Function to fetch system information from the ESP32 device
def get_system_info():
    if not api_url:
        messagebox.showerror("Error", "API URL is not set. Please set it first.")
        return
    try:
        response = requests.get(f"{api_url}/api/system/info")
        response.raise_for_status()
        data = response.json()
        populate_fields(data)
    except requests.RequestException as e:
        messagebox.showerror("Error", f"Failed to get system info: {e}")

# Populate the GUI fields with the fetched system information
def populate_fields(data):
    hostname_entry.delete(0, tk.END)
    hostname_entry.insert(0, data.get("hostname", ""))
    wifi_ssid_entry.delete(0, tk.END)
    wifi_ssid_entry.insert(0, data.get("ssid", ""))
    stratum_url_entry.delete(0, tk.END)
    stratum_url_entry.insert(0, data.get("stratumURL", ""))
    stratum_port_entry.delete(0, tk.END)
    stratum_port_entry.insert(0, data.get("stratumPort", ""))
    stratum_user_entry.delete(0, tk.END)
    stratum_user_entry.insert(0, data.get("stratumUser", ""))
    frequency_entry.delete(0, tk.END)
    frequency_entry.insert(0, data.get("frequency", ""))
    core_voltage_entry.delete(0, tk.END)
    core_voltage_entry.insert(0, data.get("coreVoltage", ""))

# Save configuration to the ESP32 device
def save_config():
    if not api_url:
        messagebox.showerror("Error", "API URL is not set. Please set it first.")
        return
    
    config = {
        "hostname": hostname_entry.get(),
        "ssid": wifi_ssid_entry.get(),
        "wifiPass": wifi_password_entry.get(),
        "stratumURL": stratum_url_entry.get(),
        "stratumPort": int(stratum_port_entry.get()),
        "stratumUser": stratum_user_entry.get(),
        "stratumPassword": stratum_password_entry.get(),
        "frequency": int(frequency_entry.get()),
        "coreVoltage": int(core_voltage_entry.get())
    }
    
    try:
        response = requests.patch(f"{api_url}/api/system", json=config)
        response.raise_for_status()
        messagebox.showinfo("Success", "Configuration saved successfully!")
    except requests.RequestException as e:
        messagebox.showerror("Error", f"Failed to save configuration: {e}")

# Restart the ESP32 device
def restart_device():
    if not api_url:
        messagebox.showerror("Error", "API URL is not set. Please set it first.")
        return
    try:
        response = requests.post(f"{api_url}/api/system/restart")
        response.raise_for_status()
        messagebox.showinfo("Success", "Device restarted successfully!")
    except requests.RequestException as e:
        messagebox.showerror("Error", f"Failed to restart device: {e}")

# GUI setup
root = tk.Tk()
root.title("Bitaxe Configuration tool - by wssh: https://afflicted.sh")

# API URL configuration
tk.Label(root, text="API Base URL").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
api_url_entry = tk.Entry(root, width=30)
api_url_entry.grid(row=0, column=1, padx=5, pady=5)
set_api_url_button = tk.Button(root, text="Set API URL", command=set_api_url)
set_api_url_button.grid(row=0, column=2, padx=5, pady=5)

# Configuration fields for user input
fields = [
    ("Hostname", "hostname"),
    ("WiFi SSID", "wifi_ssid"),
    ("WiFi Password", "wifi_password"),
    ("Stratum URL", "stratum_url"),
    ("Stratum Port", "stratum_port"),
    ("Stratum User", "stratum_user"),
    ("Stratum Password", "stratum_password"),
    ("Frequency", "frequency"),
    ("Core Voltage", "core_voltage")
]

entries = {}
for idx, (label_text, var_name) in enumerate(fields, start=1):
    label = tk.Label(root, text=label_text)
    label.grid(row=idx, column=0, padx=5, pady=5, sticky=tk.W)
    
    entry = tk.Entry(root, show="*" if "password" in var_name else None)
    entry.grid(row=idx, column=1, padx=5, pady=5)
    entries[var_name] = entry

# Entry assignments for easy reference
hostname_entry = entries["hostname"]
wifi_ssid_entry = entries["wifi_ssid"]
wifi_password_entry = entries["wifi_password"]
stratum_url_entry = entries["stratum_url"]
stratum_port_entry = entries["stratum_port"]
stratum_user_entry = entries["stratum_user"]
stratum_password_entry = entries["stratum_password"]
frequency_entry = entries["frequency"]
core_voltage_entry = entries["core_voltage"]

# Buttons for fetch, save, and restart actions
fetch_button = tk.Button(root, text="Fetch Config", command=get_system_info)
fetch_button.grid(row=len(fields) + 1, column=0, padx=5, pady=5)

save_button = tk.Button(root, text="Save Config", command=save_config)
save_button.grid(row=len(fields) + 1, column=1, padx=5, pady=5)

restart_button = tk.Button(root, text="Restart Device", command=restart_device)
restart_button.grid(row=len(fields) + 2, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()
