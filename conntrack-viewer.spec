%include	/usr/lib/rpm/macros.perl
Summary:	Conntrack Viewer - view the masquerading connection with iptables
Summary(pl):	Conntrack Viewer - podgl�d po��cze� maskowanych przez iptables
Name:		conntrack-viewer
Version:	1.1
Release:	1
License:	GPL v2
Group:		Networking/Utilities
Source0:	http://cv.intellos.net/%{name}-%{version}/%{name}-%{version}.tar.gz
URL:		http://cv.intellos.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Conntrack Viewer is a perl script to view the masquerading connections
with iptables, it uses /proc/net/ip_conntrack.

%description -l pl
Conntrack Viewer jest skryptem perlowym do ogl�dania po��cze�
maskowanych za pomoc� iptables, u�ywa /proc/net/ip_conntrack.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install %{name}.pl	$RPM_BUILD_ROOT%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*