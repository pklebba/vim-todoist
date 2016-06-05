import todoist
import vim

def get_tasks():
    return "ToDo"


def get_projects():

    sync = get_sync()
    if sync:
        print "===== My Projects ====="

        for project in sync['projects']:
            print "-> {}".format(project['name'])

        print "======================="

def get_api():
    token_exists = int(vim.eval('exists("g:todoist_token")'))

    if token_exists:
        token = vim.eval('g:todoist_token')
        return todoist.TodoistAPI(token)
    else:
        print "To use vim-todoist, you must type your Token API in .vimrc. Please type: let g:todoist_token = 'YOUR_TOKEN'"
        return 0

def get_sync():
    api = get_api()

    if api:
        return api.sync()

    return 0
