%define _prefix /opt/3ps

%define name     speex
%define ver      1.2rc1
%define rel      1

Summary: An open-source, patent-free speech codec
Name: %name
Version: %ver
Release: %rel
License: BSD
Group: tr
Source: http://www.speex.org/download/%{name}-%{ver}.tar.gz
URL: http://www.speex.org/
Vendor: Speex
Packager: Tech Residents
BuildRoot: %{_tmppath}/%{name}-root

%description
Speex is a patent-free audio codec designed especially for voice (unlike 
Vorbis which targets general audio) signals and providing good narrowband 
and wideband quality. This project aims to be complementary to the Vorbis
codec.

%package devel
Summary:	Speex development files
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Speex development files.

%prep
%setup

%build
export CFLAGS='-O3'
%configure --enable-shared --enable-static --with-ogg="%{_prefix}" --with-ogg-libraries="%{_libdir}"
make

%install
%{__rm} -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install
%{__rm} -rf %{buildroot}%{_prefix}/share

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%exclude %{_mandir}/man1/speexdec.1.gz
%exclude %{_mandir}/man1/speexenc.1.gz
%doc COPYING AUTHORS ChangeLog NEWS README
%doc doc/manual.pdf
%doc %{_mandir}/man1
%attr(755,root,root) %{_bindir}/speex*
%attr(755,root,root) %{_libdir}/libspeex*.so*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libspeex*.la
%{_includedir}/speex/speex*.h
%{_libdir}/pkgconfig/speex.pc
%{_libdir}/pkgconfig/speexdsp.pc
%{_libdir}/libspeex*.a
