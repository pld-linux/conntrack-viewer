# Conditional build:
%bcond_without	dist_kernel	# without distribution kernel
#
Summary:	Conntrack Viewer - view the masquerading connection with iptables
Summary(pl.UTF-8):	Conntrack Viewer - podgląd połączeń maskowanych przez iptables
Name:		conntrack-viewer
Version:	1.3
Release:	1
License:	GPL v2
Group:		Networking/Utilities
Source0:	http://cv.intellos.net/%{name}-%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	21d12842f8f1eb57dec8848fc853e252
URL:		http://cv.intellos.net/
BuildRequires:	rpm-perlprov
%{?with_dist_kernel:Requires:	kernel >= 2.4 }
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Conntrack Viewer is a perl script to view the masquerading connections
with iptables, it uses /proc/net/ip_conntrack.

%description -l pl.UTF-8
Conntrack Viewer jest skryptem perlowym do oglądania połączeń
maskowanych za pomocą iptables, używa /proc/net/ip_conntrack.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install %{name}.pl		$RPM_BUILD_ROOT%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
