
## License

This repository is licensed under the Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License. It is provided for educational purposes only. Please refer to the LICENSE file for more details.

[![License: CC BY-NC-ND 4.0](https://licensebuttons.net/l/by-nc-nd/4.0/88x31.png)](https://creativecommons.org/licenses/by-nc-nd/4.0/)

# Disruption

This repository has highly volatile code and if downloaded may damage your computer.
This has a cron jobs function that fires it every three seconds. If blocked the first time it willtry again and again.
There are different versions for different things. If you cant read code copy to an AI service like GPT, Bing or Gemini and they will help you identify the various sections to be changed. 

# Search+Destroy

### Search+Destroy Report

#### Overview

The script provided is a harmful and malicious piece of software designed for system disruption and data destruction. Below is a detailed analysis of each component of the script and its implications for system security.

---

#### Components

1. **Local IP and Open Ports Discovery:**
   ```python
   def discover_local_ips_and_ports():
       ...
   ```
   - **Functionality:** Identifies local IP addresses and open ports on the machine.
   - **Details:** Utilizes `socket` and `psutil` libraries to gather information about the system’s network interfaces and connections.
   - **Security Implications:** Collecting IP addresses and open ports is a reconnaissance step, potentially used to plan subsequent attacks.

2. **Executable Permission Handling:**
   ```python
   def ensure_executable():
       ...
   ```
   - **Functionality:** Ensures the script has execute permissions on Linux systems.
   - **Details:** Uses `os.chmod` to modify file permissions.
   - **Security Implications:** Ensures the script can run automatically, contributing to persistence and making it harder to remove.

3. **Cron Job and Scheduled Task Creation:**
   ```python
   def add_cron_job():
       ...
   ```
   - **Functionality:** Sets up the script to execute at regular intervals.
   - **Details:** Adds a cron job for Linux or a scheduled task for Windows to run the script every minute.
   - **Security Implications:** Ensures that the script remains active and continues its disruptive activities, making it resilient to manual removal.

4. **CPU Stress Function:**
   ```python
   def cpu_stress():
       ...
   ```
   - **Functionality:** Consumes CPU resources indefinitely.
   - **Details:** Implements an infinite loop to keep the CPU busy.
   - **Security Implications:** Causes system slowdowns or crashes by overwhelming the CPU, effectively executing a denial-of-service attack.

5. **File Deletion Function:**
   ```python
   def delete_files(path):
       ...
   ```
   - **Functionality:** Deletes files from a specified directory.
   - **Details:** Traverses the directory and removes all files.
   - **Security Implications:** Leads to data loss and potential system damage by deleting important files.

6. **SYN Flood Attack:**
   ```python
   def syn_flood(target_ip, target_port):
       ...
   ```
   - **Functionality:** Sends SYN packets to a target IP and port.
   - **Details:** Implements a SYN Flood attack on non-Windows platforms.
   - **Security Implications:** Part of a Distributed Denial of Service (DDoS) attack, intended to overwhelm network services and disrupt connectivity.

7. **Process Termination:**
   ```python
   def kill_process(process_name):
       ...
   ```
   - **Functionality:** Terminates a specified process.
   - **Details:** Uses `taskkill` on Windows or `pkill` on Linux to end the process.
   - **Security Implications:** Disrupts critical system or application processes, potentially causing service outages.

8. **System Disruption Attack:**
   ```python
   def disrupt_system(important_directory, critical_process):
       ...
   ```
   - **Functionality:** Orchestrates a series of disruptive actions.
   - **Details:** Combines CPU stress, file deletion, network flooding, and process termination in a coordinated attack.
   - **Security Implications:** Comprehensive and destructive attack aimed at overwhelming and disabling the system.

---

#### Summary

The script is designed to execute a "search and destroy" operation, targeting various system resources and functionalities:

- **Persistence:** Ensures the script remains active through scheduled tasks and cron jobs.
- **Resource Exhaustion:** Uses CPU stress to degrade system performance.
- **Destruction:** Deletes files and terminates essential processes.
- **Network Attack:** Conducts SYN Flood attacks to disrupt network services.

**Ethical and Legal Considerations:** Deploying or utilizing this script is illegal and unethical. It constitutes a serious cyber attack that can result in criminal charges and significant damage to systems and data.

**Recommendation:** If discovered in a professional setting, treat this script as a critical security threat. Act promptly to isolate affected systems, remove the script, and conduct a thorough investigation to prevent further damage.
