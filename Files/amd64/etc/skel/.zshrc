alias cls='clear'
setopt prompt_subst
setopt INTERACTIVE_COMMENTS
PROMPT="%F{8}┌── %F{6}%*, %D{%d/%m/%Y}%f %F{8}|%f %F{2}%n@%m%f: %F{3}%~%f 
%F{8}|%f
%F{8}└─> %f"
HISTFILE=~/.zsh_history
HISTSIZE=5000
SAVEHIST=5000
setopt HIST_IGNORE_DUPS     # Não grava comandos repetidos seguidos
setopt HIST_IGNORE_SPACE    # Não grava comandos que começam com espaço (útil para senhas)