%define _prefix /opt/3ps

Name:		libogg
Version:	1.3.0
Release:	1
Summary:	Ogg Bitstream Library.

Group:		tr
Packager:	Tech Residents
License:	BSD
URL:		http://www.xiph.org/
Vendor:		Xiph.org Foundation <team@xiph.org>
Source:		%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-root

#Epoch is required since Redhat package uses it.
Epoch: 2

%description
Libogg is a library for manipulating ogg bitstreams.  It handles
both making ogg bitstreams and getting packets from ogg bitstreams.

%package devel
Summary: 	Ogg Bitstream Library Development
Group: 		Development/Libraries
Requires: 	libogg = %{epoch}:%{version}-%{release}

%description devel
The libogg-devel package contains the header files, static libraries
and documentation needed to develop applications with libogg.

%prep
%setup -q -n %{name}-%{version}

%build
CFLAGS="$RPM_OPT_FLAGS" %configure --enable-static
make

%install
rm -rf $RPM_BUILD_ROOT

make DESTDIR=$RPM_BUILD_ROOT install
rm -rf %{buildroot}%{_prefix}/share/doc

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc AUTHORS CHANGES COPYING README
%{_libdir}/libogg.so.*

%files devel
%defattr(-,root,root)
%doc doc/index.html
%doc doc/framing.html
%doc doc/oggstream.html
%doc doc/white-ogg.png
%doc doc/white-xifish.png
%doc doc/stream.png
%doc doc/libogg/*.html
%doc doc/libogg/style.css
%dir %{_includedir}/ogg
%{_includedir}/ogg/ogg.h
%{_includedir}/ogg/os_types.h
%{_includedir}/ogg/config_types.h
%{_libdir}/libogg.a
%{_libdir}/libogg.la
%{_libdir}/libogg.so
%{_libdir}/pkgconfig/ogg.pc
%{_datadir}/aclocal/ogg.m4
