# Script: 012_validate_terraform_plan.py

import json
import sys

def validate_plan(plan_file):
    """
    Validate a Terraform plan file based on predefined rules.

    Args:
        plan_file (str): Path to the Terraform plan JSON file.

    Returns:
        bool: True if the plan is valid, False otherwise.
    """
    # Validation criteria
    allowed_instance_types = ['t2.micro', 't2.small']  # Example allowed instance types
    allowed_ip_ranges = ['10.0.0.0/16', '192.168.1.0/24']  # Example allowed IP ranges
    max_resource_count = 10  # Maximum number of resources allowed
    resource_count = 0

    try:
        # Load the plan file
        with open(plan_file) as f:
            plan = json.load(f)
        
        # Extract resource changes from the plan
        resource_changes = plan.get('resource_changes', [])
        for rc in resource_changes:
            resource_count += 1

            # Validate S3 buckets for public-read access
            if rc['type'] == 'aws_s3_bucket' and rc['change']['actions'] != ['delete']:
                if rc['change']['after'].get('acl') == 'public-read':
                    print(f"Validation failed: S3 bucket {rc['name']} has public-read access.", file=sys.stderr)
                    return False

            # Validate EC2 instance types
            if rc['type'] == 'aws_instance' and rc['change']['actions'] != ['delete']:
                instance_type = rc['change']['after'].get('instance_type')
                if instance_type not in allowed_instance_types:
                    print(f"Validation failed: EC2 instance {rc['name']} has invalid instance type '{instance_type}'.", file=sys.stderr)
                    return False

            # Validate security groups for allowed IP ranges
            if rc['type'] == 'aws_security_group' and rc['change']['actions'] != ['delete']:
                ingress_rules = rc['change']['after'].get('ingress', [])
                for rule in ingress_rules:
                    for ip_range in rule.get('cidr_blocks', []):
                        if ip_range not in allowed_ip_ranges:
                            print(f"Validation failed: Security group {rc['name']} has unauthorized IP range '{ip_range}'.", file=sys.stderr)
                            return False

        # Validate resource count
        if resource_count > max_resource_count:
            print(f"Validation failed: Resource count {resource_count} exceeds limit of {max_resource_count}.", file=sys.stderr)
            return False

        return True
    except Exception as e:
        print(f"Error during validation: {e}", file=sys.stderr)
        return False

# Usage: python validate_terraform_plan.py <plan_file>
if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Usage: python validate_terraform_plan.py <plan_file>")
    
    if validate_plan(sys.argv[1]):
        print("Validation passed.")
    else:
        print("Validation failed.", file=sys.stderr)
