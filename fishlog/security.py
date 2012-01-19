USERS = {'member':'member',
          'admin':'admin'}
GROUPS = {'member':['group:members']}

def groupfinder(userid, request):
    if userid in USERS:
        return GROUPS.get(userid, [])
