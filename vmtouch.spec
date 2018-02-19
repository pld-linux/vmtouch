Summary:	Portable file system cache diagnostics and control
Name:		vmtouch
Version:	1.3.0
Release:	1
License:	BSD
Group:		Applications
Source0:	https://github.com/hoytech/vmtouch/archive/v%{version}.tar.gz
# Source0-md5:	deaa76af2cadfde293547f1940208b0f
Patch0:		%{name}-destdir.patch
URL:		https://hoytech.com/vmtouch/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
vmtouch is a tool for learning about and controlling the file system
cache of unix and unix-like systems.

%prep
%setup -q
%patch0 -p1

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
