%define name psycopg2
%define version 2.4.4
%define unmangled_version 2.4.4
%define release 1

Summary: Python-PostgreSQL Database Adapter
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{unmangled_version}.tar.gz
License: GPL with exceptions or ZPL
Group: 30and30
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Vendor: Federico Di Gregorio <fog@initd.org>
Packager: 30and30
Url: http://initd.org/psycopg/

%description
psycopg2 is a PostgreSQL database adapter for the Python programming
language.  psycopg2 was written with the aim of being very small and fast,
and stable as a rock.

psycopg2 is different from the other database adapter because it was
designed for heavily multi-threaded applications that create and destroy
lots of cursors and make a conspicuous number of concurrent INSERTs or
UPDATEs. psycopg2 also provide full asycronous operations and support
for coroutine libraries.


%prep
%setup -n %{name}-%{unmangled_version}

%build
env CFLAGS="$RPM_OPT_FLAGS" python setup.py build

%install
python setup.py install -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)
