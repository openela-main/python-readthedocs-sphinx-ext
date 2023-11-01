%global srcname readthedocs-sphinx-ext

Name:           python-%{srcname}
Version:        2.1.4
Release:        3%{?dist}
Summary:        Sphinx extension for Read the Docs overrides

License:        MIT
URL:            https://github.com/readthedocs/readthedocs-sphinx-ext
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  %{py3_dist jinja2}
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist requests}
BuildRequires:  %{py3_dist sphinx}

%global _desc %{expand:
This module adds extensions that make Sphinx easier to use.  Some of them
require Read the Docs features, others are just code that we ship and
enable during builds on Read the Docs.  We currently ship:
- An extension for building docs like Read the Docs
- template-meta - allows users to specify template overrides in per-page
  contexts.}

%description %_desc

%package -n     python3-%{srcname}
Summary:        Sphinx extension for Read the Docs overrides

%description -n python3-%{srcname} %_desc

%prep
%autosetup -n %{srcname}-%{version}

%build
%py3_build
rst2html --no-datestamp README.rst README.html

%install
%py3_install

%check
%pytest

%files -n python3-%{srcname}
%doc README.html
%license LICENSE
%{python3_sitelib}/readthedocs_ext/
%{python3_sitelib}/readthedocs_sphinx_ext*

%changelog
* Tue Aug 10 2021 Mohan Boddu <mboddu@redhat.com> - 2.1.4-3
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Fri Apr 16 2021 Mohan Boddu <mboddu@redhat.com> - 2.1.4-2
- Rebuilt for RHEL 9 BETA on Apr 15th 2021. Related: rhbz#1947937

* Wed Mar 17 2021 Jerry James <loganjerry@gmail.com> - 2.1.4-1
- Version 2.1.4

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jan 19 2021 Jerry James <loganjerry@gmail.com> - 2.1.3-1
- Version 2.1.3
- Revert to the py3_* macros (avoids dependency on external mock)

* Wed Jan  6 2021 Jerry James <loganjerry@gmail.com> - 2.1.2-1
- Version 2.1.2

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 23 2020 Jerry James <loganjerry@gmail.com> - 2.1.1-1
- Version 2.1.1

* Sat Jul 11 2020 Jerry James <loganjerry@gmail.com> - 2.1.0-1
- Version 2.1.0

* Tue Jun 16 2020 Jerry James <loganjerry@gmail.com> - 2.0.0-1
- Version 2.0.0

* Fri May 29 2020 Jerry James <loganjerry@gmail.com> - 1.0.4-2
- Remove unnecessary version manipulation

* Fri May 29 2020 Jerry James <loganjerry@gmail.com> - 1.0.4-1
- Version 1.0.4

* Mon May 25 2020 Miro Hrončok <mhroncok@redhat.com> - 1.0.3-2
- Rebuilt for Python 3.9

* Tue Apr 21 2020 Jerry James <loganjerry@gmail.com> - 1.0.3-1
- Version 1.0.3

* Thu Jan 30 2020 Jerry James <loganjerry@gmail.com> - 1.0.1-1
- Initial RPM
