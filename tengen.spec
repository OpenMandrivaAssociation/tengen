%define	version	0.1.0
%define release	%mkrel 2

Summary:	Go chess for GNOME
Name:		tengen
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Games/Boards
URL:		http://tengen.rubyforge.org/
Source:		http://rubyforge.org/frs/download.php/2390/%{name}-%{version}.tar.bz2
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

%build
ruby install.rb config --bin-dir=%{_gamesbindir} --data-dir=%{_gamesdatadir}
ruby install.rb setup

%install
rm -rf %{buildroot}
ruby install.rb install --prefix=%{buildroot}


mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Tengen
Comment=Go chess for GNOME
Exec=%{_bindir}/%{name}
Icon=strategy_section
Terminal=false
Type=Application
Categories=GNOME;GTK;X-MandrivaLinux-MoreApplications-Games-Boards;Game;BoardGame;
EOF

%post
%update_menus

%postun
%clean_menus

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING NEWS README
%{_gamesbindir}/*
%{_gamesdatadir}/%{name}
%{ruby_sitelibdir}/*
%{_datadir}/applications/*


