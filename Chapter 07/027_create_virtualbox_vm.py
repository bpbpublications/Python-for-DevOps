# Script: 027_create_virtualbox_vm.py

import virtualbox
from virtualbox.library import MachineState

def create_virtual_machine(name, os_type_id, memory_size=1024):
    """
    Creates a VirtualBox virtual machine with the specified parameters.

    Args:
        name (str): Name of the virtual machine.
        os_type_id (str): Operating system type ID (e.g., 'Ubuntu_64').
        memory_size (int, optional): Memory size in MB. Default is 1024 MB.

    Returns:
        virtualbox.library.IMachine: The created virtual machine object.
    """
    try:
        # Initialize VirtualBox API
        vbox = virtualbox.VirtualBox()
        
        # Create a new virtual machine
        vm = vbox.create_machine(settings_file=None, name=name, os_type_id=os_type_id, flags="")
        
        # Set the memory size
        vm.memory_size = memory_size
        
        # Register the machine
        vbox.register_machine(vm)
        
        return vm
    except Exception as e:
        print(f"An error occurred while creating the virtual machine: {e}")
        return None

# Example usage
if __name__ == "__main__":
    vm = create_virtual_machine('MyVM', 'Ubuntu_64', 2048)
    if vm:
        print(f'Created VM: {vm.name}')
