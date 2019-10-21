packages = {
        'package1' : {'ram' : 2048, 'vcpu' : 1, 'disk' : 10},
        'package2' : {'ram' : 2048, 'vcpu' : 2, 'disk' : 20},
        'package3' : {'ram' : 4096, 'vcpu' : 4, 'disk' : 40}
}

network_PXE = {'name' : 'VLAN80', 'device' : 'br80'}
networks = [
    {'name' : 'VLAN191', 'device' : 'br191'},
    {'name' : 'VLAN70', 'device' : 'br70'},
    {'name' : 'VLAN81', 'device' : 'br81'}
]

cmd_install_centos7 = 'virt-install --name {0} --ram {1} --vcpus={2} ' \
                      '--disk path=/var/lib/libvirt/images/{3}.img,size={4},bus=virtio,format=qcow2 ' \
                      '-l {5} ' \
                      '--network bridge={6} ' \
                      '--network bridge={7} ' \
                      '--console pty,target_type=serial ' \
                      '--hvm --graphics vnc,listen=0.0.0.0 ' \
                      '--noautoconsole ' \
                      '--os-variant rhel7 --virt-type=kvm --os-type Linux ' \
                      '-x \"ks={8}\"'

cmd_install_ubuntu16 = 'virt-install --name {} --ram 2048 --vcpus=2 ' \
                      '--disk path=/var/lib/libvirt/images/minhnv_ser04.img,size=20,bus=virtio,format=qcow2 ' \
                      '-l {} ' \
                      '--network bridge={} ' \
                      '--network bridge={} ' \
                      '--console pty,target_type=serial ' \
                      '--hvm --graphics vnc,listen=0.0.0.0 ' \
                      '--noautoconsole ' \
                      '--os-variant ubuntuxenial --virt-type=kvm --os-type Linux ' \
                      '-x \"ks={}\"'

OSs = {
    'centos7' : {
        'name' : 'CentOS 7',
        'ks_dir' : 'http://192.168.70.107/cblr/svc/op/ks/profile/CentOS7-x86_64_KVM',
        'location' : 'http://192.168.70.107/cblr/links/CentOS7-x86_64/',
        'cmd' : cmd_install_centos7
    },
    'ubuntu16.04' : {
        'name' : 'Ubuntu 16.04',
        'ks_dir' : 'http://192.168.70.107/cblr/svc/op/ks/profile/CentOS7-x86_64_KVM',
        'location' : 'http://192.168.70.107/cblr/links/CentOS7-x86_64/',
        'cmd' : cmd_install_ubuntu16
    }
}



