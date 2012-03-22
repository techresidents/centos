%define name nodejs
%define version 0.6.8
%define release 1
%define prefix /opt/3ps

Summary: Event-driven I/O server-side JavaScript environment based on V8.
Name: %{name}
Release: %{release}
Version: %{version}
Source: node-v%{version}.tar.gz

BuildRoot: %{_topdir}/tmp/%{name}-%{version}-buildroot
Group: 30and30
Packager: 30and30
License: nodejs

%description 
Event-driven I/O server-side JavaScript environment based on V8.

%prep
%setup -q -n node-v%{version}

%build
./configure --prefix %{prefix}
make

%install
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%{prefix}/bin/*
%{prefix}/include/*
%{prefix}/lib/*
%{prefix}/share/*
