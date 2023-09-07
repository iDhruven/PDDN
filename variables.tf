variable "region" {
  type = string
  description = "AWS Region (e.g., us-east-1)"
  default = "us-east-1"
}

variable "ami" {
  type = string
  description = "AMI ID for the EC2 instances"
  default = "ami-0123456789abcdef0"
}

variable "instance_type" {
  type = string
  description = "Instance Type (e.g., t2.micro)"
  default = "t2.micro"
}

variable "subnet_id" {
  type = string
  description = "Subnet ID for the EC2 instances"
  default = "subnet-12345678"
}

variable "security_group_ids" {
  type = list(string)
  description = "List of Security Group IDs"
  default = ["sg-12345678"]
}

variable "node_count" {
  type = number
  description = "Number of Kubernetes Worker Nodes"
  default = 2
}
