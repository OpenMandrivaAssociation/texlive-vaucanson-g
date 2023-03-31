Name:		texlive-vaucanson-g
Version:	15878
Release:	2
Summary:	PSTricks macros for drawing automata
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pstricks/contrib/vaucanson-g
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/vaucanson-g.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/vaucanson-g.doc.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
