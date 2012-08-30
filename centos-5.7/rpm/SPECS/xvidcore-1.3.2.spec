%define _prefix /opt/3ps

%{?fc1:%define _without_selinux 1}
%{?el3:%define _without_selinux 1}
%{?rh9:%define _without_selinux 1}
%{?rh7:%define _without_selinux 1}
%{?el2:%define _without_selinux 1}

Summary: Free reimplementation of the OpenDivX video codec
Name: xvidcore
Version: 1.3.2
Release: 1
License: XviD
Group: tr
Packager: Tech Residents
URL: http://www.xvid.org/
Source: http://downloads.xvid.org/downloads/xvidcore-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-root

#BuildRequires: yasm
BuildRequires: yasm
%{!?_without_selinux:BuildRequires: prelink}
Obsoletes: libxvidcore <= %{version}-%{release}
Provides: libxvidcore = %{version}-%{release}

%description
Free reimplementation of the OpenDivX video codec. You can play OpenDivX
and DivX4 videos with it, as well as encode compatible files.

%package devel
Summary: Static library, headers and documentation of the XviD video codec
Group: Development/Libraries
Requires: %{name} = %{version}

Obsoletes: xvidcore-static <= 1.0.0
Obsoletes: libxvidcore-devel <= %{version}-%{release}
Provides: libxvidcore-devel = %{version}-%{release}

%description devel
Free reimplementation of the OpenDivX video codec. You can play OpenDivX
and DivX4 videos with it, as well as encode compatible files.

This package contains the static library, header files and API documentation
needed to build applications that will use the XviD video codec.

%prep
%setup -n %{name}

%build
cd build/generic/
%configure --disable-static
%{__make} %{?_smp_mflags}
cd -

%install
%{__rm} -rf %{buildroot}
cd build/generic/
%{__make} install DESTDIR="%{buildroot}"
cd -
### Make .so and .so.x symlinks to the so.x.y file, +x to get proper stripping
%{__ln_s} -f libxvidcore.so.4.3 %{buildroot}%{_libdir}/libxvidcore.so.4
%{__ln_s} -f libxvidcore.so.4.3 %{buildroot}%{_libdir}/libxvidcore.so
%{__chmod} +x %{buildroot}%{_libdir}/libxvidcore.so.4.3
### Remove unwanted files from the docs
%{__rm} -f doc/Makefile
### Clear executable stack flag bit (should not be needed)
#execstack -c %{buildroot}%{_libdir}/*.so.*.* || :

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog LICENSE README TODO
%{_libdir}/libxvidcore.so.*

%files devel
%defattr(-, root, root, 0755)
%doc CodingStyle doc/* examples/
%{_includedir}/xvid.h
%{_libdir}/libxvidcore.so
%exclude %{_libdir}/libxvidcore.a
