Summary:	LinuxPhobia - fast schooting game
Summary(pl):	LinuxPhobia - gra - bardzo szybka strzelanka
Name:		linuxphobia
Version:	1.1
Release:	1
License:	probably free, but no source
Group:		X11/Applications/Games
Source0:	http://www.lynxlabs.com/games/linuxphobia/%{name}-%{version}-i386.tar.bz2
Source1:	LinuxPhobia.desktop
URL:		http://www.lynxlabs.com/games/linuxphobia/index.html
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
- Ogg-vorbis musics and dynamic stereo sounds
- 3D rendered graphics

%description -l pl
Bardzo szybka "strzelanka". Cechy:
- obroty o 360 stopni,
- 200 ufoli jednocze¶nie,
- gra w pojedynkê lub we dwójkê,
- du¿o broni,
- efekty ¶wietlne,
- s³odkie odg³osy w stereo,
- grafika 3D.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_applnkdir}/Games}

mv -f {dat/,music/,pics/,sounds/} $RPM_BUILD_ROOT%{_libdir}
mv -f {linuxphobia,phobia2.ico} $RPM_BUILD_ROOT%{_libdir}

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Games

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
