Summary:	LinuxPhobia - fast schooting game
Summary(pl):	LinuxPhobia - gra - bardzo szybka strzelanka
Name:		linuxphobia	
Version:	1.1
Release:	1
License:	Free
Group:		X11/Applications/Games	
Source0:	http://www.lynxlabs.com/games/linuxphobia/%{name}-%{version}-i386.tar.bz2
Source1:	LinuxPhobia.desktop	
URL:		http://www.lynxlabs.com/games/linuxphobia/index.html
Requires:	SDL
Requires:	SDL_mixer
Requires:	XFree86
ExclusiveArch:  %{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Fast shooting game. Features:
- full 360 degrees of freedom
- 200 aliens on screen at same time!
- one or two players
- lots of weapons
- light effects
- Ogworbis-musics and dynamic stereo sounds
- 3D rendered graphics 

%description -l pl
Bardzo szybka "strzelanka".
- obroty o 360 stopni,
- 200 ufoli jednocze¶nie,
- gra w pojedynkê lub w dwójkê,
- du¿o borni,
- efekty ¶wietlne,
- s³odkie odg³osy w stereo,
- grafika 3D,

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/X11R6/share/{games/%{name},applnk/Games}		

mv -f {dat/,music/,pics/,sounds/} $RPM_BUILD_ROOT/usr/X11R6/share/games/%{name}/
mv {linuxphobia,phobia2.ico}	$RPM_BUILD_ROOT/usr/X11R6/share/games/%{name}

install %{SOURCE1}	$RPM_BUILD_ROOT/usr/X11R6/share/applnk/Games/

gzip -nf9 README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root)/usr/X11R6/share/games/%{name}/linuxphobia
/usr/X11R6/share/games/%{name}/phobia2.ico
/usr/X11R6/share/games/%{name}/dat
/usr/X11R6/share/games/%{name}/music
/usr/X11R6/share/games/%{name}/pics
/usr/X11R6/share/games/%{name}/sounds
/usr/X11R6/share/applnk/Games/
