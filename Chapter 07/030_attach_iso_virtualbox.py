# Script: 030_attach_iso_virtualbox.py

import virtualbox

# Initialize VirtualBox and locate the virtual machine
vbox = virtualbox.VirtualBox()
vm_name = 'Your_VM_Name'  # Replace with the name of your VM
iso_path = '/path/to/your/iso/file.iso'  # Replace with the path to your ISO file

try:
    vm = vbox.find_machine(vm_name)

    # Attach the ISO to the CD/DVD drive
    with vm.create_session() as session:
        # Get the storage controller for the CD/DVD drive (e.g., IDE Controller)
        dvd_drive = session.machine.get_storage_controller_by_name('IDE Controller')
        
        # Attach the ISO file
        session.machine.attach_device(
            name='IDE Controller', 
            port=1, 
            device=0, 
            type=virtualbox.library.DeviceType.dvd, 
            medium=vbox.open_medium(iso_path, virtualbox.library.AccessMode.read, virtualbox.library.DeviceType.dvd, {})
        )
        
        # Save the machine settings
        session.machine.save_settings()

    print(f"ISO file {iso_path} attached to VM '{vm_name}' as DVD.")
except Exception as e:
    print(f"An error occurred: {e}")
