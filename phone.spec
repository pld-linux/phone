Summary:	Voice over IP
Summary(pl.UTF-8):	Głos po IP
Name:		phone
Version:	002
Release:	3
License:	GPL
Group:		Applications/Communications
Source0:	http://www.linuxmotors.com/phone/%{name}-%{version}.tgz
# Source0-md5:	5589481785d43f2077bc46f87cd91f2d
URL:		http://www.linuxmotors.com/phone/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Voice over IP - an internet phone for Linux. With Linux, a full duplex
sound board, speakers and a microphone, and a 24000 bits-per-second
connection to the internet or better, you can talk with other people
with the same setup over the internet.

%description -l pl.UTF-8
Głos po IP - internetowy telefon dla Linuksa. Mając Linuksa, kartę
dźwiękową full-duplex, głośniki i mikrofon oraz połączenie z
Internetem co najmniej 24000 bitów/sekundę, możesz rozmawiać z ludźmi
używając tego samego łącza.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install phone $RPM_BUILD_ROOT%{_bindir}


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changelog README
%attr(755,root,root) %{_bindir}/*
