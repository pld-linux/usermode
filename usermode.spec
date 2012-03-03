Summary:	Tools for certain user account management tasks
Summary(de.UTF-8):	Anwender-Tools
Summary(fr.UTF-8):	Outils utilisateur
Summary(pl.UTF-8):	Narzędzia użytkownika
Summary(tr.UTF-8):	Kullanıcı araçları
Name:		usermode
Version:	1.108
Release:	1
License:	GPL v2+
Group:		Applications/System
Source0:	https://fedorahosted.org/releases/u/s/usermode/%{name}-%{version}.tar.xz
# Source0-md5:	bef795b757defb9fd27cfbd48ef79861
Source1:	config-util
URL:		https://fedorahosted.org/usermode/
BuildRequires:	gtk+2-devel
BuildRequires:	libuser-devel
BuildRequires:	pam-devel
BuildRequires:	pwdb-devel
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
#Requires:	nss_db
Requires:	util-linux
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The usermode package contains the userhelper program, which can be
used to allow configured programs to be run with superuser privileges
by ordinary users.

%description -l de.UTF-8
Mehrere grafische Tools, u.a. eines zum Verwalten von Disketten (und
anderen Wechseldatenträgern) und eines zum Ändern der
Finger-Informationen eines Benutzers

%description -l fr.UTF-8
De nombreux outils graphiques, dont un outil pour aider les
utilsateurs à gérer les disquettes (et les autres supports amovibles)
et un outil pour aider les utilisateurs à modifier les informations
les concernant.

%description -l pl.UTF-8
Kilka graficznych narzędzi, w tym program pomagający użytkownikowi
zarządzanie dyskietkami (i innymi wymiennymi nośnikami) także program
pomocny przy zmianie informacji dla programu finger.

%description -l tr.UTF-8
Bu paket, kullanıcıların disketlerin yönetimini yapmak, kişisel finger
bilgilerini değiştirmek gibi işler için kullanabilecekleri araçlar
içerir.

%package gtk
Summary:	Graphical tools for certain user account management tasks
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}

%description gtk
The usermode-gtk package contains several graphical tools for users:
userinfo, usermount and userpasswd. Userinfo allows users to change
their finger information. Usermount lets users mount, unmount, and
format file systems. Userpasswd allows users to change their
passwords.

Install the usermode-gtk package if you would like to provide users
with graphical tools for certain account management tasks.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	INSTALL='install -p' \
	DESTDIR=$RPM_BUILD_ROOT

# in pld we do not install default wrappers
%{__rm} -v $RPM_BUILD_ROOT/etc/security/console.apps/*
%{__rm} $RPM_BUILD_ROOT%{_bindir}/shutdown

install -p %{SOURCE1} \
	$RPM_BUILD_ROOT/etc/security/console.apps/config-util

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ChangeLog NEWS README
%attr(4711,root,root) %{_sbindir}/userhelper
%attr(755,root,root) %{_bindir}/consolehelper
%config(noreplace) %verify(not md5 mtime size) /etc/security/console.apps/config-util
%{_mandir}/man8/userhelper.8*
%{_mandir}/man8/consolehelper.8*

%files gtk
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/consolehelper-gtk
%attr(755,root,root) %{_bindir}/pam-panel-icon
%attr(755,root,root) %{_bindir}/userinfo
%attr(755,root,root) %{_bindir}/usermount
%attr(755,root,root) %{_bindir}/userpasswd
%{_mandir}/man1/pam-panel-icon.1*
%{_mandir}/man1/userinfo.1*
%{_mandir}/man1/usermount.1*
%{_mandir}/man1/userpasswd.1*
%{_mandir}/man8/consolehelper-gtk.8*
%{_datadir}/%{name}
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*.png
%{_pixmapsdir}/keys.xpm
