# Script: 001_aws_instance_setup.py

# Define the AWS provider and specify the region to use
provider "aws" {
  region = "us-east-1"
}

# Create an AWS EC2 instance resource
resource "aws_instance" "example" {
  # Specify the Amazon Machine Image (AMI) ID for the instance
  ami           = "ami-0c02fb55956c7d316"
  
  # Specify the instance type (e.g., t2.micro)
  instance_type = "t2.micro"
}
