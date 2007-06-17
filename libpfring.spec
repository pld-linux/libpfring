
%define		cvs_snap	20070610

Summary:	User space library used to manipulate PF_RING
Summary(pl.UTF-8):	Biblioteka przestrzeni użytkownika do obsługi PF_RING
Name:		libpfring
Version:	0.9.4
Release:	0.%{cvs_snap}.2
License:	BSD
Group:		Libraries
Source0:	%{name}-%{version}-%{cvs_snap}.tar.bz2
# Source0-md5:	dcbde7036a9ada8f53a42c2a681e5c66
URL:		http://www.ntop.org/PF_RING.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libpfring is a user space library used to manipulate PF_RING.

%description -l pl.UTF-8
libpfring to biblioteka przestrzeni użytkownika służąca do obsługi
PF_RING.

%package devel
Summary:	Header files for libpfring
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libpfring
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libpfring.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libpfring.

%package static
Summary:	Static libpfring library
Summary(pl.UTF-8):	Statyczna biblioteka libpfring
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libpfring library.

%description static -l pl.UTF-8
Statyczna biblioteka libpfring.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc} %{rpmcflags} -fPIC -Wall"

%{__cc} -shared -Wl,-soname -Wl,libpfring.so.0.9.4 %{rpmldflags} -o libpfring.so.0.9.4 *.o 

%{__make} clean
%{__make} \
	CC="%{__cc} %{rpmcflags} -Wall"

%install
rm -rf $RPM_BUILD_ROOT

install -D libpfring.a		$RPM_BUILD_ROOT%{_libdir}/libpfring.a
install -D libpfring.so.0.9.4	$RPM_BUILD_ROOT%{_libdir}/libpfring.so.0.9.4
ln -sf libpfring.so.0.9.4	$RPM_BUILD_ROOT%{_libdir}/libpfring.so
install -D pfring.h		$RPM_BUILD_ROOT%{_includedir}/pfring.h
install -D ring.h		$RPM_BUILD_ROOT%{_includedir}/ring.h

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpfring.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpfring.so
%{_includedir}/*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libpfring.a
