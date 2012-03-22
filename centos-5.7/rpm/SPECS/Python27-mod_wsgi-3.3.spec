Summary: Python27-mod_wsgi-3.3
Name: Python27-mod_wsgi
Release: 1
Version: 3.3

#Renaming mod_wsgi to Python27-mod_wsgi to prevent conflicts
#from other yum repos. This also make it clear which version
#of python mod_wsgi is built against.
#Source: http://modwsgi.googlecode.com/files/mod_wsgi-3.3.tar.gz
Source: Python27-mod_wsgi-3.3.tar.gz

BuildRoot: %{_topdir}/tmp/%{name}-%{version}-buildroot
Group: 30and30
Packager: 30and30
License: Apache License 2.0
AutoReqProv: no

%description 
mod_wsgi-3.3

%prep
%setup -q

%build
./configure --with-python=/opt/3ps/bin/python
make

%install
make install DESTDIR=$RPM_BUILD_ROOT

%files
%defattr(-, root, root)
/usr/lib64/*
