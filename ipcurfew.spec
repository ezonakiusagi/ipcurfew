#
# RPM spec file for ipcurfew
# Copyright (C) 2016 Bond Masuda. All rights reserved.
#

Name:           ipcurfew
Version:        0.1
Release:        1%{?dist}
Summary:        IP curfew enforces restrictions on services based on public IP
License:        GPLv3
Group:          System/Management
Source0:        %{name}-%{version}.tar.gz
Requires:       ksh >= 20120801
Requires:       bash
Requires:       coreutils
Requires:       findutils
Requires:       curl
Requires:       gawk
Requires:       sed
Requires:       grep
Requires:       util-linux
BuildArch:      noarch

%description
IP curfew enforces restrictions on system services based on the system's 
public internet IP address. This can ensure that certain types of network
services are or are not running when the system is connected to certain
networks.

%prep
%setup -q

%build

%install
%{__mkdir} -p ${RPM_BUILD_ROOT}/etc/%{name}/rules.d
%{__mkdir} -p ${RPM_BUILD_ROOT}/etc/sysconfig/%{name}
%{__mkdir} -p ${RPM_BUILD_ROOT}/usr/sbin
%{__mkdir} -p ${RPM_BUILD_ROOT}/lib/systemd/system
%{__mkdir} -p ${RPM_BUILD_ROOT}/var/cache/%{name}/ipinfo
%{__install} -m 755 %{name} ${RPM_BUILD_ROOT}/usr/sbin/%{name}
%{__install} -m 755 lib/systemd/system/%{name}.service ${RPM_BUILD_ROOT}/lib/systemd/system/%{name}.service
%{__install} -m 755 rules/transmission.rule ${RPM_BUILD_ROOT}/etc/ipcurfew/rule.d/transmission.rule
%{__install} -m 755 etc/sysconfig/%{name} ${RPM_BUILD_ROOT}/etc/sysconfig/%{name}

%post
# reload systemd so it knows about the new service
systemctl daemon-reload

%files
%defattr(-,root,root,-)
%doc README LICENSE
%attr(755,root,root) %dir /var/cache/%{name}/ipinfo
%attr(755,root,root) %dir /etc/%{name}/rules.d
%attr(644,root,root) /etc/%{name}/rules.d/*
%attr(644,root,root) /etc/sysconfig/%{name}
%attr(755,root,root) %{_sbindir}/%{name}
%attr(644,root,root) /lib/systemd/system/%{name}.service

%changelog
* Wed Aug 31 2016 Bond Masuda <bond.masuda@jlbond.com> - 0.1-1
- 1st packaging

