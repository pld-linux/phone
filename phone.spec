Summary:	Voice over IP
Name:		phone
Version:	002
Release:	1
Group:		Applications/Communications
Group(pl):	Aplikacje/Komunikacja
License:	GPL
Source0:	%{name}-%{version}.tgz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Voice over IP

%prep
%setup  -q

%build
%{__make} CFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT

gzip -9nf README 

install -d		$RPM_BUILD_ROOT%{_bindir}
install phone	 	$RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz
%attr(755,root,root) %{_bindir}/*
