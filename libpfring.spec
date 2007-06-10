
%define		_cvs_snap	20070610

Summary:	user space library used to manpulate PF_RING
Name:		libpfring
Version:	0.9.4
Release:	0.%{_cvs_snap}.2
License:	BSD
Group:		Libraries
Source0:	%{name}-%{version}-%{_cvs_snap}.tar.bz2
# Source0-md5:	dcbde7036a9ada8f53a42c2a681e5c66
URL:		http://www.ntop.org/PF_RING.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libpfring is a user space library used to manpulate PF_RING

%package devel
Summary:	Header files and develpment documentation for libpfring
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
libpfring is a user space library used to manpulate PF_RING

%package static
Summary:	Static libpfring library
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
libpfring is a user space library used to manpulate PF_RING

This package contains the static library used for development.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}"

%{__cc} -shared -Wl,-soname -Wl,libpfring.so.0.9.4 %{rpmldflags} -o libpfring.so.0.9.4 *.o 

ln -s libpfring.so.0.9.4 libpfring.so

%install
rm -rf $RPM_BUILD_ROOT

install -D libpfring.a		$RPM_BUILD_ROOT%{_libdir}/libpfring.a
install -D libpfring.so.0.9.4	$RPM_BUILD_ROOT%{_libdir}/libpfring.so.0.9.4
install -D libpfring.so		$RPM_BUILD_ROOT%{_libdir}/libpfring.so
install -D pfring.h		$RPM_BUILD_ROOT%{_includedir}/pfring.h
install -D ring.h		$RPM_BUILD_ROOT%{_includedir}/ring.h

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
