%define	version	0.2.1
%define release 	2

Summary:	Library of useful guile modules
Name:		guile-lib
Version:	%{version}
Release:	%{release}
License:	GPLv3
Group:		Development/Other
URL:		http://savannah.nongnu.org/projects/guile-lib
Source:		http://download.savannah.gnu.org/releases/guile-lib/%{name}-%{version}.tar.gz
BuildRequires:	texinfo
BuildRequires:	guile-devel
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
%makeinstall_std



%files
%doc {AUTHORS,ChangeLog,NEWS,README}
%{_infodir}/*.info*
%{_datadir}/guile/site/*




