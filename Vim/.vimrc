set nocompatible        " required
filetype off            " required

" set the runtime path to include Vundle and initialize
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()

" alternatively, pass a path where Vundle should install plugins
"call vundle#begin('~/some/path/here')

" let Vundle manage Vundle, required
Plugin 'gmarik/Vundle.vim'
Plugin 'vim-scripts/indentpython.vim'
Plugin 'Valloric/YouCompleteMe'
Plugin 'scrooloose/syntastic'
Plugin 'nvie/vim-flake8'
Plugin 'tmhedberg/SimpylFold'
Plugin 'nvie/vim-flake8'
" Add all your plugins here (note older versions of Vundle used Bundle instead of Plugin)


" All of your Plugins must be added before the following line
call vundle#end()            " required
filetype plugin indent on    " required

nnoremap <C-J> <C-W><C-J>
nnoremap <C-K> <C-W><C-K>
nnoremap <C-L> <C-W><C-L>
nnoremap <C-H> <C-W><C-H>

" Disabling arrow keys
nnoremap <Up> <NOP>
nnoremap <Down> <NOP>
nnoremap <Left> <NOP>
nnoremap <Right> <NOP>

inoremap <Up> <NOP>
inoremap <Down> <NOP>
inoremap <Left> <NOP>
inoremap <Right> <NOP>

nmap , $p
"SimplyFold configuration
set foldmethod=indent
set foldlevel=99
nnoremap <space>f za 
let g:SimpylFold_docstring_preview=1

"YouCompleteMe configuration  
let g:ycm_autoclose_preview_window_after_completion=1
map <space>g  :YcmCompleter GoToDefinitionElseDeclaration<CR>
highlight Pmenu ctermfg=7  ctermbg=9

"GOTO definition
"python with virtualenv support
py << EOF
import os
import sys
if 'VIRTUAL_ENV' in os.environ:
  project_base_dir = os.environ['VIRTUAL_ENV']
  activate_this = os.path.join(project_base_dir, 'bin/activate_this.py')
  execfile(activate_this, dict(__file__=activate_this))
EOF


"Parenthases color matching
highlight MatchParen ctermfg=none ctermbg=Green ctermfg=Red

"setttings for Python files
let python_highlight_all=1
syntax on

au BufNewFile,BufRead *.py
	set tabstop=8 softtabstop=0 expandtab shiftwidth=4 smarttab
	set textwidth=79
	set fileformat=unix
	set number
	set wrap
	set encoding=utf-8

"settings for JavaScript, HTML and CSS files
au BufNewFile,BufRead *.js, *.html
	set tabstop=2
	set softtabstop=2
	set shiftwidth=2

"System clipboard
set clipboard=unnamed
