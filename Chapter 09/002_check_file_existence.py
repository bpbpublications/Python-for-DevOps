# Script: 002_check_file_existence.py

from ansible.module_utils.basic import AnsibleModule

def run_module():
    # Define arguments for the module
    module = AnsibleModule(
        argument_spec=dict(
            path=dict(type='str', required=True)  # File path as a required argument
        ),
        supports_check_mode=True
    )

    # Initialize result dictionary
    result = dict(changed=False)

    try:
        # Check if the file exists
        with open(module.params['path'], 'r'):
            result['message'] = 'File exists'
    except IOError:
        # Handle case when file does not exist
        module.fail_json(msg='File does not exist')

    # Return result if file exists
    module.exit_json(**result)

if __name__ == '__main__':
    run_module()
