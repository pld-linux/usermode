Summary:     User Tools
Summary(de): Anwender-Tools
Summary(fr): Outils utilisateur
Summary(pl): Narzêdzia u¿ytkownika
Summary(tr): Kullanýcý araçlarý
Name:        usermode
Version:     1.4.3
Release:     2
Copyright:   GPL
Group:       X11/Applications
Group(pl):   X11/Aplikacje
Source:      %{name}-%{version}.tar.gz
Patch:       usermode.patch
Requires:    util-linux
Buildroot:   /tmp/%{name}-%{version}-root

%description
Several graphical tools, including a tool to help users manage floppies
(and other removable media) and a tool to help the user change his or
her finger information.

%description -l de
Mehrere grafische Tools, u.a. eines zum Verwalten von Disketten (und anderen Wechseldatenträgern) und eines zum Ändern der Finger-Informationen eines Benutzers

%description -l fr
De nombreux outils graphiques, dont un outil pour aider les
utilsateurs à gérer les disquettes (et les autres supports amovibles) et un
outil pour aider les utilisateurs à modifier les informations les
concernant.

%description -l pl
Kilka graficznych narzêdzi, w tym program pomagaj±cy u¿ytkownikowi
zarz±dzanie dyskietkami (i innymi wymiennymi no¶nikami) tak¿e program
pomocny przy zmianie informacji dla programu finger.

%description -l tr
Bu paket, kullanýcýlarýn disketlerin yönetimini yapmak, kiþisel finger
bilgilerini deðiþtirmek gibi iþler için kullanabilecekleri araçlar içerir.

%prep
%setup -q
%patch -p1

%build
make CFLAGS="$RPM_OPT_FLAGS `gtk-config --cflags`"

%install
rm -rf $RPM_BUILD_ROOT
make PREFIX=$RPM_BUILD_ROOT install
make PREFIX=$RPM_BUILD_ROOT install-man

gzip -9nf $RPM_BUILD_ROOT/usr/man/man{1,8}/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644, root, root, 755)
/etc/X11/wmconfig/*
%attr(0755, root, root) /usr/bin/*
%attr(4755, root, root) /usr/sbin/userhelper
%attr(0644, root,  man) /usr/man/man[18]/*

%changelog
* Tue Dec 1 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.4.3-2]
- added -q %setup parameter,
- added gzipping man pages,
- simpification in %files,
- added using $RPM_OPT_FLAGS during conpile,
- added Group(pl).

* Sat Oct 31 1998 Przemys³aw Bia³ek <lobo@polbox.com>
- added %%defattr macro to allows build package from non root account,
- modify package for gtk-1.1.x,
- added pl translation.

* Wed Jun 10 1998 Prospector System <bugs@redhat.com>
- translations modified for de

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Apr 16 1998 Erik Troan <ewt@redhat.com>
- use gtk-config during build
- added make archive rule to Makefile
- uses a build root

* Fri Nov  7 1997 Otto Hammersmith <otto@redhat.com>
new version that fixed memory leak bug.

* Mon Nov  3 1997 Otto Hammersmith <otto@redhat.com>
updated version to fix bugs

* Fri Oct 17 1997 Otto Hammersmith <otto@redhat.com>
Wrote man pages for userpasswd and userhelper.

* Tue Oct 14 1997 Otto Hammersmith <otto@redhat.com>
Updated the packages... now includes userpasswd for changing passwords
and newer versions of usermount and userinfo.  No known bugs or
misfeatures. 

Fixed the file list...

* Mon Oct 6 1997 Otto Hammersmith <otto@redhat.com>
Created the spec file.
