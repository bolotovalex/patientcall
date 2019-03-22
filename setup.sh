#!/bin/bash
clear

#Check root
if [ "$(id -u)" != "0" ]; then
   echo "Need root privelegies"
   exit 1
fi

#Check $1 and $2
if [[ -z "$2" ]] && [[ -z "$2" ]]; then
	echo "Use ./setup.sh [new_password] [name_pc]"
	echo
	exit 1
fi

#Check $1 Name PC
if [[ -z "$2" ]]; then
	echo "Not enter name"
	echo
	exit 1
fi

#Check $2 new password for pi user
if [[ -z "$1" ]]; then
	echo "No enter new password"
	echo
	exit 1
fi


#Read network par
read -p "Setup Network Y/N: " ch_network
if [[ "$ch_network" == "Y" ]] || [[ "$ch_network" == "y" ]] || [[ "$ch_network" == "N" ]] || [[ "$ch_network" == "n" ]]; then
	if [[ "$ch_network" == "Y" ]] || [[ "$ch_network" == "y" ]]; then
		echo "Setup Static"
		read -p "Enter IP address: " ip
		read -p "Enter netmask: " netmask
		read -p "Enter gateway: " gateway
		echo
		echo "Check you config:"
		echo "IP ADDRESS: $ip"
		echo "NETMASK   : $netmask"
		echo "GATEWAY   : $gateway"
		echo
		read -p "Correct Y/N:" ch2
	fi
fi

read -p "Reboot after install?: " reboot_now

echo
#Enable ssh
systemctl enable ssh

#Set Timezone Asia/Yekaterinburg
timedatectl set-timezone Asia/Yekaterinburg

#Disable overscan and enable hotplug hdmi
sed -i 's/quiet splash plymouth.ignore-serial-consoles//' /boot/cmdline.txt
sed -i 's/.#disable_overscan=1/disable_overscan=1/' /boot/config.txt
sed -i 's/#hdmi_force_hotplug=1/hdmi_force_hotplug=1/' /boot/config.txt
sed -i 's/#arm_freq=800/arm_freq=/' /boot/config.txt
echo "gpu_mem=128" >> /boot/config.txt
#Set keyboard type
echo '
# KEYBOARD CONFIGURATION FILE
# Consult the keyboard(5) manual page.
XKBMODEL=pc101
XKBLAYOUT="us,ru"
XKBVARIANT=""
XKBOPTIONS="grp:alt_shift_toggle"
BACKSPACE="guess"' > /etc/default/keyboard

#set password
echo "Set password user - pi:$1"
echo pi:$1 | chpasswd

#Enable VNC
systemctl enable vncserver-x11-serviced

#Locale gen
sed -i 's/^# *\(ru_RU.UTF-8\)/\1/' /etc/locale.gen && locale-gen

#Change hostname
echo "Hostame: $2"
echo "$2" > /etc/hostname
echo "127.0.0.1       localhost
::1             localhost ip6-localhost ip6-loopback
ff02::1         ip6-allnodes
ff02::2         ip6-allrouters
127.0.1.1       $2" > /etc/hosts

#Create autostart file
test -f /home/pi/.config/lxsession/LXDE-pi/autostart
if [ $(echo $?) -eq "1" ]; then
  mkdir -p /home/pi/.config/lxsession/LXDE-pi/
  touch /home/pi/.config/lxsession/LXDE-pi/autostart
  chown pi:pi -R /home/pi/.config/lxsession/
  chmod 744 -R /home/pi/.config/lxsession/
fi
echo "@lxpanel --profile LXDE-pi
@pcmanfm --desktop --profile LXDE-pi
@xscreensaver -no-splash
@point-rpi
@xset s off
@xset -dpms
@xset s noblank
@unclutter -idle 5
@python3 /home/pi/patientcall/$2" > /home/pi/.config/lxsession/LXDE-pi/autostart
chown pi:pi /home/pi/.config/lxsession/LXDE-pi/autostart
chmod 744 /home/pi/.config/lxsession/LXDE-pi/autostart

#Install unclutter and xterm
dpkg -i *.deb

#Copy setupid file and create Desktop shortcut

#Setup Network
if [ "$ch2" == Y ] || [ "$ch2" == y ]; then
	echo "auto lo" > /etc/network/interfaces
  echo "iface lo inet loopback" >> /etc/network/interfaces
  echo "#ETH0" >> /etc/network/interfaces
  echo "auto eth0" >> /etc/network/interfaces
  echo "iface eth0 inet static" >> /etc/network/interfaces
  echo "address $ip" >> /etc/network/interfaces
  echo "netmask $netmask" >> /etc/network/interfaces
  echo "gateway $gateway" >> /etc/network/interfaces
  echo "dns-nameservers 77.88.8.8" >> /etc/network/interfaces
fi
if [[ "$ch_network" == "N" ]] || [[ "$ch_network" == "n" ]]; then
  echo "auto lo" > /etc/network/interfaces
  echo "iface lo inet loopback" >> /etc/network/interfaces
  echo "auto eth0" >> /etc/network/interfaces
  echo "iface eth0 inet dhcp" >> /etc/network/interfaces
  echo "dns-nameservers 10.41.129.130" >> /etc/network/interfaces
fi

#Reboot

if [[ "$reboot_now" == "Y" ]] || [[ "$reboot_now" == "y" ]]; then
	reboot
else
	rm -rf /home/pi/rmis
fi
