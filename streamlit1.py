import os
import streamlit as st

st.set_page_config(page_title="Docker & Linux Command Menu", layout="wide")
st.title("🧰 Docker & Linux Command Center")

with st.sidebar:
    st.header("Select Command")
    command = st.selectbox("Choose an action:", [
        "Launch Docker container",
        "Stop Docker container",
        "Start Docker container",
        "Remove Docker container",
        "List running containers",
        "List all containers",
        "List Docker images",
        "Show calendar",
        "Show date",
        "Make directory",
        "Create empty file",
        "List files",
        "Disk usage",
        "Memory usage",
        "CPU info",
        "Block devices",
        "Processes",
        "System uptime",
        "Network interfaces",
        "Ping host",
        "Download (wget)",
        "Download (curl -O)",
        "Create tar archive",
        "Extract tar archive",
        "Install package",
        "Update packages",
        "Reboot",
        "Shutdown",
        "Service status",
        "Start service",
        "Stop service",
        "Move file",
        "Copy file",
        "Remove file",
        "Remove folder",
        "Environment variables",
        "Top snapshot",
        "Groups",
        "Last logins",
        "Who is logged in",
        "Kernel messages",
        "Open ports",
        "Search in file",
        "Count lines in file",
        "Kernel version",
        "Clear screen",
    ])

if "output" not in st.session_state:
    st.session_state.output = ""

st.subheader(f"🔧 Selected: {command}")

if command == "Launch Docker container":
    image = st.text_input("Image name")
    cname = st.text_input("Container name")
    if st.button("Launch"):
        st.session_state.output = os.popen(f"docker run -d --name {cname} {image}").read()

elif command == "Stop Docker container":
    name = st.text_input("Container name/ID")
    if st.button("Stop"):
        st.session_state.output = os.popen(f"docker stop {name}").read()

elif command == "Start Docker container":
    name = st.text_input("Container name/ID")
    if st.button("Start"):
        st.session_state.output = os.popen(f"docker start {name}").read()

elif command == "Remove Docker container":
    name = st.text_input("Container name/ID")
    if st.button("Remove"):
        st.session_state.output = os.popen(f"docker rm {name}").read()

elif command == "List running containers":
    if st.button("Show"):
        st.session_state.output = os.popen("docker ps").read()

elif command == "List all containers":
    if st.button("Show"):
        st.session_state.output = os.popen("docker ps -a").read()

elif command == "List Docker images":
    if st.button("Show"):
        st.session_state.output = os.popen("docker images").read()

elif command == "Show calendar":
    if st.button("Calendar"):
        st.session_state.output = os.popen("cal").read()

elif command == "Show date":
    if st.button("Date"):
        st.session_state.output = os.popen("date").read()

elif command == "Make directory":
    d = st.text_input("Directory name")
    if st.button("Create Folder"):
        st.session_state.output = os.popen(f"mkdir -p {d}").read()

elif command == "Create empty file":
    f = st.text_input("File name")
    if st.button("Create File"):
        st.session_state.output = os.popen(f"touch {f}").read()

elif command == "List files":
    if st.button("List Files"):
        st.session_state.output = os.popen("ls -l").read()

elif command == "Disk usage":
    if st.button("Disk Info"):
        st.session_state.output = os.popen("df -h").read()

elif command == "Memory usage":
    if st.button("Memory Info"):
        st.session_state.output = os.popen("free -h").read()

elif command == "CPU info":
    if st.button("CPU Info"):
        st.session_state.output = os.popen("lscpu").read()

elif command == "Block devices":
    if st.button("Block Devices"):
        st.session_state.output = os.popen("lsblk").read()

elif command == "Processes":
    if st.button("Process List"):
        st.session_state.output = os.popen("ps aux | head -20").read()

elif command == "System uptime":
    if st.button("Uptime"):
        st.session_state.output = os.popen("uptime").read()

elif command == "Network interfaces":
    if st.button("Network"):
        st.session_state.output = os.popen("ip addr").read()

elif command == "Ping host":
    host = st.text_input("Host to ping")
    if st.button("Ping"):
        st.session_state.output = os.popen(f"ping -c 4 {host}").read()

