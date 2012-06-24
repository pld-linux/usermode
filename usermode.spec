Summary:	User Tools
Summary(de):	Anwender-Tools
Summary(fr):	Outils utilisateur
Summary(pl):	Narz�dzia u�ytkownika
Summary(tr):	Kullan�c� ara�lar�
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

%description -l de
Mehrere grafische Tools, u.a. eines zum Verwalten von Disketten (und
anderen Wechseldatentr�gern) und eines zum �ndern der
Finger-Informationen eines Benutzers

%description -l fr
De nombreux outils graphiques, dont un outil pour aider les
utilsateurs � g�rer les disquettes (et les autres supports amovibles)
et un outil pour aider les utilisateurs � modifier les informations
les concernant.

%description -l pl
Kilka graficznych narz�dzi, w tym program pomagaj�cy u�ytkownikowi
zarz�dzanie dyskietkami (i innymi wymiennymi no�nikami) tak�e program
pomocny przy zmianie informacji dla programu finger.

%description -l tr
Bu paket, kullan�c�lar�n disketlerin y�netimini yapmak, ki�isel finger
bilgilerini de�i�tirmek gibi i�ler i�in kullanabilecekleri ara�lar
i�erir.

%prep
%setup -q
%patch -p1

%build
%{__make} \
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
%{_desktopdir}/*
