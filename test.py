from packages import login_required


@login_required
def login(name):
    name = 'mohamed'
    print(name)
login('ali')