import subprocess
from nicegui import ui

with ui.fab('navigation', label='Transport'):
    ui.fab_action('train', on_click=lambda: ui.notify('Wifi'))
    ui.fab_action('sailing', on_click=lambda: ui.notify('Wifi'))
    ui.fab_action('rocket', on_click=lambda: ui.notify('Wifi'))

print("Choose a process to proceed: ")
print("1. Show all available networks")
print("2. show informations from all available networks")

choice = input("Enter your choice [1 or 2]: ")
print("You selected option:", choice)

if choice == "1":
    devices = subprocess.check_output(['netsh','wlan','show','profiles'])
    networks = subprocess.check_output(['netsh', 'wlan', 'show', 'networks', 'mode=Bssid'])
    devices = devices.decode('ascii')
    devices= devices.replace("\r","")
    print(devices)

elif choice == "2":
    devices = subprocess.check_output(['netsh','wlan','show','profiles'])
    networks = subprocess.check_output(['netsh', 'wlan', 'show', 'networks', 'mode=Bssid'])
    networks = networks.decode('ascii')
    networks= networks.replace("\r","")
    print(networks)

else:
    print("Invalid choice.")
    exit()

password_choice = input("Do you want to know the saved password? (y/n): ").strip().lower()

if password_choice == "y":
    profile = input("Enter the profile (SSID) name: ").strip()
    password = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', profile, 'key=clear'])
    if profile:
        print(f"Password for {profile} is: {password.decode('ascii')}")
    else:
        print(f"No saved password found for '{profile}'. It may be an open network, "
              "or the profile doesn't exist on this PC.")
elif password_choice == "n":
    print("You chose not to retrieve the password.")
else:
    print("Invalid choice.")
    exit()

ui.run(native="run")