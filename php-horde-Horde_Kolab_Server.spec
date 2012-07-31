%define		status		stable
%define		pearname	Horde_Kolab_Server
%include	/usr/lib/rpm/macros.php
Summary:	%{pearname} - A package for manipulating the Kolab user database
Name:		php-horde-Horde_Kolab_Server
Version:	1.0.2
Release:	1
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.horde.org/get/%{pearname}-%{version}.tgz
# Source0-md5:	b4c266288968a17e0c99cddd640182ae
URL:		https://github.com/horde/horde/tree/master/framework/Kolab_Server/
BuildRequires:	php-channel(pear.horde.org)
BuildRequires:	php-packagexml2cl
BuildRequires:	php-pear-PEAR >= 1:1.7.0
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.610
Requires:	php-channel(pear.horde.org)
Requires:	php-hash
Requires:	php-horde-Horde_Auth < 2.0.0
Requires:	php-horde-Horde_Exception < 2.0.0
Requires:	php-pear >= 4:1.3.6-2
Suggests:	php-horde-Horde_Date
Suggests:	php-horde-Horde_Ldap
Suggests:	php-ldap
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# exclude optional dependencies
%define		_noautoreq	 pear(Horde/Date.*) pear(Horde/Ldap.*)

%description
This package allows to read/write entries in the Kolab user database
stored in LDAP.

In PEAR status of this package is: %{status}.

%prep
%pear_package_setup

mv docs/Horde_Kolab_Server/TODO .
mv docs/Horde_Kolab_Server/usage.txt .
mv docs/Horde_Kolab_Server/examples .

%build
packagexml2cl package.xml > ChangeLog

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post -p <lua>
%pear_package_print_optionalpackages

%files
%defattr(644,root,root,755)
%doc ChangeLog install.log
%doc optional-packages.txt
%doc TODO usage.txt
%{php_pear_dir}/.registry/.channel.*/*.reg
%dir %{php_pear_dir}/Horde/Kolab
%{php_pear_dir}/Horde/Kolab/Server
%{_examplesdir}/%{name}-%{version}
