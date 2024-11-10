import subprocess
import sys


def create_user(username, password, full_name=""):
    """
    Creates a new user on a Windows machine using the 'net user' command.

    Args:
    username (str): The username for the new user.
    password (str): The password for the new user.
    full_name (str): The full name of the user (optional).
    """
    try:
        # Create user command
        command = f'net user {username} {password} /add'

        # Optionally, set full name (this is not required but can be added for better user management)
        if full_name:
            command += f' /fullname:"{full_name}"'

        # Run the command to create the user
        subprocess.run(command, check=True, shell=True)

        # Optionally, you can add the user to a specific group (e.g., Administrators)
        # Add user to the Administrators group
        add_to_admin_group = f'net localgroup Administrators {username} /add'
        subprocess.run(add_to_admin_group, check=True, shell=True)

        print(f"User '{username}' created successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error creating user: {e}")
    except Exception as ex:
        print(f"Unexpected error: {ex}")


if __name__ == "__main__":
    # Example usage
    username = input("Enter the username for the new user: ")
    password = input("Enter the password for the new user: ")
    full_name = input("Enter the full name for the new user (optional): ")

    create_user(username, password, full_name)
