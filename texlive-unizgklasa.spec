Name:		texlive-unizgklasa
Version:	51647
Release:	2
Summary:	A LaTeX class for theses at the Faculty Of Graphic Arts in Zagreb
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/unizgklasa
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/unizgklasa.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/unizgklasa.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This class is intended for generating graduate and final theses
according to the instructions of the Faculty of Graphic Arts,
University of Zagreb. It does not necessarily correspond to the
requirements of each component of the University, but is
designed as an idea for linking and uniformizing the look of
all graduate papers. Anyone who likes it is welcome to use it.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/unizgklasa
%doc %{_texmfdistdir}/doc/latex/unizgklasa

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
