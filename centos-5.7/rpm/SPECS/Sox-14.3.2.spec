%define _prefix /opt/3ps

Summary: General purpose sound file conversion tool
Name: Sox
Version: 14.3.2
Release: 1
License: GPLv2+ and LGPLv2+
Group: tr
Packager: Tech Residents
URL: http://sox.sourceforge.net/

Source: sox-%{version}.tar.gz
Buildroot: %{_tmppath}/%{name}-root

BuildRequires: libid3tag-devel
Requires: libid3tag

BuildRequires: lame-devel
Requires: lame

BuildRequires: libmad-devel
Requires: libmad

%description
SoX (Sound eXchange) is a sound file format converter SoX can convert
between many different digitized sound formats and perform simple
sound manipulation functions, including sound effects.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup -q -n sox-%{version}

%build
export CFLAGS="%{optflags} -I%{_includedir}" 
export LDFLAGS="-L%{_libdir}"
%configure \
    --disable-static \
    --includedir="%{_includedir}/sox"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-, root, root, 0755)
%exclude %{_mandir}/man1/sox.1.gz

%doc AUTHORS ChangeLog COPYING README
%doc %{_mandir}/man1/play.1*
%doc %{_mandir}/man1/rec.1*
%doc %{_mandir}/man1/sox.1*
%doc %{_mandir}/man1/soxi.1*
%doc %{_mandir}/man7/soxeffect.7*
%doc %{_mandir}/man7/soxformat.7*
%{_bindir}/play
%{_bindir}/rec
%{_bindir}/sox
%{_bindir}/soxi
%{_libdir}/libsox.so.*
%dir %{_libdir}/sox/

%files -n Sox-devel
%defattr(-, root, root, 0755)
%doc %{_mandir}/man3/libsox.3*
%{_includedir}/sox/
%{_libdir}/libsox.so
%{_libdir}/pkgconfig/sox.pc
%exclude %{_libdir}/libsox.la
