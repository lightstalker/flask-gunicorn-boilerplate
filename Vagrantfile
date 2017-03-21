# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
  config.vm.box = "ubuntu/precise32"
  config.vm.network :private_network, ip: "192.168.33.10"

  config.vm.synced_folder "serverRoot", "/opt/dss/serverRoot"
  config.vm.synced_folder "log", "/var/log/dss/server", create: true

  config.vm.provider "virtualbox" do |vb|
    vb.memory = "1024"
  end

  config.vm.provision :ansible_local do |ansible|
    ansible.install = true
    ansible.install_mode = :pip
    ansible.playbook = "ansible/playbook.yml"
  end
end
