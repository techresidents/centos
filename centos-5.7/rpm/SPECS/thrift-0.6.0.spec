%define version 0.6.0
%define release 1
%define prefix /opt/3ps
%define _topdir /opt/30and30/centos/centos-5.7/rpm

Name:           thrift
License:        Apache License v2.0
Summary:        RPC and serialization framework
Version:        %{version}
Release:        %{release}
URL:            http://developers.facebook.com/thrift
Source0:        %{name}-%{version}.tar.gz
Group: 30and30
Packager: 30and30
BuildRoot: %{_topdir}/tmp/%{name}-%{version}-buildroot

BuildRequires:  gcc >= 3.4.6
BuildRequires:  gcc-c++


%description
Thrift is a software framework for scalable cross-language services
development. It combines a powerful software stack with a code generation
engine to build services that work efficiently and seamlessly between C++,
Java, C#, Python, Ruby, Perl, PHP, Objective C/Cocoa, Smalltalk, Erlang,
Objective Caml, and Haskell.

%prep
%setup -q

%build
./configure --prefix %{prefix} \
 --without-c_glib \
 --without-csharp \
 --without-java \
 --without-erlang \
 --without-python \
 --without-perl \
 --without-php \
 --without-php_extension \
 --without-ruby \
 --without-haskell            
make 

%install
make install DESTDIR=$RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{prefix}/bin/thrift

%package lib-cpp
Summary: Thrift C++ library
Group:   Libraries

%description lib-cpp
C++ libraries for Thrift.

%files lib-cpp
%defattr(-,root,root)
%{prefix}/lib/libthrift*.so.*


%package lib-cpp-devel
Summary:   Thrift C++ library development files
Group:     Libraries
Requires:  %{name} = %{version}-%{release}
Requires:  boost-devel
%if %{!?without_libevent: 1}
Requires:  libevent-devel >= 1.2
%endif
%if %{!?without_zlib: 1}
Requires:  zlib-devel
%endif

%description lib-cpp-devel
C++ static libraries and headers for Thrift.

%files lib-cpp-devel
%defattr(-,root,root)
%{prefix}/include/thrift/
%{prefix}/lib/libthrift*.*a
%{prefix}/lib/libthrift*.so
%{prefix}/lib/pkgconfig/thrift*.pc

%clean
rm -rf ${RPM_BUILD_ROOT}

