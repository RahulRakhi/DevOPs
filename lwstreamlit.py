import streamlit as st
import subprocess
import os
# ------------------ Docker Command Data ------------------
docker_commands = {
    "docker build": {
        "description": "Builds a Docker image from a Dockerfile.",
        "usage": "docker build -t <image_name> .",
        "example": "docker build -t myapp ."
    },
    "docker run": {
        "description": "Runs a command in a new container.",
        "usage": "docker run [OPTIONS] IMAGE [COMMAND] [ARG...]",
        "example": "docker run -d --name mycontainer -p 8080:80 myapp"
    },
    "docker pull": {
        "description": "Pulls an image from a Docker registry.",
        "usage": "docker pull <image_name>",
        "example": "docker pull ubuntu"
    },
    "docker push": {
        "description": "Pushes an image to a Docker registry.",
        "usage": "docker push <image_name>",
        "example": "docker push yourusername/myapp"
    },
    "docker ps": {
        "description": "Lists running containers.",
        "usage": "docker ps [OPTIONS]",
        "example": "docker ps -a"
    },
    "docker stop": {
        "description": "Stops one or more running containers.",
        "usage": "docker stop <container_id>",
        "example": "docker stop 123abc456def"
    },
    "docker rm": {
        "description": "Removes one or more containers.",
        "usage": "docker rm <container_id>",
        "example": "docker rm 123abc456def"
    },
    "docker rmi": {
        "description": "Removes one or more images.",
        "usage": "docker rmi <image_id>",
        "example": "docker rmi myapp"
    },
    "docker images": {
        "description": "Lists all Docker images.",
        "usage": "docker images",
        "example": "docker images"
    },
    "docker exec": {
        "description": "Executes a command inside a running container.",
        "usage": "docker exec -it <container_id> <command>",
        "example": "docker exec -it mycontainer bash"
    },
    "docker logs": {
        "description": "Fetches logs of a container.",
        "usage": "docker logs <container_id>",
        "example": "docker logs mycontainer"
    },
    "docker network ls": {
        "description": "Lists all Docker networks.",
        "usage": "docker network ls",
        "example": "docker network ls"
    },
    "docker volume ls": {
        "description": "Lists all Docker volumes.",
        "usage": "docker volume ls",
        "example": "docker volume ls"
    },
    "docker inspect": {
        "description": "Returns detailed information on containers or images.",
        "usage": "docker inspect <name|id>",
        "example": "docker inspect mycontainer"
    },
    "docker stats": {
        "description": "Displays a live stream of container(s) resource usage statistics.",
        "usage": "docker stats",
        "example": "docker stats"
    },
    "docker rename": {
        "description": "Renames a container.",
        "usage": "docker rename <old_name> <new_name>",
        "example": "docker rename webapp backend"
    },
    "docker pause": {
        "description": "Pauses all processes within one or more containers.",
        "usage": "docker pause <container_id>",
        "example": "docker pause mycontainer"
    },
    "docker unpause": {
        "description": "Unpauses all processes within one or more containers.",
        "usage": "docker unpause <container_id>",
        "example": "docker unpause mycontainer"
    }
}

# ------------------ Streamlit UI ------------------
st.set_page_config(page_title="Docker Command Helper", page_icon="🐳")
st.title("🐳 Docker Command Helper with File Upload + Shell Access")
st.markdown("Use this tool to explore Docker commands, upload a Dockerfile, and run basic safe shell commands.")

# ----------- File Upload Section -------------
st.header("📁 Upload Your Dockerfile or Config Files")
uploaded_file = st.file_uploader("Choose a file", type=["Dockerfile", "txt", "sh", "yml", "yaml", "json", "conf"])

if uploaded_file is not None:
    file_path = os.path.join(".", uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.success(f"✅ File uploaded: `{uploaded_file.name}`")

    file_ext = uploaded_file.name.split('.')[-1] if "." in uploaded_file.name else "dockerfile"
    st.code(open(file_path).read(), language=file_ext)

# ----------- Docker Command Info Section -------------
st.header("📘 Docker Command Explorer")
selected_command = st.selectbox("Select a Docker Command", list(docker_commands.keys()))

if selected_command:
    cmd = docker_commands[selected_command]
    st.subheader(f"🔧 {selected_command}")
    st.markdown(f"**Description:** {cmd['description']}")
    st.code(cmd['usage'], language='bash')
    st.markdown("**Example:**")
    st.code(cmd['example'], language='bash')

# ----------- Search Section -------------
st.header("🔍 Search for a Docker Command")
search = st.text_input("Type to search", placeholder="e.g. build, ps, run")

if search:
    matches = [cmd for cmd in docker_commands if search.lower() in cmd.lower()]
    if matches:
        for match in matches:
            match_data = docker_commands[match]
            st.subheader(f"🔎 {match}")
            st.write(match_data["description"])
            st.code(match_data["usage"], language='bash')
            st.code(match_data["example"], language='bash')
    else:
        st.warning("No matching Docker commands found.")

# ----------- Run Custom Shell Command -------------
st.header("💻 Run Docker or Safe Shell Commands")

allowed_prefixes = ("docker", "ls", "pwd")
custom_command = st.text_input("Enter a command (safe commands only)", placeholder="e.g. docker ps -a")

if st.button("▶️ Run Command"):
    if custom_command.strip() == "":
        st.warning("⚠️ Please enter a command.")
    elif any(custom_command.startswith(prefix) for prefix in allowed_prefixes):
        try:
            result = subprocess.check_output(custom_command, shell=True, stderr=subprocess.STDOUT, text=True)
            st.success("✅ Command executed successfully:")
            st.code(result)
        except subprocess.CalledProcessError as e:
            st.error("❌ Command failed:")
            st.code(e.output)
    else:
        st.warning("⚠️ Only commands starting with `docker`, `ls`, or `pwd` are allowed for security reasons.")

# ----------- Footer -------------
st.markdown("---")
st.caption("💪 Created by Rahul • Streamlit-based Docker Tool")
