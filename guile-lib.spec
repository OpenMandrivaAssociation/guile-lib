%define	version	0.1.6
%define release	%mkrel 1

Summary:	Library of useful guile modules
Name:		guile-lib
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Development/Other
URL:		http://home.gna.org/guile-lib/
Source:		http://download.gna.org/guile-lib/%{name}-%{version}.tar.gz
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
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

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%post
%_install_info guile-library.info

%preun
%_remove_install_info guile-library.info

%files
%defattr(-,root,root)
%doc {AUTHORS,ChangeLog,NEWS,README}
%{_infodir}/*.info*
%{_datadir}/guile/site/*

