Summary:	User Tools
Summary(de):	Anwender-Tools
Summary(fr):	Outils utilisateur
Summary(pl):	Narzêdzia u¿ytkownika
Summary(tr):	Kullanýcý araçlarý
Name:		usermode
Version:	1.9
Release:	2
License:	GPL
Group:		X11/Applications
Source0:	%{name}-%{version}.tar.gz
Patch0:		%{name}-FHS20.patch
Requires:	util-linux
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Several graphical tools, including a tool to help users manage
floppies (and other removable media) and a tool to help the user
change his or her finger information.

%description -l de
Mehrere grafische Tools, u.a. eines zum Verwalten von Disketten (und
anderen Wechseldatenträgern) und eines zum Ändern der
Finger-Informationen eines Benutzers

%description -l fr
De nombreux outils graphiques, dont un outil pour aider les
utilsateurs à gérer les disquettes (et les autres supports amovibles)
et un outil pour aider les utilisateurs à modifier les informations
les concernant.

%description -l pl
Kilka graficznych narzêdzi, w tym program pomagaj±cy u¿ytkownikowi
zarz±dzanie dyskietkami (i innymi wymiennymi no¶nikami) tak¿e program
pomocny przy zmianie informacji dla programu finger.

%description -l tr
Bu paket, kullanýcýlarýn disketlerin yönetimini yapmak, kiþisel finger
bilgilerini deðiþtirmek gibi iþler için kullanabilecekleri araçlar
içerir.

%prep
%setup -q
%patch -p1

%build
%{__make} CFLAGS="%{rpmcflags} `gtk-config --cflags`"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install install-man PREFIX=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_applnkdir}/*
%attr(0755,root,root) %{_bindir}/*
%attr(4755,root,root) %{_sbindir}/userhelper
%{_mandir}/man[18]/*
