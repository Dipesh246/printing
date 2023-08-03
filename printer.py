import subprocess,platform

def print_text_unix(file, printer_name):
    system = platform.system()
    print("Os: ",system)
    if system == 'Linux' or system == 'MacOs':
        try:
            subprocess.run(["lpstat", "-p", printer_name], check=True, capture_output=True)
        except subprocess.CalledProcessError:
            print(f"Printer '{printer_name}' not found.")
            return

        try:
            subprocess.run(["lp", "-d", printer_name, file], check=True)
        except subprocess.CalledProcessError:
            print(f"Failed to print using printer '{printer_name}'.")
            return

        print(f"Printed successfully using printer '{printer_name}'.")

    if system == 'Windows':
        try:
            subprocess.run(["wmic", "printer", "where", f'name="{printer_name}"', "get", "name"], check=True, capture_output=True, text=True)
        except subprocess.CalledProcessError:
            print(f"Printer '{printer_name}' not found.")
            return

        try:
            subprocess.run(["cmd", "/c", "start", "/b", "notepad", "/p", file], check=True)
        except subprocess.CalledProcessError:
            print(f"Failed to print using printer '{printer_name}'.")
            return

        print(f"Printed successfully using printer '{printer_name}'.")




