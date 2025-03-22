# Script: 028_attach_virtualbox_hard_disk.py

import virtualbox

# Initialize VirtualBox and locate the virtual machine
vbox = virtualbox.VirtualBox()
vm_name = 'Your_VM_Name'  # Replace with the name of your VM
new_disk_path = '/path/to/new/disk.vhd'  # Replace with the desired path for the new disk

try:
    vm = vbox.find_machine(vm_name)

    # Create and attach a new hard disk
    with vm.create_session() as session:
        # Create a new virtual hard disk
        hd = vbox.create_medium('VHD', new_disk_path, virtualbox.library.AccessMode.write, virtualbox.library.MediumVariant.standard)
        hd.create_base_storage(10240 * 1024 * 1024)  # Create a 10 GB disk (size in bytes)
        
        # Attach the new hard disk to the VM
        session.machine.attach_device('SATA Controller', 0, 0, 'HardDisk', hd)
        
        # Save the machine settings
        session.machine.save_settings()

    print(f"New hard disk created and attached to VM '{vm_name}'.")
except Exception as e:
    print(f"An error occurred: {e}")
