def cannons_ready(gunners):
    a = map(lambda x: True if x == 'aye' else False, list(gunners.values()))
    ready = True
    for x in a:
        ready = ready and x
    return 'Fire!' if ready else 'Shiver me timbers!'
