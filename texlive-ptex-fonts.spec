Name:		texlive-ptex-fonts
Version:	64330
Release:	1
Summary:	Fonts for use with pTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ptex-fonts
License:	bsd3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ptex-fonts.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ptex-fonts.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The bundle contains fonts for use with pTeX and the documents
for the makejvf program. This is a redistribution derived from
the ptex-texmf distribution by ASCII MEDIA WORKS.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/fonts/vf/ptex-fonts
%{_texmfdistdir}/fonts/tfm/ptex-fonts
%doc %{_texmfdistdir}/fonts/source/ptex-fonts
%doc %{_texmfdistdir}/doc/fonts/ptex-fonts

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
