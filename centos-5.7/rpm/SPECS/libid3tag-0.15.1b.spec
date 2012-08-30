%define _prefix /opt/3ps

Summary: Library for reading and writing ID3v1 and ID3v2 tags
Name: libid3tag
Version: 0.15.1b
Release: 3%{?dist}
License: GPL
Group: tr
Packager: Tech Residents
URL: http://www.underbit.com/products/mad/
Source: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: zlib-devel, gcc-c++
Conflicts: libmad < 0.15.1b

%description
A library for reading and (eventually) writing ID3 tags, both ID3v1 and the
various versions of ID3v2.

%package devel
Summary: Header and library for developing programs that will use libid3tag
Group: Development/Libraries
Requires: %{name} = %{version}, pkgconfig, zlib-devel

%description devel
A library for reading and (eventually) writing ID3 tags, both ID3v1 and the
various versions of ID3v2.

This package contains the header file as well as the static library needed
to develop programs that will use libid3tag for ID3 tar reading and writing.

%prep
%setup

# Create an additional pkgconfig file
%{__cat} > id3tag.pc << EOF
prefix=%{_prefix}
exec_prefix=%{_prefix}
libdir=%{_libdir}
includedir=%{_includedir}

Name: id3tag
Description: ID3 tag library
Requires:
Version: %{version}
Libs: -L%{_libdir} -lid3tag -lz
Cflags: -I%{_includedir}
EOF

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__install} -Dp -m 644 id3tag.pc %{buildroot}%{_libdir}/pkgconfig/id3tag.pc

%clean
%{__rm} -rf %{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-, root, root, 0755)
%doc CHANGES COPYING COPYRIGHT CREDITS README TODO
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%{_libdir}/*.a
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/*
%exclude %{_libdir}/*.la
