%define	version	0.1.2
%define release	%mkrel 1

Summary:	Library of useful guile modules
Name:		guile-lib
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Development/Other
URL:		http://home.gna.org/guile-lib/
Source:		%{name}-%{version}.tar.bz2
BuildRequires:	texinfo
Requires:	guile >= 1.6
BuildArch:	noarch

%description
A set of various-purpose library modules for Guile. Covered areas include:

  * Unit testing framework ala JUnit
  * Logging system
  * String routines (wrapping, completion, soundex algorithm)
  * OS process chains (think "shell pipes in scheme")
  * ANSI escape sequence text coloring
  * SRFI-35 (conditions)

%prep
%setup -q
chmod 0644 src/guile-lib/src/sxml/ssax.scm

%build
mkdir ,,build
cd ,,build
../src/configure --prefix=%{_prefix} --destdir=%{buildroot}
make

%install
rm -rf %{buildroot}
cd ,,build
mkdir -p %{buildroot}%{_infodir}
make install

%clean
rm -rf %{buildroot}

%post
%_install_info guile-library.info

%preun
%_remove_install_info guile-library.info

%files
%defattr(-,root,root)
%doc src/guile-lib/{AUTHORS,ChangeLog,NEWS,README}
%{_infodir}/*.info*
%{_datadir}/guile/site/*