elif command == "Download (wget)":
    url = st.text_input("URL")
    if st.button("Download"):
        st.session_state.output = os.popen(f"wget {url}").read()

elif command == "Download (curl -O)":
    url = st.text_input("URL")
    if st.button("Download"):
        st.session_state.output = os.popen(f"curl -O {url}").read()

elif command == "Create tar archive":
    arch = st.text_input("Archive name.tar")
    target = st.text_input("Target file/folder")
    if st.button("Create Archive"):
        st.session_state.output = os.popen(f"tar -cvf {arch} {target}").read()

elif command == "Extract tar archive":
    arch = st.text_input("Archive name.tar")
    if st.button("Extract"):
        st.session_state.output = os.popen(f"tar -xvf {arch}").read()

elif command == "Install package":
    pkg = st.text_input("Package name")
    if st.button("Install"):
        st.session_state.output = os.popen(f"sudo dnf install -y {pkg}").read()

elif command == "Update packages":
    if st.button("Update All"):
        st.session_state.output = os.popen("sudo dnf update -y").read()

elif command == "Reboot":
    if st.button("Reboot Now"):
        st.session_state.output = os.popen("sudo reboot").read()

elif command == "Shutdown":
    if st.button("Shutdown Now"):
        st.session_state.output = os.popen("sudo shutdown now").read()

elif command == "Service status":
    svc = st.text_input("Service name")
    if st.button("Check Status"):
        st.session_state.output = os.popen(f"systemctl status {svc}").read()

elif command == "Start service":
    svc = st.text_input("Service name")
    if st.button("Start Service"):
        st.session_state.output = os.popen(f"sudo systemctl start {svc}").read()

elif command == "Stop service":
    svc = st.text_input("Service name")
    if st.button("Stop Service"):
        st.session_state.output = os.popen(f"sudo systemctl stop {svc}").read()

elif command == "Move file":
    src = st.text_input("Source path")
    dst = st.text_input("Destination path")
    if st.button("Move"):
        st.session_state.output = os.popen(f"mv {src} {dst}").read()

elif command == "Copy file":
    src = st.text_input("Source path")
    dst = st.text_input("Destination path")
    if st.button("Copy"):
        st.session_state.output = os.popen(f"cp {src} {dst}").read()

elif command == "Remove file":
    file = st.text_input("File to delete")
    if st.button("Delete File"):
        st.session_state.output = os.popen(f"rm -f {file}").read()

elif command == "Remove folder":
    folder = st.text_input("Folder to delete")
    if st.button("Delete Folder"):
        st.session_state.output = os.popen(f"rm -rf {folder}").read()

elif command == "Environment variables":
    if st.button("Show ENV"):
        st.session_state.output = os.popen("printenv").read()

elif command == "Top snapshot":
    if st.button("Top"):
        st.session_state.output = os.popen("top -bn1 | head -20").read()

elif command == "Groups":
    if st.button("Groups"):
        st.session_state.output = os.popen("groups").read()

elif command == "Last logins":
    if st.button("Last 10 Logins"):
        st.session_state.output = os.popen("last -n 10").read()

elif command == "Who is logged in":
    if st.button("Who"):
        st.session_state.output = os.popen("who").read()

elif command == "Kernel messages":
    if st.button("dmesg | tail"):
        st.session_state.output = os.popen("dmesg | tail").read()

elif command == "Open ports":
    if st.button("Show Ports"):
        st.session_state.output = os.popen("ss -tuln").read()

elif command == "Search in file":
    pat = st.text_input("Search pattern")
    file = st.text_input("File to search")
    if st.button("Search"):
        st.session_state.output = os.popen(f"grep '{pat}' {file}").read()

elif command == "Count lines in file":
    file = st.text_input("File name")
    if st.button("Count"):
        st.session_state.output = os.popen(f"wc -l {file}").read()

elif command == "Kernel version":
    if st.button("Version"):
        st.session_state.output = os.popen("uname -r").read()

elif command == "Clear screen":
    st.session_state.output = ""

if st.session_state.output:
    st.subheader("📋 Output")
    st.code(st.session_state.output)
