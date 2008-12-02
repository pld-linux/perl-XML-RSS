#
# Conditional build:
%bcond_with	tests	# perform "make test"
#			  (t/008_store_retrieve.t require network fetch)
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	XML
%define		pnam	RSS
Summary:	XML::RSS - module for RDF Site Summary (RSS) files managment
Summary(pl.UTF-8):	XML::RSS - moduł do zarządzania plikami RDF Site Summary (RSS)
Name:		perl-XML-RSS
Version:	1.40
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/XML/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	9dfd319f9562ddd0abd7d4a4cab5e0dd
URL:		http://search.cpan.org/dist/XML-RSS/
%if %{with tests}
BuildRequires:	perl-Test-Manifest >= 0.9
BuildRequires:	perl-XML-Parser >= 2.23
%endif
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Provides:	perl(XML::RSS::Creator)
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module was created to help those who need to manage RDF Site
Summary (RSS) files. It makes quick work of creating, updating, and
saving RSS files.

%description -l pl.UTF-8
Ten moduł został stworzony, aby pomóc przy zarządzaniu plikami RDF
Site Summary (RSS). Pozwala szybko tworzyć, uaktualniać i zapisywać
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
%{perl_vendorlib}/XML/RSS/Private
%{_mandir}/man3/XML::RSS.3pm*
