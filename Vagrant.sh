# Navigate to the workspace directory
cd $WORKSPACE

# Download the Vagrant installer
curl -O https://releases.hashicorp.com/vagrant/X.Y.Z/vagrant_X.Y.Z_linux_amd64.zip

# Unzip the installer
unzip vagrant_X.Y.Z_linux_amd64.zip

# Make Vagrant executable
chmod +x vagrant

# Optionally, move it to a directory included in the PATH
mv vagrant /usr/local/bin/
