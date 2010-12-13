%define python_sitelib /usr/lib/python2.4/site-packages/

Summary: Abiquo SOSReport plugins
Name: abiquo-sosreport-plugins
Version: 1.0
Release: 2
License: BSD 
Group: System Environment/Base
URL: http://packages.abiquolabs.com/
Packager: Sergio Rubio <srubio@abiquo.com>
Vendor: Abiquo Repository, http://www.abiquo.com
Requires: sos 

Source0: abiquo_kvm_node.py
Source1: abiquo_xen_node.py
Source2: abiquo_server.py
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
This package contains Abiquo sosreport plugins.

%install
%{__rm} -rf %{buildroot}
mkdir -p %{buildroot}%{python_sitelib}/sos/plugins
%{__cp} %{_sourcedir}/abiquo_kvm_node.py %{buildroot}/%{python_sitelib}/sos/plugins/
%{__cp} %{_sourcedir}/abiquo_xen_node.py %{buildroot}/%{python_sitelib}/sos/plugins/
%{__cp} %{_sourcedir}/abiquo_server.py %{buildroot}/%{python_sitelib}/sos/plugins/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%{python_sitelib}/sos/plugins/*

%changelog
* Mon Sep 27 2010 Sergio Rubio <srubio@abiquo.com> - 1.0-2
- Updated scripts

* Fri Jun 04 2010 Sergio Rubio <srubio@abiquo.com> - 1.0-1
- Initial Release
