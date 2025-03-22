# Script: 008_deploy_git_project.py

import subprocess
import os

def run_command(command, working_directory=None):
    """
    Executes a shell command and prints its output.
    Exits the script if the command fails.
    """
    try:
        result = subprocess.run(command, shell=True, check=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=working_directory)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.stderr}")
        exit(1)

def git_clone(repo_url, clone_path):
    """
    Clones a Git repository to the specified path.
    Creates the directory if it does not exist.
    """
    if not os.path.exists(clone_path):
        os.makedirs(clone_path)
        print(f"Created directory: {clone_path}")
    else:
        print(f"Directory already exists: {clone_path}")
    run_command(f"git clone {repo_url} .", clone_path)

def install_dependencies(working_directory):
    """
    Installs project dependencies from a requirements.txt file.
    """
    requirements_file = os.path.join(working_directory, "requirements.txt")
    if os.path.exists(requirements_file):
        run_command("pip install -r requirements.txt", working_directory)
    else:
        print(f"No requirements.txt found in {working_directory}. Skipping dependency installation.")

def deploy_application(working_directory):
    """
    Deploys the application. Add your deployment-specific steps here.
    """
    print(f"Deploying application in {working_directory}")
    # Example: Run an application-specific script or command
    run_command("python app.py", working_directory)

if __name__ == "__main__":
    # Configuration
    repo_url = 'https://github.com/your-username/your-repo.git'  # Replace with your repository URL
    clone_path = '/path/to/your/project'  # Replace with the desired local path
    
    # Script execution
    git_clone(repo_url, clone_path)
    install_dependencies(clone_path)
    deploy_application(clone_path)
