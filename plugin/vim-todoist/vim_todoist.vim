" --------------------------------
" Add our plugin to the path
" --------------------------------
python import sys
python import vim
python sys.path.append(vim.eval('expand("<sfile>:h")'))
python import vim_todoist

" --------------------------------
"  Function(s)
" --------------------------------
function! GetTasks()
python vim_todoist.get_tasks()
endfunction

function! GetProjects()
python vim_todoist.get_projects()
endfunction

" --------------------------------
"  Expose our commands to the user
" --------------------------------
command! ToDo call GetTasks()
command! ToDoProjects call GetProjects()
