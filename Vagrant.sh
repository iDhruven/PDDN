# Navigate to the workspace directory
cd $WORKSPACE

# Download the Vagrant installer
curl -O https://releases.hashicorp.com/vagrant/2.3.7/vagrant_2.3.7_linux_amd64.zip

# Unzip the installer
unzip vagrant_2.3.7_linux_amd64.zip

# Make Vagrant executable
chmod +x vagrant

# Optionally, move it to a directory included in the PATH
mv vagrant /Users/idhruven/.jenkins/workspace/PDDN
