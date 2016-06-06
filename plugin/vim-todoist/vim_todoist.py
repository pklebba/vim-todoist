import todoist
import vim

def get_tasks():
    sync = get_sync()
    if sync:
        print "===== Tasks To Do ====="

        for task in sync['items']:
            print "-> {}".format(task['content'].encode('utf-8'))

        print "======================="


def get_completed_tasks():
    api = get_api()

    if api:
        tasks = api.get_all_completed_items()

        print "===== Completed Tasks ====="
        for task in tasks['items']:
            print "[{}] -> {}".format(task['completed_date'], task['content'].encode('utf-8'))

        print "==========================="
        

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
