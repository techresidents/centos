%define _prefix /opt/3ps

Name:		libvorbis
Version:	1.3.3
Release:	1
Summary:	The Vorbis General Audio Compression Codec.

Group:		tr
Packager:       Tech Residents
License:	BSD
URL:		http://www.xiph.org/
Vendor:		Xiph.org Foundation <team@xiph.org>
Source:		%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

#Epoch is required since Redhat packages use it.
Epoch:          1

Requires:	libogg >= 1.1
BuildRequires:	libogg-devel >= 1.1

%description
Ogg Vorbis is a fully open, non-proprietary, patent-and-royalty-free,
general-purpose compressed audio format for audio and music at fixed 
and variable bitrates from 16 to 128 kbps/channel.

%package devel
Summary: 	Vorbis Library Development
Group: 		Development/Libraries
Requires:	libogg-devel >= 1.1
Requires:	libvorbis = %{epoch}:%{version}-%{release}

%description devel
The libvorbis-devel package contains the header files, static libraries 
and documentation needed to develop applications with libvorbis.

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
%doc AUTHORS COPYING README
%{_libdir}/libvorbis.so.*
%{_libdir}/libvorbisfile.so.*
%{_libdir}/libvorbisenc.so.*

%files devel
%doc doc/*.html
%doc doc/*.png
%doc doc/*.txt
%doc doc/vorbisfile
%doc doc/vorbisenc
%{_datadir}/aclocal/vorbis.m4
%dir %{_includedir}/vorbis
%{_includedir}/vorbis/codec.h
%{_includedir}/vorbis/vorbisfile.h
%{_includedir}/vorbis/vorbisenc.h
%{_libdir}/libvorbis.a
%{_libdir}/libvorbis.la
%{_libdir}/libvorbis.so
%{_libdir}/libvorbisfile.a
%{_libdir}/libvorbisfile.la
%{_libdir}/libvorbisfile.so
%{_libdir}/libvorbisenc.a
%{_libdir}/libvorbisenc.la
%{_libdir}/libvorbisenc.so
%{_libdir}/pkgconfig/vorbis.pc
%{_libdir}/pkgconfig/vorbisfile.pc
%{_libdir}/pkgconfig/vorbisenc.pc
