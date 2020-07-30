set number
set termguicolors
set autoindent
set showmode
set showcmd
set wrap
set encoding=utf-8

set tabstop=4
set shiftwidth=4
set softtabstop=4
set expandtab
set smarttab


call plug#begin()
Plug 'sainnhe/vim-color-forest-night'
Plug 'vim-airline/vim-airline-themes'
Plug 'vim-airline/vim-airline'
Plug 'itchyny/lightline.vim'
call plug#end()

let g:forest_night_enable_italic = 1
let g:forest_night_disable_italic_comment = 1
let g:forest_night_cursor = 'red'

let g:airline_theme = 'forest_night'

let g:lightline = {'colorscheme' : 'forest_night'}
colorscheme forest-night
