Name: ipw2100-firmware
Version: 1.3
Release: 6
Summary: Intel PRO/Wireless 2100 firmware
Source: ipw2100-fw-%{version}.tgz
License: Proprietary
Group: System/Kernel and hardware
URL: http://ipw2100.sourceforge.net
BuildRoot: %{_tmppath}/%{name}-%{version}
BuildArch: noarch

%description
Firmware for Intel PRO/Wireless 2100 (IPW2100) mini PCI adapter support.

%prep
%setup -qc

%build

%install
rm -rf %{buildroot}
install -d %{buildroot}/lib/firmware
install -m644 *.fw %{buildroot}/lib/firmware/

%clean
rm -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%doc LICENSE
/lib/firmware/*.fw

