%define version 2.2.1
%define release 1
%define prefix /opt/3ps/app

Name:           maven2
License:        Apache License v2.0
Summary:        Software project management and comprehension tool
Version:        %{version}
Release:        %{release}
Source0:        apache-maven-%{version}-bin.tar.gz
Group:          tr
Packager:       Tech Residents
BuildRoot:      %{_topdir}/tmp/%{name}-%{version}-buildroot


%description
Apache Maven is a software project management and comprehension tool. Based on the concept of a project object model (POM), Maven can manage a project's build, reporting and documentation from a central piece of information. 

%prep
[ -d $RPM_BUILD_ROOT ] && rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{prefix}
tar -C $RPM_BUILD_ROOT/%{prefix} -xzf %{SOURCE0} 

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{prefix}

%files
%defattr(-,root,root)
%{prefix}/apache-maven-%{version}/*

%clean
rm -rf ${RPM_BUILD_ROOT}
