# Script: 019_build_project.py

import subprocess

def build_project():
    """
    Builds the project by running the 'make clean' and 'make all' commands.
    Uses the subprocess module to execute shell commands.
    :return: None
    """
    try:
        # Run 'make clean' to clean the build environment
        subprocess.run(['make', 'clean'], check=True)
        
        # Run 'make all' to build the project
        subprocess.run(['make', 'all'], check=True)
    
    except subprocess.CalledProcessError as e:
        # Handle error if any of the subprocess commands fail
        print(f"Error occurred during the build process: {e}")
        return False
    
    print("Build completed successfully.")
    return True

if __name__ == "__main__":
    # Invoke the build function
    build_project()
