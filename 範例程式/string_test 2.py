my_str = '''A long time ago in a galaxy far, far away....
STAR WARS
Episode IV
A NEW HOPE
It is a period of civil war. Rebel spaceships, striking from a hidden base, have won their first victory against the evil Galactic Empire.
During the battle, Rebel spies managed to steal secret plans to the Empire's ultimate weapon, the DEATH STAR, an armored space station with enough power to destroy an entire planet.
Pursued by the Empire's sinister agents, Princess Leia races home aboard her starship, custodian of the stolen plans that can save her people and restore freedom to the galaxy....'''
print(my_str)
print(my_str.find("Leia"))    # 尋找莉莉公主再第幾個字串
print(my_str.count(" ")+my_str.count("\n")+1)    # 計算文章內出現單字數量