# http://www.careercup.com/question?id=15556758

cache = {}
def probability_of_alive(size, x, y, steps):
    # Handle some base cases
    p = 0
    if x < 0 or y < 0 or x >= size or y >= size:
        # Outside the island, im dead
        p = 0
    elif steps < 1:
        # No more steps, im safe
        p = 1
    else:
        for ox in (-1, 1):
            for oy in (-1, 1):
                nx, ny = x + ox, y + oy
                if cache.has_key((nx, ny)):
                    q = cache[(nx,ny)]
                else:
                    q = probability_of_alive(size, nx, ny, steps - 1)
                p += q / 4.0

    cache[(x,y)] = p
    return p






print probability_of_alive(20, 5, 4, 8)