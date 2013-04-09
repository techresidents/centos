%define _prefix /opt/3ps

Name:          elasticsearch
Version:       0.20.6
Release:       1
Summary:       A distributed, highly available, RESTful search engine
Packager:      Tech Residents
Group:         tr
License:       Apache 2.0
Source:        elasticsearch-%{version}.tar.gz
Prefix:        %{_prefix}
Buildroot:     %{_tmppath}/%{name}-%{version}-%{release}-root

%description
A distributed, highly available,  RESTful search engine.

%prep
%setup -q

%clean
rm -rf $RPM_BUILD_ROOT

%install
[ "%{buildroot}" != "/" ] && %{__rm} -rf %{buildroot}
%{__mkdir} -p %{buildroot}%{prefix}/app/elasticsearch-%{version}

#bin
%{__mkdir} -p %{buildroot}%{prefix}/app/elasticsearch-%{version}/bin
%{__install} -p -m 755 bin/elasticsearch %{buildroot}%{prefix}/app/elasticsearch-%{version}/bin
%{__install} -p -m 755 bin/elasticsearch.in.sh %{buildroot}%{prefix}/app/elasticsearch-%{version}/bin
%{__install} -p -m 755 bin/plugin %{buildroot}%{prefix}/app/elasticsearch-%{version}/bin

#config
%{__mkdir} -p %{buildroot}%{prefix}/app/elasticsearch-%{version}/config
%{__install} -p -m 644 config/elasticsearch.yml %{buildroot}%{prefix}/app/elasticsearch-%{version}/config
%{__install} -p -m 644 config/logging.yml %{buildroot}%{prefix}/app/elasticsearch-%{version}/config

#lib
%{__mkdir} -p %{buildroot}%{prefix}/app/elasticsearch-%{version}/lib/sigar
%{__install} -p -m 644 lib/*.jar %{buildroot}%{prefix}/app/elasticsearch-%{version}/lib
%ifarch i386
%{__install} -p -m 644 lib/sigar/libsigar-x86-linux.so %{buildroot}%{prefix}/app/elasticsearch-%{version}/lib/sigar
%endif
%ifarch x86_64
%{__install} -p -m 644 lib/sigar/libsigar-amd64-linux.so %{buildroot}%{prefix}/app/elasticsearch-%{version}/lib/sigar
%endif

#data
%{__mkdir} -p %{buildroot}%{prefix}/app/elasticsearch-%{version}/data


#log
%{__mkdir} -p %{buildroot}%{prefix}/app/elasticsearch-%{version}/log

%files
%defattr(-,root,root,-)
%{prefix}/app/elasticsearch-%{version}/bin/*
%{prefix}/app/elasticsearch-%{version}/config/*
%{prefix}/app/elasticsearch-%{version}/lib/*
%{prefix}/app/elasticsearch-%{version}/data
%{prefix}/app/elasticsearch-%{version}/log
