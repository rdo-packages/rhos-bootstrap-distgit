%global debug_package %{nil}
%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

Name:           rhos-bootstrap
Summary:        Red Hat OpenStack bootstrap utility
Version:        XXX
Release:        XXX

Group:          System Environment/Base
License:        ASL 2.0

URL:            https://github.com/redhat-openstack/rhos-bootstrap
Source:         https://github.com/redhat-openstack/rhos-bootstrap/archive/%{upstream_version}.tar.gz#/rhos-bootstrap-%{upstream_version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(setuptools-scm)

Requires:       python3-libdnf
Requires:       python3-dnf
Requires:       python3-pyyaml
Requires:       python3-requests

Suggests:       subscription-manager

%{?python_provide:%python_provide python3-%{name}}

%description
A bootstrap tool used to handle repository, dnf module configuration, and
tripleoclient installation in preparation for a Red Hat OpenStack installation.

%prep
%autosetup -n rhos-bootstrap-%{upstream_version} -S git
rm -rf *.egg-info

%build
%{py3_build}

%install
%{py3_install}
install -d -m 755 %{buildroot}/%{_datadir}/%{name}
cp -ar versions/*.yaml %{buildroot}/%{_datadir}/%{name}

%files
%license LICENSE
%doc README.rst AUTHORS ChangeLog
%{python3_sitelib}/rhos_bootstrap*
%{_bindir}/%{name}
%{_datadir}/%{name}

%changelog
