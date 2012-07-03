#!/bin/bash

POSTINSTALL_DIR="/root/postinstall"

#Sync time and date
/sbin/chkconfig ntpd on
/sbin/ntpdate pool.ntp.org
/sbin/service ntpd start

#Install Tech Residents repo
cp $POSTINSTALL_DIR/repos/*.repo /etc/yum.repos.d

#Check updates and update installed packages 
yum clean all
#yum -y check-update
#yum -y update

#Install python 2.7 since sysutils needs it and it's required for cfengine promises
yum --disablerepo=* --enablerepo=tr -y install python27 python27-devel

#Install cfengine and let it do the rest.
yum --disablerepo=* --enablerepo=tr -y install cfengine-community
