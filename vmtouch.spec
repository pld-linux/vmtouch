Summary:	Portable file system cache diagnostics and control
Name:		vmtouch
Version:	1.3.1
Release:	1
License:	BSD
Group:		Applications
Source0:	https://github.com/hoytech/vmtouch/archive/v%{version}.tar.gz
# Source0-md5:	46c153c48ab035d37d16e8bc1587e8d8
URL:		https://hoytech.com/vmtouch/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
vmtouch is a tool for learning about and controlling the file system
cache of unix and unix-like systems.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	PREFIX="%{_prefix}" \
	BINDIR="%{_bindir}" \
	MANDIR="%{_mandir}/man8" \
	DESTDIR="$RPM_BUILD_ROOT"

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README.md TODO TUNING.md
%attr(755,root,root) %{_bindir}/vmtouch
%{_mandir}/man8/vmtouch.8*
