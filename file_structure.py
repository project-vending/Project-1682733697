
import os

# Define project directory and subdirectories
project_directory = "realtime_dashboard_project"
subdirectories = ["data", "code", "docker", "dashboard"]

# Create project directory and subdirectories
os.mkdir(project_directory)
for subdirectory in subdirectories:
    os.mkdir(os.path.join(project_directory, subdirectory))

# Create empty files
with open(os.path.join(project_directory, "data", "streaming_data.csv"), "w") as f:
    pass
    
with open(os.path.join(project_directory, "code", "streaming_data_collector.py"), "w") as f:
    pass
    
with open(os.path.join(project_directory, "code", "data_processor.py"), "w") as f:
    pass
    
with open(os.path.join(project_directory, "dashboard", "streamlit_dashboard.py"), "w") as f:
    pass
