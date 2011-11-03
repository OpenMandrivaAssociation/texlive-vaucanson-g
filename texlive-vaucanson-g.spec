# revision 15878
# category Package
# catalog-ctan /graphics/pstricks/contrib/vaucanson-g
# catalog-date 2008-10-30 09:45:25 +0100
# catalog-license lppl
# catalog-version 0.4
Name:		texlive-vaucanson-g
Version:	0.4
Release:	1
Summary:	PSTricks macros for drawing automata
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pstricks/contrib/vaucanson-g
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/vaucanson-g.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/vaucanson-g.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
VauCanSon-G is a package that enables the user to draw automata
within texts written using LaTeX. The package macros make use
of commands of PStricks.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/vaucanson-g/VCColor-names.def
%{_texmfdistdir}/tex/generic/vaucanson-g/VCPref-beamer.tex
%{_texmfdistdir}/tex/generic/vaucanson-g/VCPref-default.tex
%{_texmfdistdir}/tex/generic/vaucanson-g/VCPref-mystyle.tex
%{_texmfdistdir}/tex/generic/vaucanson-g/VCPref-slides.tex
%{_texmfdistdir}/tex/generic/vaucanson-g/Vaucanson-G.tex
%{_texmfdistdir}/tex/generic/vaucanson-g/vaucanson-g.sty
%{_texmfdistdir}/tex/generic/vaucanson-g/vaucanson.sty
%doc %{_texmfdistdir}/doc/generic/vaucanson-g/CHANGES
%doc %{_texmfdistdir}/doc/generic/vaucanson-g/README
%doc %{_texmfdistdir}/doc/generic/vaucanson-g/VCManual-src/TwoStates.tex
%doc %{_texmfdistdir}/doc/generic/vaucanson-g/VCManual-src/VCManual.tex
%doc %{_texmfdistdir}/doc/generic/vaucanson-g/VCManual.pdf
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
