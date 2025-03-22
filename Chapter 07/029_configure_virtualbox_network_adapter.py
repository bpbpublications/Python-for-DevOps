# Script: 029_configure_virtualbox_network_adapter.py

import virtualbox

# Initialize VirtualBox and locate the virtual machine
vbox = virtualbox.VirtualBox()
vm_name = 'Your_VM_Name'  # Replace with the name of your VM

try:
    vm = vbox.find_machine(vm_name)

    # Configure the network adapter
    with vm.create_session() as session:
        # Get the first network adapter
        adapter = session.machine.get_network_adapter(0)
        
        # Set the attachment type to NAT and enable the adapter
        adapter.attachment_type = virtualbox.library.NetworkAttachmentType.nat
        adapter.enabled = True
        
        # Save the machine settings
        session.machine.save_settings()

    print(f"Network adapter for VM '{vm_name}' configured to NAT and enabled.")
except Exception as e:
    print(f"An error occurred: {e}")
