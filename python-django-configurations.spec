# Created by pyp2rpm-3.3.2
%global pypi_name django-configurations

Name:           python-%{pypi_name}
Version:        2.1
Release:        1%{?dist}
Summary:        A helper for organizing Django settings

License:        BSD
URL:            https://django-configurations.readthedocs.io/
Source0:        https://files.pythonhosted.org/packages/source/d/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(sphinx)

# If we do want to enable tests, we need these deps.
# They are listed in tests/requirements.txt
#BuildRequires:  python3dist(coverage)
#BuildRequires:  python3dist(mock)
#BuildRequires:  python3dist(dj-database-url)
#BuildRequires:  python3dist(six)

# As well as these deps not in Fedora yet.
# They are listed in tests/requirements.txt
#BuildRequires:  python3dist(django-discover-runner)
#BuildRequires:  python3dist(dj-email-url)
#BuildRequires:  python3dist(dj-search-url)
#BuildRequires:  python3dist(django-cache-url) >= 1.0.0

%description
django-configurations django-configurations eases Django project configuration
by relying on the composability of Python classes. It extends the notion of

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
 
Requires:       python3dist(setuptools)
%description -n python3-%{pypi_name}
django-configurations django-configurations eases Django project configuration
by relying on the composability of Python classes. It extends the notion of

%package -n python-%{pypi_name}-doc
Summary:        django-configurations documentation
%description -n python-%{pypi_name}-doc
Documentation for django-configurations

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build
# generate html docs 
PYTHONPATH=${PWD} sphinx-build-3 docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%py3_install

# Disable due to large # of deps not in Fedora yet
#%%check
#%%{__python3} setup.py test

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{_bindir}/django-cadmin
%{python3_sitelib}/configurations
%{python3_sitelib}/django_configurations-%{version}-py?.?.egg-info

%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE

%changelog
* Thu Mar 21 2019 Mike DePaulo <mikedep333@redhat.com> - 2.1-1
- Initial package.
