%include	/usr/lib/rpm/macros.perl
%define         pdir XML
%define         pnam RSS

Summary:	Module for RDF Site Summary (RSS) files managment
Summary(pl):	Modu³ do zarz±dzania plikami RDF Site Summary (RSS)
Name:		perl-%{pdir}-%{pnam}
Version:	0.97
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6.1
BuildRequires:	perl-XML-Parser
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
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf BUGS TODO README Changes

find $RPM_BUILD_ROOT -name .packlist | xargs -r rm -f

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_sitelib}/%{pdir}/%{pnam}.pm
%{_mandir}/man3/*
%doc *.gz
