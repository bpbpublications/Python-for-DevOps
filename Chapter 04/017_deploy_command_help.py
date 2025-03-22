# Script: 017_deploy_command_help.py

import argparse

def main():
    """
    Main function to demonstrate conditional help message for a specific command.
    Displays additional help when the 'deploy' command is selected with the '--help' option.
    """
    # Create the argument parser
    parser = argparse.ArgumentParser(description="CLI tool for application management")
    parser.add_argument("command", choices=["deploy", "build", "test"], help="Command to execute")
    parser.add_argument("--help", action="store_true", help="Show additional help for the selected command")

    # Parse the arguments
    args = parser.parse_args()

    # Display help for the deploy command
    if args.command == "deploy" and args.help:
        print("Deploy command helps you to deploy your application. Use it to push updates or new builds to your target environment.")
    else:
        print(f"Executing command: {args.command}")

if __name__ == "__main__":
    main()
