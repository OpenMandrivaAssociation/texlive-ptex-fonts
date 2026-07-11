%global tl_name ptex-fonts
%global tl_revision 64330

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Fonts for use with pTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/ptex-fonts
License:	bsd3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ptex-fonts.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ptex-fonts.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The bundle contains fonts for use with pTeX and the documents for the
makejvf program. This is a redistribution derived from the ptex-texmf
distribution by ASCII MEDIA WORKS.

