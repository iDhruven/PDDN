provider "aws" {
  region = var.region
}

#Kubernetes Master Server
resource "aws_instance" "kubmaster" {
  ami = var.ami
  instance_type = var.instance_type
  subnet_id = var.security_group_ids

  tags = {
    Name = "Kubernetes Master"
  }
}

#Kubernetes Worker Nodes
resource "aws_instance" "kubeworker" {
  count = var.node_count

  ami = var.ami
  instance_type = var.instance_type
  subnet_id = var.subnet_id
  security_groups = var.security_group_ids

  tags = {
    Name = "Kubernetes Worker"
  }

  depends_on = [aws_instance.kubmaster]

}

#Kubernetes Jenkins Server
resource "aws_instance" "jenkins" {
  ami = var.ami
  instance_type = var.instance_type
  subnet_id = var.subnet_id
  security_groups = var.security_group_ids

  tags = {
    Name = "Jenkins Server"
  }
}

#Nginx Server
resource "aws_instance" "nginx" {
  ami = var.ami
  instance_type = var.instance_type
  subnet_id = var.subnet_id
  security_groups = var.security_group_ids

  tags = {
    Name = "Nginx Server"
  }
}