Summary:	Twin - a windowing environment
Name:		twin
Version:	0.3.8
Release:	1
License:	LGPL
Group:		Libraries
Group(de):	Libraries
Group(pl):	Biblioteki
Source0:	http://download.sourceforge.net/twin/%{name}-%{version}.tar.gz
Patch0:		%{name}-ncurses.patch
Patch1:		%{name}-makeinstall.patch
BuildRequires:	XFree86-devel
BuildRequires:	gpm-devel
BuildRequires:	libggi-devel
BuildRequires:	libgii-devel
BuildRequires:	ncurses-devel
BuildRequires:	zlib-devel
URL:		http://twin.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Twin is a windowing environment with mouse support, window manager,
terminal emulator and networked clients, all inside a text display.

It supports a variety of displays:
- plain text terminals (any termcap/ncurses compatible terminal,
  Linux console, twin's own terminal emulator);
- X11, where it can be used as a multi-window xterm;
- itself (you can display a twin on another twin);
- twdisplay, a general network-transparent display client, used
  to attach/detach more displays on-the-fly.

%package devel
Summary:	Header files and etc for develop twin applications
Summary(pl):	Pliki nag³ówkowe dla twin
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
Header files and etc for develop twin applications.

%description -l pl devel
Pliki nag³ówkowe i inne potrzebne do tworzenia programów opartych o
twin.

%package static
Summary:	Static twin libraries
Summary(pl):	Biblioteki statyczne twin
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
Static twin libraries.

%description -l pl static
Biblioteki statyczne twin.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

perl -pi -e "s/prefix = \/usr\/local/prefix = \%{_prefix}/" MakePaths

%build
%{__make} config <<EOF
y
y
n
m
y
y
m
m
n
y
m
y
n
m
y
y
y
y
m
m
m
m
y
n
n
n
y
y
n
EOF
%{__make} OPT_FLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
%{__install} -d $RPM_BUILD_ROOT%{_mandir}/man1

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%{__install} docs/twin.1 $RPM_BUILD_ROOT%{_mandir}/man1

gzip -9nf BUGS Changelog.txt README README.porting TODO twin-*.lsm \
	docs/{Configure,libTw++.txt,libTw.txt,Tutorial} clients/README.twsetroot

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%dir %{_libdir}/twin/
%dir %{_libdir}/twin/modules
%dir %{_libdir}/twin/modules/HW
%attr(755,root,root) %{_libdir}/twin/modules/*.so
%attr(755,root,root) %{_libdir}/twin/modules/HW/*.so

%files devel
%defattr(644,root,root,755)
%doc *.gz docs/*.gz clients/README*
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/*

#%files static
#%defattr(644,root,root,755)
#%{_libdir}/lib*.a
