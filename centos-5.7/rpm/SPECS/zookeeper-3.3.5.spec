%define version 3.3.5
%define release 1
%define prefix /opt/3ps
%{!?python_sitearch: %define python_sitearch %(/bin/env python -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}

Name:           zookeeper
License:        Apache License v2.0
Summary:        Highly Reliable Distributed Coordination
Version:        %{version}
Release:        %{release}
URL:            http://zookeeper.apache.org
Source0:        %{name}-%{version}.tar.gz
Group: tr
Packager: Tech Residents
BuildRoot: %{_topdir}/tmp/%{name}-%{version}-buildroot

%description
ZooKeeper is a centralized service for maintaining configuration information, naming, providing distributed synchronization,
and providing group services. All of these kinds of services are used in some form or another by distributed applications.
Each time they are implemented there is a lot of work that goes into fixing the bugs and race conditions that are inevitable.
Because of the difficulty of implementing these kinds of services, applications initially usually skimp on them ,
which make them brittle in the presence of change and difficult to manage. Even when done correctly, different implementations
of these services lead to management complexity when the applications are deployed.

%prep
%setup -q

%build
pushd src/c
./configure --prefix %{prefix}
make
popd

%install
[ "%{buildroot}" != "/" ] && %{__rm} -rf %{buildroot}

mkdir -p %{buildroot}%{prefix}/app/zookeeper-%{version}
install -p -D -m 644 zookeeper-%{version}.jar  %{buildroot}%{prefix}/app/zookeeper-%{version}/zookeeper-%{version}.jar
cp -ar conf %{buildroot}%{prefix}/app/zookeeper-%{version}
cp -ar lib %{buildroot}%{prefix}/app/zookeeper-%{version}
cp -ar bin %{buildroot}%{prefix}/app/zookeeper-%{version}
cp -ar docs %{buildroot}%{prefix}/app/zookeeper-%{version}

#C libs
make install DESTDIR=$RPM_BUILD_ROOT -C src/c

# Kludge for ugly default path
mv %{buildroot}%{prefix}/include/c-client-src %{buildroot}%{prefix}/include/zookeeper

#Python libs 
cd src/contrib/zkpython
python src/python/setup.py install --install-lib %{buildroot}%{python_sitearch}

%files
%defattr(-,root,root)
%{prefix}/app/zookeeper-%{version}
%{prefix}/lib/libzookeeper_mt.so.*
%{prefix}/lib/libzookeeper_st.so.*
%exclude %{prefix}/bin/*
%exclude /usr/*

%package devel
Summary: C headers and static libraries for zookeeper.
Group: tr
Requires: gcc

%description devel
C headers and static libraries for zookeeper.

%files devel
%defattr(-,root,root)
%{prefix}/include/*
%{prefix}/lib/*.a
%{prefix}/lib/*.la
%{prefix}/lib/*.so

%package python-devel
Summary: Python development libraries for zookeeper.
Group: tr
Requires: python, zookeeper

%description python-devel
Python development libraries for zookeeper.

%files python-devel
%defattr(-,root,root)
%{python_sitearch}

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%clean
[ "%{buildroot}" != "/" ] && %{__rm} -rf %{buildroot}
