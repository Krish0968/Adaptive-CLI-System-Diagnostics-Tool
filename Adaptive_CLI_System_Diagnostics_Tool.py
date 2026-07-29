import platform
import socket
import os

try:
    import psutil
except ImportError:
    psutil = None


def system_info():
    print("\n--- SYSTEM INFORMATION ---")
    print("OS:", platform.system())
    print("Version:", platform.version())
    print("Machine:", platform.machine())
    print("Processor:", platform.processor())
    print("Hostname:", socket.gethostname())
    print("Python:", platform.python_version())


def cpu_info():
    if psutil is None:
        print("psutil is not installed.")
        return
    print("\nCPU Usage:", psutil.cpu_percent(interval=1), "%")
    print("CPU Cores:", psutil.cpu_count())


def ram_info():
    if psutil is None:
        print("psutil is not installed.")
        return
    m = psutil.virtual_memory()
    print("\nTotal RAM:", round(m.total / 1024**3, 2), "GB")
    print("Used RAM:", round(m.used / 1024**3, 2), "GB")
    print("Available:", round(m.available / 1024**3, 2), "GB")
    print("Usage:", m.percent, "%")


def disk_info():
    if psutil is None:
        print("psutil is not installed.")
        return
    path = "C:\\" if os.name == "nt" else "/"
    d = psutil.disk_usage(path)
    print("\n--- DISK INFORMATION ---")
    print("Total Disk:", round(d.total / 1024**3, 2), "GB")
    print("Used Disk:", round(d.used / 1024**3, 2), "GB")
    print("Free Disk:", round(d.free / 1024**3, 2), "GB")
    print("Usage:", d.percent, "%")


def battery_info():
    if psutil is None:
        print("psutil is not installed.")
        return
    b = psutil.sensors_battery()
    if b:
        print("\nBattery:", b.percent, "%")
        print("Charging:", b.power_plugged)
    else:
        print("\nBattery Not Available")


def internet_check():
    try:
        socket.create_connection(("8.8.8.8", 53), 2)
        print("\nInternet Status: Connected")
    except:
        print("\nInternet Status: Not Connected")


while True:
    print("\n==== Adaptive CLI System Diagnostics Tool ====")
    print("1. System Information")
    print("2. CPU Usage")
    print("3. RAM Information")
    print("4. Disk Information")
    print("5. Battery Status")
    print("6. Internet Connectivity Check")
    print("7. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        system_info()
    elif choice == "2":
        cpu_info()
    elif choice == "3":
        ram_info()
    elif choice == "4":
        disk_info()
    elif choice == "5":
        battery_info()
    elif choice == "6":
        internet_check()
    elif choice == "7":
        print("Thank you!")
        break
    else:
        print("Invalid Choice. Please try again.")
