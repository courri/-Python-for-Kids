def spaceship_building(cans):
    total_cans = 0
    for week in range(1,53):
        total_cans = total_cans + cans
        print('Week %s = %s cans' % (week, total_cans))
        
spaceship_building(2)

spaceship_building(13)