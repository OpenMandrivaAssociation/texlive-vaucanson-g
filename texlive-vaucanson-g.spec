# revision 15878
# category Package
# catalog-ctan /graphics/pstricks/contrib/vaucanson-g
# catalog-date 2008-10-30 09:45:25 +0100
# catalog-license lppl
# catalog-version 0.4
Name:		texlive-vaucanson-g
Version:	0.4
Release:	3
Summary:	PSTricks macros for drawing automata
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pstricks/contrib/vaucanson-g
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/vaucanson-g.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/vaucanson-g.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
VauCanSon-G is a package that enables the user to draw automata
within texts written using LaTeX. The package macros make use
of commands of PStricks.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
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

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Thu Jan 05 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.4-2
+ Revision: 757409
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.4-1
+ Revision: 719876
- texlive-vaucanson-g
- texlive-vaucanson-g
- texlive-vaucanson-g

