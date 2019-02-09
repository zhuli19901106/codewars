def any_arrows(arrows):
    for arrow in arrows:
        if not ('damaged' in arrow and arrow['damaged']):
            return True
    return False
    