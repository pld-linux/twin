Summary:	Twin - a windowing environment
Summary(pl):	Tekstowe ¶rodowisko okienkowe
Name:		twin
Version:	0.5.1
Release:	2
License:	LGPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/twin/%{name}-%{version}.tar.gz
# Source0-md5:	46b31e1bdd4fda60336da24034896c53
Patch0:		%{name}-bitops.patch
URL:		http://twin.sourceforge.net/
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gpm-devel
BuildRequires:	gtk+-devel
BuildRequires:	libggi-devel
BuildRequires:	libtool
BuildRequires:	ncurses-devel
BuildRequires:	zlib-devel
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

%description -l pl
Twin jest tekstowym ¶rodowiskiem okienkowym - zmienia terminal
tekstowy w ¶rodowisko podobne do zarz±dcy okien znanego ze ¶rodowiska
X Window.

Obs³uguje wy¶wietlanie na:
- terminalach czysto tekstowych (dowolnym zgodnym z termcap/ncurses,
  konsoli Linuksa, w³asnym emulatorze Twin)
- w systemie X Window, gdzie mo¿e byæ u¿ywany jako wielookienkowy
  xterm
- sobie samym (mo¿na wy¶wietlaæ twin na innym twin)
- twdisplay, czyli ogólnym, przezroczystym sieciowo kliencie, u¿ywanym
  do do³±czania i od³±czania w locie.

%package devel
Summary:	Header files etc for developing twin applications
Summary(pl):	Pliki nag³ówkowe dla twin
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files etc for developing twin applications.

%description devel -l pl
Pliki nag³ówkowe i inne potrzebne do tworzenia programów opartych o
twin.

%package static
Summary:	Static twin libraries
Summary(pl):	Biblioteki statyczne twin
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static twin libraries.

%description static -l pl
Biblioteki statyczne twin.

%package TT-hw-gtk
Summary:	TT GTK+ driver for twin
Summary(pl):	Sterownik TT GTK+ do twin
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description TT-hw-gtk
GTK+ target driver for twin's TT library.

%description TT-hw-gtk -l pl
Sterownik wyj¶cia GTK+ do biblioteki TT z twin.

%package hw-X11
Summary:	X11 driver for twin
Summary(pl):	Sterownik X11 do twin
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description hw-X11
X11 driver for twin.

%description hw-X11 -l pl
Sterownik X11 do twin.

%package hw-ggi
Summary:	GGI driver for twin
Summary(pl):	Sterownik GGI do twin
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description hw-ggi
GGI driver for twin.

%description hw-ggi -l pl
Sterownik GGI do twin.

%package hw-tty
Summary:	TTY driver with GPM support for twin
Summary(pl):	Sterownik TTY z obs³ug± GPM-a do twin
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description hw-tty
TTY driver with mouse support through GPM for twin.

%description hw-tty -l pl
Sterownik TTY z obs³ug± myszy przez GPM do twin.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%configure

%{__make} \
	CFLAGS="%{rpmcflags} -Wall -D_GNU_SOURCE"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}/man1

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install docs/twin.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc BUGS Changelog.txt README docs/{Compatibility,Philosophy,Tutorial}
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_sbindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%dir %{_libdir}/TT
%dir %{_libdir}/TT/modules
%dir %{_libdir}/TT/modules/HW
%attr(755,root,root) %{_libdir}/TT/modules/HW/twin*.so*
%attr(755,root,root) %{_libdir}/TT/modules/HW/xml.so*
%dir %{_libdir}/twin
%{_libdir}/twin/system.*
%dir %{_libdir}/twin/modules
%attr(755,root,root) %{_libdir}/twin/modules/*.so*
%dir %{_libdir}/twin/modules/HW
%attr(755,root,root) %{_libdir}/twin/modules/HW/hw_display.so*
%attr(755,root,root) %{_libdir}/twin/modules/HW/hw_twin.so*
%dir %{_datadir}/twin
%dir %{_datadir}/twin/themes
%{_mandir}/man1/*

%files devel
%defattr(644,root,root,755)
%doc docs/{diagram.txt,libTT-design.txt,libTw.txt,ltrace.conf} clients/README.twsetroot
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%files TT-hw-gtk
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/TT/modules/HW/gtk.so*

%files hw-X11
%defattr(644,root,root,755)
%doc themes/hw_gfx/README
%attr(755,root,root) %{_libdir}/TT/modules/HW/X11.so*
%attr(755,root,root) %{_libdir}/twin/modules/HW/hw_X*.so*
%attr(755,root,root) %{_libdir}/twin/modules/HW/hw_gfx.so*
%dir %{_datadir}/twin/themes/hw_gfx
%{_datadir}/twin/themes/hw_gfx/*.xpm

%files hw-ggi
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/twin/modules/HW/hw_ggi.so*

%files hw-tty
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/twin/modules/HW/hw_tty.so*
