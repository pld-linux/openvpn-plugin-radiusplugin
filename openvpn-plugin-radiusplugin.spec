#
%define		subver	beta5
Summary:	OpenVPN Radius Plugin
Name:		openvpn-plugin-radiusplugin
Version:	2.1
Release:	0.%{subver}.1
License:	GPL v2
Group:		Applications
Source0:	http://www.nongnu.org/radiusplugin/radiusplugin_v%{version}_%{subver}.tar.gz
# Source0-md5:	fdc2796a2469dbdce7d7ef128737c921
Patch0:		%{name}-makefile.patch
URL:		http://www.nongnu.org/radiusplugin/index.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libgcrypt-devel
BuildRequires:	libstdc++-devel
BuildRequires:	openvpn-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libdir		%{_prefix}/%{_lib}/openvpn/plugins
%define		_sysconfdir	/etc/openvpn

%description
Plugin for OpenVPN providing Radius authentication and accounting
support.

%prep
%setup -q -n radiusplugin_v%{version}_%{subver}
%patch0 -p0

%build
%{__make} \
	CC="%{__cc}" \
	CXX="%{__cxx}" \
	CFLAGS="%{rpmcflags} -shared -fPIC -DPIC" \
	CXXFLAGS="%{rpmcflags} -shared -fPIC -DPIC" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_libdir}}

cp -a radiusplugin.so $RPM_BUILD_ROOT%{_libdir}
cp -a radiusplugin.cnf $RPM_BUILD_ROOT%{_sysconfdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/radiusplugin.cnf
%attr(755,root,root) %{_libdir}/radiusplugin.so
