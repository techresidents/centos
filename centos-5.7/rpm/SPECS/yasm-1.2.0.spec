%define _prefix /opt/3ps

Summary: Complete rewrite of the NASM assembler
Name: yasm
Version: 1.2.0
Release: 0
License: BSD and (Artistic or GPLv2+ or LGPLv2+) and LGPLv2
Packager: Tech Residents
Group: tr
URL: http://www.tortall.net/projects/yasm/
Source: yasm-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: bison
BuildRequires: byacc
#BuildRequires: xmlto
#BuildRequires: gettext-devel

%description
Yasm is a complete rewrite of the NASM assembler under the "new" BSD License
(some portions are under other licenses, see COPYING for details). It is
designed from the ground up to allow for multiple assembler syntaxes to be
supported (eg, NASM, TASM, GAS, etc.) in addition to multiple output object
formats and even multiple instruction sets. Another primary module of the
overall design is an optimizer module.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup -q -n yasm-%{version}

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Artistic.txt AUTHORS BSD.txt COPYING GNU*
%doc %{_mandir}/man1/yasm.1*
%{_bindir}/vsyasm
%{_bindir}/yasm
%{_bindir}/ytasm

%files devel
%defattr(-, root, root, 0755)
%doc %{_mandir}/man7/yasm_*.7*
%{_includedir}/libyasm/
%{_includedir}/libyasm.h
%{_includedir}/libyasm-stdint.h
%{_libdir}/libyasm.a
