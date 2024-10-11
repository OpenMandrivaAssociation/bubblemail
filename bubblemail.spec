Summary:	Extensible mail notification service.
Name:		bubblemail
Version:	1.9
Release:	1
Group:		Networking/Mail
License:	GPL-2.0-only
URL:		http://bubblemail.free.fr/
Source0:	https://framagit.org/razer/%{name}/-/archive/v%{version}/%{name}-v%{version}.tar.bz2
BuildRequires:	gettext-devel
BuildRequires:	pkgconfig(appstream-glib)
BuildRequires:	pkgconfig(folks)
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(pillow)
BuildRequires:	python%{pyver}dist(pyxdg)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	vala

Requires:	gnome-keyring
Requires:	gstreamer1.0-python
Requires:	%{_lib}folks-eds26
Requires:	python%{pyver}dist(dbus-python)
Requires:	python%{pyver}dist(requests)
Requires:	python%{pyver}dist(pyxdg)
Requires:	python%{pyver}dist(pysocks)
Requires:	typelib(Folks)
Recommends:	gnome-online-accounts
#Recommends:	gnome-shell-extension-bubblemail

%description
Bubblemail is a DBus service providing a list of the new and unread user's mail from:

  * Local inbox (mbox and maildir formats)
  * POP3 and/or IMAP servers defined as internal accounts
  * Gnome online accounts with email support (Google, Microsoft exchange, IMAP and SMTP)

It's desktop independent, highly configurable, can be extended via plugins, and is mostly
written in python.

%files -f %{name}.lang
%license LICENSE.txt
%doc AUTHORS CHANGELOG.md CONTRIBUTING.md README.md
%{_sysconfdir}/xdg/autostart/%{name}d.desktop
%{_bindir}/%{name}
%{_bindir}/%{name}-avatar-provider
%{_bindir}/%{name}d
%{_datadir}/applications/bubblemail.desktop
%{_datadir}/%{name}/
%{_datadir}/icons/hicolor/*/apps/%{name}.svg
%{_mandir}/man1/%{name}.1*
%{_mandir}/man1/%{name}d.1*
%{python3_sitelib}/%{name}/
%{python3_sitelib}/%{name}-%{version}-*.*-info
%{_metainfodir}/%{name}.appdata.xml

#----------------------------------------------------------------------

%prep
%autosetup -p1 -n %{name}-v%{version}


%build
%py_build

%install
%py_install

# locales
%find_lang %{name}

