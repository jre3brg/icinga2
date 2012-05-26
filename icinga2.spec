Summary: network monitoring application
Name: icinga
Version: 1.3beta6
Release: 2
License: GPL
Group: Productivity/Networking/IRC
Source: https://github.com/gunnarbeutner/strawberry/
URL: http://www.icinga.org/
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

BuildRequires: openssl-devel
BuildRequires: gcc-c++

%description
Icinga 2 is a general-purpose network monitoring application.

%prep
%setup -n %{name}-%{version}

%build
./configure --prefix=/usr
make %{?_smp_mflags} all

%install
make DESTDIR=$RPM_BUILD_ROOT install

%clean
[ "$RPM_BUILD_ROOT" != "/" ] && [ -d $RPM_BUILD_ROOT ] && rm -rf $RPM_BUILD_ROOT;

%define _sharedir %{_prefix}/share
%define _libdir %{_prefix}/lib

%files
%defattr(-,root,root)
%{_bindir}/icinga
%dir %{_libdir}/icinga
%{_libdir}/icinga/discovery.so.0
%{_libdir}/icinga/discovery.la
%{_libdir}/icinga/configrpc.la
%{_libdir}/icinga/demo.la
%{_libdir}/icinga/configfile.so.0
%{_libdir}/icinga/configrpc.so
%{_libdir}/icinga/discovery.so.0.0.0
%{_libdir}/icinga/libbase.so.0
%{_libdir}/icinga/libicinga.so.0.0.0
%{_libdir}/icinga/libjsonrpc.so.0
%{_libdir}/icinga/configrpc.so.0.0.0
%{_libdir}/icinga/libbase.so.0.0.0
%{_libdir}/icinga/libicinga.so.0
%{_libdir}/icinga/libbase.la
%{_libdir}/icinga/configfile.so
%{_libdir}/icinga/discovery.so
%{_libdir}/icinga/libjsonrpc.so
%{_libdir}/icinga/libbase.so
%{_libdir}/icinga/demo.so.0
%{_libdir}/icinga/configfile.la
%{_libdir}/icinga/libjsonrpc.la
%{_libdir}/icinga/demo.so.0.0.0
%{_libdir}/icinga/configrpc.so.0
%{_libdir}/icinga/libicinga.la
%{_libdir}/icinga/libjsonrpc.so.0.0.0
%{_libdir}/icinga/demo.so
%{_libdir}/icinga/configfile.so.0.0.0
%{_libdir}/icinga/libicinga.so
%dir %{_sharedir}/doc
%dir %{_sharedir}/doc/icinga2
%{_sharedir}/doc/icinga2
%{_sharedir}/doc/icinga2/ChangeLog
%{_sharedir}/doc/icinga2/AUTHORS
%{_sharedir}/doc/icinga2/INSTALL
%{_sharedir}/doc/icinga2/NEWS
%{_sharedir}/doc/icinga2/COPYING
%{_sharedir}/doc/icinga2/README
%{_sharedir}/doc/icinga2/COPYING.Exceptions
