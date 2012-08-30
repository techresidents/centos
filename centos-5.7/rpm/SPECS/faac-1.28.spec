%define _prefix /opt/3ps

Summary: Reference encoder and encoding library for MPEG2/4 AAC
Name: faac
Version: 1.28
Release: 1
License: LGPL
Packager: Tech Residents
Group: tr
URL: http://www.audiocoding.com/

Source: http://dl.sf.net/faac/faac-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-root

#BuildRequires: libmp4v2-devel
BuildRequires: autoconf >= 2.50, automake, libtool, dos2unix, gcc-c++

%description
FAAC is an AAC audio encoder. It currently supports MPEG-4 LTP, MAIN and LOW
COMPLEXITY object types and MAIN and LOW MPEG-2 object types. It also supports
multichannel and gapless encoding.

%package devel
Summary: Development libraries of the FAAC AAC encoder
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
FAAC is an AAC audio encoder. It currently supports MPEG-4 LTP, MAIN and LOW
COMPLEXITY object types and MAIN and LOW MPEG-2 object types. It also supports
multichannel and gapless encoding.

This package contains development files and documentation for libfaac.

%prep
%setup

%build
sh bootstrap
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README TODO docs/*
%{_bindir}/faac
%{_libdir}/libfaac.a
%{_libdir}/libfaac.so.*
%{_mandir}

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/faac.h
%{_includedir}/faaccfg.h
%{_libdir}/libfaac.so
%exclude %{_libdir}/libfaac.la
