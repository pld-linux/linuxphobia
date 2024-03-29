Summary:	LinuxPhobia - fast schooting game
Summary(pl.UTF-8):	LinuxPhobia - gra, bardzo szybka strzelanka
Name:		linuxphobia
Version:	1.1
Release:	2
License:	probably free, but no source
Group:		X11/Applications/Games
Source0:	%{name}-%{version}-i386.tar.bz2
# Source0-md5:	e5d3deac8f4c03a3fd3855c5a2449535
Source1:	LinuxPhobia.desktop
# no longer valid
#URL:		http://www.lynxlabs.com/games/linuxphobia/index.html
Requires:	SDL
Requires:	SDL_mixer
Requires:	XFree86
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libdir		%{_prefix}/lib/%{name}

%description
Fast shooting game. Features:
- full 360 degrees of freedom
- 200 aliens on screen at same time!
- one or two players
- lots of weapons
- light effects
- Ogg-Vorbis musics and dynamic stereo sounds
- 3D rendered graphics

%description -l pl.UTF-8
Bardzo szybka "strzelanka". Cechy:
- obroty o 360 stopni,
- 200 ufoli jednocześnie,
- gra w pojedynkę lub we dwójkę,
- dużo broni,
- efekty świetlne,
- słodkie odgłosy w stereo,
- grafika 3D.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_applnkdir}/Games}

mv -f {dat/,music/,pics/,sounds/} $RPM_BUILD_ROOT%{_libdir}
mv -f {linuxphobia,phobia2.ico} $RPM_BUILD_ROOT%{_libdir}

cat %{SOURCE1} | sed "s:LIBDIR:%{_libdir}:" > $RPM_BUILD_ROOT%{_applnkdir}/Games/LinuxPhobia.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%dir %{_libdir}
%attr(755,root,root) %{_libdir}/linuxphobia
%{_libdir}/phobia2.ico
%{_libdir}/dat
%{_libdir}/music
%{_libdir}/pics
%{_libdir}/sounds
%{_applnkdir}/Games/*.desktop
