#
# Conditional build:
%bcond_without tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	XML
%define	pnam	RSS
Summary:	XML::RSS - module for RDF Site Summary (RSS) files managment
Summary(pl):	XML::RSS - modu³ do zarz±dzania plikami RDF Site Summary (RSS)
Name:		perl-%{pdir}-%{pnam}
Version:	1.04
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	7fd0c5393c3fffac0dcf447d9f0dfb4f
%if %{with tests}
BuildRequires:	perl-Test-Manifest >= 0.9
BuildRequires:	perl-XML-Parser >= 2.23
%endif
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module was created to help those who need to manage RDF Site
Summary (RSS) files. It makes quick work of creating, updating, and
saving RSS files.

%description -l pl
Ten modu³ zosta³ stworzony, aby pomóc przy zarz±dzaniu plikami RDF
Site Summary (RSS). Pozwala szybko tworzyæ, uaktualniaæ i zapisywaæ
pliki RSS.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{perl_vendorlib}/XML/RSS

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc TODO README Changes
%{perl_vendorlib}/XML/RSS.pm
%dir %{perl_vendorlib}/XML/RSS
%{_mandir}/man3/*
