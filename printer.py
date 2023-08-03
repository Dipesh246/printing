import subprocess

def print_text_unix(file, printer_name):
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



