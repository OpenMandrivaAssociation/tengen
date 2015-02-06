%define	version	0.1.0
%define release	9

Summary:	Go chess for GNOME
Name:		tengen
Version:	%{version}
Release:	%{release}
License:	GPLv2+
Group:		Games/Boards
URL:		http://tengen.rubyforge.org/
Source:		http://rubyforge.org/frs/download.php/2390/%{name}-%{version}.tar.bz2
Patch0:		tengen-0.1.0-nomutex.patch
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch
BuildRequires:	ruby
Requires:	ruby-libglade2
Requires:	ruby-gnome2
Requires:	gnugo

%description
Tengen is a GNOME program that plays Go, a strategic board game that's
popular worldwide. Currently it features:

* SVG graphics
* handles board sizes from 5x5 to 19x19
* can redo moves
* can play either against the computer or a human being

%prep
%setup -q
%patch0 -p1

%build
ruby install.rb config --bin-dir=%{_gamesbindir} \
	--data-dir=%{_gamesdatadir} \
	--site-ruby=%{ruby_vendorlibdir}
ruby install.rb setup

%install
rm -rf %{buildroot}
ruby install.rb install --prefix=%{buildroot}

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Tengen
Comment=Go chess for GNOME
Exec=%{_gamesbindir}/%{name}
Icon=strategy_section
Terminal=false
Type=Application
Categories=GNOME;GTK;X-MandrivaLinux-MoreApplications-Games-Boards;Game;BoardGame;
EOF

%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%endif

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING NEWS README
%{_gamesbindir}/*
%{_gamesdatadir}/%{name}
%{ruby_vendorlibdir}/*
%{_datadir}/applications/*


%changelog
* Sat Oct 10 2009 John Balcaen <mikala@mandriva.org> 0.1.0-8mdv2010.0
+ Revision: 456483
- Fix desktop file ( bug #44889)

* Sun Sep 20 2009 Thierry Vignaud <tvignaud@mandriva.com> 0.1.0-7mdv2010.0
+ Revision: 445416
- rebuild

* Fri Apr 03 2009 Pascal Terjan <pterjan@mandriva.org> 0.1.0-6mdv2009.1
+ Revision: 363706
- Fix a crash with recent ruby (#49482)
- Use vendor dir
- Update License tag

* Sat Aug 02 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.1.0-5mdv2009.0
+ Revision: 261483
- rebuild

* Wed Jul 30 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.1.0-4mdv2009.0
+ Revision: 254384
- rebuild
- drop old menu

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.1.0-2mdv2008.1
+ Revision: 136535
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request
    - kill explicit icon extension
    - kill desktop-file-validate's 'warning: key "Encoding" in group "Desktop Entry" is deprecated'


* Sun Jan 07 2007 Pascal Terjan <pterjan@mandriva.org> 0.1.0-2mdv2007.0
+ Revision: 105057
- mkrel
- XDG menu
- use ruby macros
- Import tengen

* Thu Dec 30 2004 Abel Cheung <deaddog@mandrake.org> 0.1.0-1mdk
- First Mandrakelinux package

