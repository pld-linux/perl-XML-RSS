%include	/usr/lib/rpm/macros.perl
%define         pdir XML
%define         pnam RSS
Summary:	Module for RDF Site Summary (RSS) files managment
Summary(pl):	Modu� do zarz�dzania plikami RDF Site Summary (RSS)
Name:		perl-%{pdir}-%{pnam}
Version:	1.02
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	ce6ea96f39874ac23e35d8e1b85557ac
BuildRequires:	perl-devel >= 5.6.1
BuildRequires:	perl-XML-Parser >= 2.23
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description 
This module was created to help those who need to manage RDF Site
Summary (RSS) files. It makes quick work of creating, updating, and
saving RSS files.

%description -l pl
Ten modu� zosta� stworzony, aby pom�c przy zarz�dzaniu plikami RDF
Site Summary (RSS). Pozwala szybko tworzy�, uaktualnia� i zapisywa�
pliki RSS.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc TODO README Changes
%{perl_vendorlib}/%{pdir}/%{pnam}.pm
%{_mandir}/man3/*
