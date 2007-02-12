Summary:	User Tools
Summary(de.UTF-8):   Anwender-Tools
Summary(fr.UTF-8):   Outils utilisateur
Summary(pl.UTF-8):   Narzędzia użytkownika
Summary(tr.UTF-8):   Kullanıcı araçları
Name:		usermode
Version:	1.9
Release:	3
License:	GPL
Group:		X11/Applications
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	173586e150c4669bca40943af84104cf
Patch0:		%{name}-FHS20.patch
BuildRequires:	gtk+-devel
BuildRequires:	pam-devel
BuildRequires:	pwdb-devel
Requires:	util-linux
#Requires:	nss_db
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Several graphical tools, including a tool to help users manage
floppies (and other removable media) and a tool to help the user
change his or her finger information.

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

%prep
%setup -q
%patch0 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} `gtk-config --cflags`"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}

%{__make} install install-man \
	PREFIX=$RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT/etc/X11/applnk/System/* $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(0755,root,root) %{_bindir}/*
%attr(4755,root,root) %{_sbindir}/userhelper
%{_mandir}/man[18]/*
%{_desktopdir}/*.desktop
