import time
import subprocess
import pytest
import paramiko

SERVER_IP = "192.168.0.105"

@pytest.fixture(scope="function")
def server():
    username = "debian"
    password = "debian"
    iperf_command = "iperf -s -u"

    # Create an SSH client
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh_client.connect(hostname=SERVER_IP, username=username, password=password)
        ssh_client.exec_command("pkill -f 'iperf -s'")
        _, stdout, stderr = ssh_client.exec_command(f"{iperf_command} &")
        time.sleep(2)
        print("iperf server started successfully.")
        ssh_client.close()
    except Exception as err:
        return err

@pytest.fixture(scope="function")
def client():
    result = None
    error = None

    duration = 10
    interval = 1

    command = ["iperf", "-c", SERVER_IP, "-u", "-t", str(duration), "-i", str(interval), "-f", "M"]

    try:
        completed_process = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        result = completed_process.stdout
    except subprocess.CalledProcessError as e:
        error = f"Command failed with error: {e.stderr.strip()}"
    except Exception as e:
        error = f"Unexpected error: {str(e)}"

    return result, error