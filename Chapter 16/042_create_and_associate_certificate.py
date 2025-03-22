# Script: 042_create_and_associate_certificate.py

import boto3

def create_certificate(domain_name):
    acm_client = boto3.client('acm')
    try:
        response = acm_client.request_certificate(
            DomainName=domain_name,
            ValidationMethod='DNS'
        )
        print(f"Certificate request for {domain_name} created. ARN: {response['CertificateArn']}")
        return response['CertificateArn']
    except Exception as e:
        print(f"Error creating certificate: {e}")
        return None

def associate_certificate(certificate_arn, load_balancer_arn, listener_port=443):
    elb_client = boto3.client('elbv2')
    try:
        response = elb_client.modify_listener(
            ListenerArn=load_balancer_arn,
            Port=listener_port,
            Protocol='HTTPS',
            Certificates=[{'CertificateArn': certificate_arn}]
        )
        print(f"Certificate associated with listener on port {listener_port}.")
    except Exception as e:
        print(f"Error associating certificate: {e}")

if __name__ == "__main__":
    domain = "example.com"
    cert_arn = create_certificate(domain)
    if cert_arn:
        associate_certificate(cert_arn, "your-load-balancer-arn")
