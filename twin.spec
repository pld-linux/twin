#
# Conditional build:
%bcond_without	static_libs	# static library
%bcond_without	ggi		# GGI hw module
#
Summary:	Twin - a windowing environment
Summary(pl.UTF-8):	Tekstowe środowisko okienkowe
Name:		twin
Version:	0.8.1
Release:	1
License:	LGPL v2+
Group:		Libraries
#Source0Download: https://github.com/cosmos72/twin/tags
Source0:	https://github.com/cosmos72/twin/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	e98efaff326335d5947eb8f7f4bb2f6c
Patch0:		%{name}-ggi.patch
Patch1:		%{name}-ac.patch
Patch2:		%{name}-ncursesw.patch
URL:		https://sourceforge.net/projects/twin/
BuildRequires:	autoconf >= 2.65
BuildRequires:	automake >= 1:1.14
BuildRequires:	bash
BuildRequires:	fontconfig-devel
BuildRequires:	freetype-devel >= 2
BuildRequires:	gpm-devel
%{?with_ggi:BuildRequires:	libggi-devel}
BuildRequires:	libtool >= 2:2
BuildRequires:	ncurses-devel
BuildRequires:	pkgconfig >= 1:0.25
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXft-devel
BuildRequires:	xorg-lib-libXpm-devel
BuildRequires:	zlib-devel
Obsoletes:	twin-TT-hw-gtk < 0.8
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Twin is a windowing environment with mouse support, window manager,
terminal emulator and networked clients, all inside a text display.

It supports a variety of displays:
- plain text terminals (any termcap/ncurses compatible terminal, Linux
  console, twin's own terminal emulator);
- X11, where it can be used as a multi-window xterm;
- itself (you can display a twin on another twin);
- twdisplay, a general network-transparent display client, used to
  attach/detach more displays on-the-fly.

%description -l pl.UTF-8
Twin jest tekstowym środowiskiem okienkowym - zmienia terminal
tekstowy w środowisko podobne do zarządcy okien znanego ze środowiska
X Window.

Obsługuje wyświetlanie na:
- terminalach czysto tekstowych (dowolnym zgodnym z termcap/ncurses,
  konsoli Linuksa, własnym emulatorze Twin)
- w systemie X Window, gdzie może być używany jako wielookienkowy
  xterm
- sobie samym (można wyświetlać twin na innym twin)
- twdisplay, czyli ogólnym, przezroczystym sieciowo kliencie, używanym
  do dołączania i odłączania w locie.

%package devel
Summary:	Header files etc for developing twin applications
Summary(pl.UTF-8):	Pliki nagłówkowe dla twin
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files etc for developing twin applications.

%description devel -l pl.UTF-8
Pliki nagłówkowe i inne potrzebne do tworzenia programów opartych o
twin.

%package static
Summary:	Static twin libraries
Summary(pl.UTF-8):	Biblioteki statyczne twin
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static twin libraries.

%description static -l pl.UTF-8
Biblioteki statyczne twin.

%package hw-X11
Summary:	X11 driver for twin
Summary(pl.UTF-8):	Sterownik X11 do twin
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description hw-X11
X11 driver for twin.

%description hw-X11 -l pl.UTF-8
Sterownik X11 do twin.

%package hw-ggi
Summary:	GGI driver for twin
Summary(pl.UTF-8):	Sterownik GGI do twin
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description hw-ggi
GGI driver for twin.

%description hw-ggi -l pl.UTF-8
Sterownik GGI do twin.

%package hw-tty
Summary:	TTY driver with GPM support for twin
Summary(pl.UTF-8):	Sterownik TTY z obsługą GPM-a do twin
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description hw-tty
TTY driver with mouse support through GPM for twin.

%description hw-tty -l pl.UTF-8
Sterownik TTY z obsługą myszy przez GPM do twin.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{!?with_static_libs:--disable-static}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/twin/*.la
%if %{with static_libs}
%{__rm} $RPM_BUILD_ROOT%{_libdir}/twin/*.a
%endif

# packaged as %doc / in common-licenses
%{__rm} $RPM_BUILD_ROOT%{_datadir}/twin/{BUGS,COPYING*,Changelog.txt,INSTALL,README*,twin-current.lsm}
%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/twin/docs

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc BUGS Changelog.txt README.md docs/{Compatibility,FAQ,Philosophy,Tutorial} clients/README.twsetroot
%attr(755,root,root) %{_bindir}/twattach
%attr(755,root,root) %{_bindir}/twcat
%attr(755,root,root) %{_bindir}/twclip
%attr(755,root,root) %{_bindir}/twclutter
%attr(755,root,root) %{_bindir}/twcuckoo
%attr(755,root,root) %{_bindir}/twdetach
%attr(755,root,root) %{_bindir}/twdialog
%attr(755,root,root) %{_bindir}/twdisplay
%attr(755,root,root) %{_bindir}/twevent
%attr(755,root,root) %{_bindir}/twfindtwin
%attr(755,root,root) %{_bindir}/twin
%attr(755,root,root) %{_bindir}/twin_server
%attr(755,root,root) %{_bindir}/twlsmsgport
%attr(755,root,root) %{_bindir}/twlsobj
%attr(755,root,root) %{_bindir}/twsendmsg
%attr(755,root,root) %{_bindir}/twsetroot
%attr(755,root,root) %{_bindir}/twstart
%attr(755,root,root) %{_bindir}/twsysmon
%attr(755,root,root) %{_bindir}/twterm
%attr(755,root,root) %{_bindir}/twthreadtest
%attr(755,root,root) %{_sbindir}/twdm
%attr(755,root,root) %{_libdir}/libTutf.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libTutf.so.1
%attr(755,root,root) %{_libdir}/libTw.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libTw.so.5
%dir %{_libdir}/twin
%attr(755,root,root) %{_libdir}/twin/libhw_display*.so
%attr(755,root,root) %{_libdir}/twin/libhw_twin*.so
%attr(755,root,root) %{_libdir}/twin/librcparse*.so
%attr(755,root,root) %{_libdir}/twin/libsocket*.so
%attr(755,root,root) %{_libdir}/twin/libterm*.so
%attr(755,root,root) %{_libdir}/twin/libwm*.so
%attr(755,root,root) %{_libdir}/twin/system.twenvrc.sh
%attr(755,root,root) %{_libdir}/twin/system.twinrc
%dir %{_datadir}/twin
%dir %{_datadir}/twin/themes
%{_mandir}/man1/twin.1*

%files devel
%defattr(644,root,root,755)
%doc docs/{diagram.txt,libTT-design.txt,libTw.txt,ltrace.conf}
%attr(755,root,root) %{_libdir}/libTutf.so
%attr(755,root,root) %{_libdir}/libTw.so
%{_libdir}/libTutf.la
%{_libdir}/libTw.la
%{_includedir}/Tutf
%{_includedir}/Tw

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libTutf.a
%{_libdir}/libTw.a
%endif

%files hw-X11
%defattr(644,root,root,755)
%doc themes/hw_gfx/README
%attr(755,root,root) %{_libdir}/twin/libhw_X11*.so
%attr(755,root,root) %{_libdir}/twin/libhw_gfx*.so
%attr(755,root,root) %{_libdir}/twin/libhw_xft*.so
%{_datadir}/twin/themes/hw_gfx

%if %{with ggi}
%files hw-ggi
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/twin/libhw_ggi*.so
%endif

%files hw-tty
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/twin/libhw_tty*.so
