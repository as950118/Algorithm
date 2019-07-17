x,y,z = map(int, input().split())
ret = x//z + y//z
hi = 0
mod_x = x%z
mod_y = y%z
if not mod_x or not mod_y:
    pass
else:
    mod_x_z = z-mod_x
    mod_y_z = z-mod_y
    if mod_x+mod_y < z:
        hi = 0
    elif mod_x_z<mod_y_z:
        ret += 1
        hi = mod_x_z
    else:
        ret += 1
        hi = mod_y_z


print(ret, hi)