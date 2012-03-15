%define _topdir /opt/30and30/centos/centos-5.7/rpm
%define _prefix /opt/3ps

Name:          mongrel2
Version:       1.7.5
Release:       1
Summary:       Mongrel2
Packager:      30and30
Group:         30and30
License:       Mongrel2
Source:        mongrel2-%{version}.tar.bz2
Prefix:        %{_prefix}
Buildroot:     %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: sqlite-devel zeromq-devel

%description
Mongrel2

%prep
%setup -q

%build
OPTFLAGS=-I/opt/3ps/include OPTLIBS=-L/opt/3ps/lib64 make all

%install
PREFIX=$RPM_BUILD_ROOT%{_prefix} make install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_prefix}/bin/m2sh
%{_prefix}/bin/mongrel2
%exclude %{_prefix}/lib/mongrel2/config_modules/null.so
%exclude %{_prefix}/lib/mongrel2/config_modules/zmq.so
%exclude %{_prefix}/lib/mongrel2/filters/null.so

