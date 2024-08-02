import pygame

def bulbasaur_back():
    b = pygame.Surface((80,80))
    b.fill ((255,0,0))
    pygame.draw.polygon(b, (100,200,200), [(11, 50), (9, 64), (12, 74), (22, 73), (24, 67), (33, 68), (36, 73), (44, 73), (43, 67), (49, 64), (52, 68), (61, 68), (60, 54), (66, 49), (66, 42), (65, 37), (60, 31), (59, 25), (58, 23), (54, 24), (50, 24)])
    pygame.draw.polygon(b, (100,200,100),[(20, 9), (21, 14), (18, 20), (15, 25), (11, 28), (7, 33), (6, 39), (6, 44), (9, 49), (13, 52), (19, 52), (22, 51), (25, 47), (28, 48), (32, 46), (36, 44), (38, 41), (39, 38), (43, 36), (46, 34), (47, 29), (48, 26), (48, 21), (47, 16), (44, 12), (39, 10), (33, 9), (30, 7), (27, 6), (22, 6)])
    pygame.draw.polygon(b, (100,200,100),[(8, 31), (17, 17), (18, 8), (20, 8), (22, 9), (24, 12), (23, 19)])
    pygame.draw.polygon(b, (26,145,115),[(43, 67), (43, 59), (52, 55), (49, 64)])
    pygame.draw.polygon(b, (26,145,115),[(33, 68), (32, 63), (30, 64), (25, 65), (23, 64), (22, 64), (20, 71), (20, 72), (20, 72), (20, 73), (19, 73), (20, 73), (22, 72), (25, 68), (33, 69)])
    pygame.draw.polygon(b, (26,145,115),[(60, 53), (60, 48), (66, 49)])
    b.set_colorkey((255,0,0))
    return b

def bulbasaur_face():
    b = pygame.Surface((80,80))
    b.fill ((255,0,0))
    pygame.draw.polygon(b, (100,200,200),[(21, 40), (26, 32), (10, 31)])
    pygame.draw.polygon(b, (100,200,100),[(19, 36), (24, 39), (41, 33), (56, 38), (60, 40), (65, 36), (67, 22), (64, 15), (45, 6), (42, 6), (42, 3), (38, 2), (37, 6), (24, 10), (13, 26)])
    pygame.draw.polygon(b, (100,200,200),[(10, 30), (21, 39), (41, 32), (47, 35), (55, 29), (57, 32), (58, 38), (64, 43), (67, 52), (67, 57), (66, 60), (69, 69), (62, 70), (61, 74), (53, 75), (51, 68), (47, 65), (42, 66), (35, 65), (26, 66), (21, 66), (16, 70), (13, 73), (6, 73), (7, 63), (10, 56), (9, 51), (12, 44)])
    pygame.draw.polygon(b, (255,255,255),[(15, 44), (19, 53), (13, 53), (13, 46)])
    pygame.draw.polygon(b, (255,255,255),[(46, 50), (52, 49), (49, 41), (44, 49), (44, 50)])
    pygame.draw.polygon(b, (200,50,50),[(16, 46), (15, 53), (19, 53)])
    pygame.draw.polygon(b, (200,50,50),[(47, 44), (49, 50), (44, 51), (44, 48)])
    pygame.draw.polygon(b, (200,50,50),[(13, 58), (25, 59), (31, 60), (34, 58), (48, 58), (45, 60), (32, 63), (29, 63), (26, 64), (21, 62)])
    pygame.draw.polygon(b, (255,255,255),[(20, 59), (21, 60), (23, 58)])
    pygame.draw.polygon(b, (255,255,255),[(38, 58), (40, 59), (41, 58)])
    pygame.draw.polygon(b, (26,145,115),[(12, 73), (18, 65), (21, 66), (14, 73)])
    pygame.draw.polygon(b, (26,145,115),[(47, 66), (51, 69), (51, 65)])
    pygame.draw.polygon(b, (50,150,50),[(23, 38), (25, 33), (39, 29), (50, 31), (51, 32), (49, 35), (41, 33), (22, 39), (23, 37), (24, 36),(18,33)])
    pygame.draw.polygon(b, (50,150,50), [(18,33),(27,33),(20,39)])
    pygame.draw.polygon(b, (50,150,50),[(57, 34), (63, 37), (60, 40), (59, 39), (58, 39)])
    pygame.draw.polygon(b, (50,150,50),[(40, 7), (37, 18), (38, 25), (37, 17)])
    pygame.draw.polygon(b, (50,150,50),[(62, 70), (61, 63), (62, 64)])
    b.set_colorkey((255,0,0))
    return b

def pikachu_back():
    b = pygame.Surface((80,80))
    b.fill ((0,255,255))
    pygame.draw.polygon(b, (247,222,38) ,[(6, 13), (11, 13), (15, 14), (17, 15), (20, 17), (22, 19), (24, 20), (26, 18), (30, 18), (32, 18), (35, 18), (39, 18), (42, 18), (43, 20), (44, 20), (46, 18), (49, 17), (51, 16), (54, 15), (59, 15), (64, 14), (67, 15), (65, 17), (62, 19), (60, 20), (57, 22), (54, 23), (51, 23), (49, 23), (48, 23), (46, 24), (49, 23), (51, 25), (52, 26), (52, 28), (52, 29), (52, 31), (53, 34), (54, 36), (54, 37), (54, 39), (53, 41), (52, 44), (55, 46), (56, 48), (58, 52), (57, 55), (56, 57), (55, 57), (58, 62), (58, 64), (58, 67), (56, 70), (54, 72), (53, 74), (47, 74), (43, 74), (34, 75), (29, 74), (24, 74), (22, 74), (17, 69), (15, 62), (15, 50), (17, 46), (2, 44), (1, 30), (19, 35), (17, 29), (18, 26), (19, 24), (13, 21), (8, 17), (5, 13)])
    pygame.draw.polygon(b, (0,0,0) ,[(13, 13), (14, 18), (14, 22), (7, 16), (5, 12), (12, 13)])
    pygame.draw.polygon(b, (0,0,0) ,[(59, 15), (59, 18), (57, 21), (64, 19), (67, 14), (67, 14)])
    pygame.draw.polygon(b, (229,50,37) ,[(53, 34), (52, 38), (53, 41), (54, 38)])
    pygame.draw.polygon(b, (114,53,36) ,[(15, 51), (28, 50), (41, 51), (46, 54), (15, 54)])
    pygame.draw.polygon(b, (114,53,36) ,[(15, 60), (30, 60), (47, 62), (47, 63), (15, 63)])
    pygame.draw.polygon(b, (247,222,38) ,[(22, 74), (22, 76), (27, 77), (32, 77), (32, 75)])
    pygame.draw.polygon(b, (247,222,38) ,[(46, 74), (49, 76), (55, 76), (60, 75), (60, 73), (59, 73)])
    pygame.draw.polygon(b, (247,222,38) ,[(1, 30), (32, 40), (27, 53), (35, 56), (33, 62), (38, 63), (36, 68), (35, 64), (30, 62), (30, 57), (22, 55), (21, 47), (2, 44)])
    pygame.draw.polygon(b, (114,53,36) ,[(36, 68), (35, 64), (30, 62), (30, 59), (31, 60), (32, 59), (33, 59), (34, 59), (34, 62), (38, 63)])
    pygame.draw.polygon(b, (247,222,38) ,[(26, 18), (30, 16), (32, 15), (35, 16), (37, 16), (40, 17), (42, 18)])
    pygame.draw.polygon(b, (0,0,0) ,[(56, 57), (53, 52), (54, 50)])
    pygame.draw.polygon(b, (0,0,0) ,[(34, 60), (35, 56), (34, 60)])
    pygame.draw.polygon(b, (0,0,0) ,[(35, 56), (27, 53), (35, 56)])
    pygame.draw.polygon(b, (0,0,0) ,[(32, 40), (27, 53), (32, 40)])
    pygame.draw.polygon(b, (0,0,0) ,[(32, 39), (32, 40), (19, 35), (32, 40)])
    pygame.draw.polygon(b, (0,0,0) ,[(17, 46), (21, 47), (17, 46)])
    pygame.draw.polygon(b, (0,0,0) ,[(21, 46), (22, 54), (21, 47)])
    pygame.draw.polygon(b, (0,0,0) ,[(22, 55), (30, 57), (22, 55)])
    pygame.draw.polygon(b, (0,0,0) ,[(30, 57), (30, 60), (30, 57)])
    pygame.draw.polygon(b, (0,0,0) ,[(23, 74), (32, 75), (22, 74)])
    pygame.draw.polygon(b, (0,0,0) ,[(45, 74), (52, 74), (46, 74)])
    b.set_colorkey((0,255,255))
    return b

def pikachu_front():
    b = pygame.Surface((100,100))
    b.fill ((0,255,255)) #
    pygame.draw.polygon(b,(247,222,38),[(7, 13), (15, 13), (20, 13), (31, 16), (35, 15), (40, 14), (47, 14), (50, 16), (53, 10), (57, 6), (61, 3), (65, 1), (67, 1), (67, 4), (64, 7), (62, 10), (58, 14), (56, 17), (53, 19), (54, 21), (55, 25), (54, 29), (53, 32), (53, 38), (53, 41), (54, 46), (55, 51), (55, 57), (56, 64), (55, 67), (52, 70), (48, 74), (44, 74), (37, 74), (31, 74), (26, 71), (23, 67), (22, 60), (23, 51), (25, 44), (25, 41), (26, 41), (23, 37), (21, 29), (23, 26), (25, 22), (27, 19), (27, 19), (18, 17), (9, 16), (7, 15), (6, 14)])
    pygame.draw.polygon(b,(247,222,38),[(56, 60), (56, 64), (69, 53), (63, 47), (72, 41), (64, 35), (74, 25), (64, 15), (50, 30), (60, 38), (54, 47), (64, 54)])
    pygame.draw.polygon(b,(247,222,38),[(30, 73), (26, 72), (21, 75), (20, 77), (22, 78), (24, 78), (28, 76), (29, 75)])
    pygame.draw.polygon(b,(247,222,38),[(46, 74), (50, 72), (51, 75), (50, 78), (49, 79), (47, 77), (46, 75)])
    pygame.draw.polygon(b,(0,0,0),[(26, 72), (30, 73), (26, 71)])
    pygame.draw.polygon(b,(0,0,0),[(30, 73), (27, 72), (30, 74)])
    pygame.draw.polygon(b,(0,0,0),[(45, 74), (50, 73), (45, 74), (51, 72), (45, 74)])
    pygame.draw.polygon(b,(0,0,0),[(50, 72), (45, 74), (50, 73)])
    pygame.draw.polygon(b,(0,0,0),[(23, 50), (26, 59), (26, 61), (27, 61), (27, 61), (28, 61), (29, 61), (30, 62), (30, 60), (30, 59), (30, 54), (29, 49), (30, 55), (30, 56), (29, 59), (30, 61), (29, 61), (28, 61), (28, 60), (27, 61), (26, 60), (26, 59)])
    pygame.draw.polygon(b,(0,0,0),[(41, 49), (39, 60), (38, 61), (40, 61), (41, 62), (42, 61), (43, 61), (44, 60), (44, 49), (44, 58), (43, 60), (44, 61), (44, 61), (43, 60), (41, 61), (40, 60), (39, 60)])
    pygame.draw.polygon(b,(0,0,0),[(48, 76), (48, 78), (48, 76)])
    pygame.draw.polygon(b,(0,0,0),[(50, 76), (50, 78), (51, 78)])
    pygame.draw.polygon(b,(0,0,0),[(22, 78), (24, 76), (22, 78)])
    pygame.draw.polygon(b,(0,0,0),[(21, 77), (24, 75), (21, 77)])
    pygame.draw.polygon(b,(0,0,0),[(60, 3), (62, 4), (63, 5), (63, 7), (63, 9), (67, 4), (68, 1), (67, 0), (65, 1), (64, 1), (62, 2), (61, 2)])
    pygame.draw.polygon(b,(0,0,0),[(12, 13), (12, 13), (13, 15), (14, 15), (15, 16), (16, 17), (13, 17), (9, 16), (7, 15), (7, 14), (6, 14), (6, 13), (7, 13), (8, 12), (12, 13)])
    pygame.draw.polygon(b,(0,0,0),[(55, 24), (54, 29), (53, 33), (53, 35)])
    pygame.draw.polygon(b,(0,0,0),[(56, 59), (56, 62), (56, 64)])
    pygame.draw.polygon(b,(0,0,0),[(31, 22), (29, 23), (30, 27), (32, 27), (34, 26), (35, 25), (35, 23), (33, 22)])
    pygame.draw.polygon(b,(0,0,0),[(46, 22), (44, 24), (43, 26), (46, 27), (47, 27), (48, 26), (48, 24), (48, 23), (46, 22), (46, 22), (47, 22)])
    pygame.draw.polygon(b,(0,0,0),[(38, 29), (39, 29), (39, 30)])
    pygame.draw.polygon(b,(0,0,0),[(35, 32), (36, 33), (37, 33), (39, 32), (40, 33), (41, 33), (42, 32), (41, 33), (39, 32), (37, 33)])
    pygame.draw.polygon(b,(200,30,30),[(22, 28), (23, 29), (23, 32), (22, 33), (22, 33), (21, 32), (21, 30), (21, 28), (22, 28)])
    pygame.draw.polygon(b,(200,30,30),[(52, 28), (50, 29), (50, 31), (50, 31), (52, 31), (53, 31), (53, 30), (54, 29), (53, 28)])
    pygame.draw.polygon(b,(255,255,255),[(32, 23), (32, 24), (33, 24), (34, 23), (33, 23)])
    pygame.draw.polygon(b,(255,255,255),[(45, 23), (46, 24), (45, 24), (45, 24), (44, 24), (44, 24), (45, 23)])
    pygame.draw.polygon(b,(114,53,36),[(55, 50), (51, 53), (51, 54), (53, 54), (55, 53), (55, 53), (56, 53)])
    pygame.draw.polygon(b,(114,53,36),[(55, 55), (53, 56), (52, 57), (53, 58), (55, 57)])
    pygame.draw.polygon(b,(114,53,36),[(56, 59), (56, 65), (61, 60), (59, 59), (60, 59), (58, 59), (59, 58), (56, 60)])
    b.set_colorkey((0,255,255))
    return b


def trainer_front():
    b = pygame.Surface((100,100))
    b.fill ((0,255,0)) #(230,190,182)
    pygame.draw.polygon(b, (232,108,111),[(37, 19), (44, 16), (53, 15), (58, 16), (61, 22), (61, 26), (59, 27), (56, 28), (48, 28), (42, 27), (38, 28), (36, 28), (36, 22)])
    pygame.draw.polygon(b, (176,56,64),[(58, 28), (54, 24), (48, 22), (43, 23), (39, 25), (36, 27), (32, 28), (32, 33), (34, 35)])
    pygame.draw.polygon(b, (253,199,192),[(41, 33), (44, 38), (49, 42), (54, 42), (57, 39), (58, 36), (58, 32), (60, 32), (61, 29), (60, 27), (60, 27), (60, 26)])
    pygame.draw.polygon(b, (164,106,98),[(49, 30), (50, 34), (49, 37), (50, 38), (52, 42), (49, 42), (44, 39), (41, 32)])
    pygame.draw.polygon(b, (0,0,0),[(54, 29), (54, 31), (51, 32), (52, 30)])
    pygame.draw.polygon(b, (232,108,111),[(44, 40), (41, 42), (38, 47), (38, 52), (39, 55), (42, 55), (46, 41)])
    pygame.draw.polygon(b, (232,108,111),[(52, 42), (50, 54), (58, 50), (62, 47), (62, 43), (62, 41), (58, 40), (56, 41)])
    pygame.draw.polygon(b, (176,56,64),[(50, 54), (48, 64), (60, 65), (64, 63), (64, 58), (66, 60), (68, 64), (71, 65), (73, 65), (74, 67), (76, 66), (75, 63), (78, 60), (78, 57), (75, 52), (70, 48), (65, 44), (62, 42), (61, 48), (55, 51)])
    pygame.draw.polygon(b, (176,56,64),[(42, 55), (40, 65), (34, 62), (38, 47), (38, 51), (38, 53), (39, 54), (40, 55)])
    pygame.draw.polygon(b, (0,0,0),[(46, 42), (47, 44), (48, 45), (50, 44), (51, 44), (51, 52), (49, 62), (41, 61), (41, 61), (42, 54), (43, 47)])
    pygame.draw.polygon(b, (0,0,0),[(45, 42), (46, 40), (49, 42), (52, 42), (52, 44), (51, 45), (49, 44), (48, 45),(46, 45)])#
    pygame.draw.polygon(b, (59,73,100),[(61, 64), (68, 82), (64, 90), (64, 92), (60, 92), (59, 89), (55, 89), (54, 85), (51, 72), (44, 86), (41, 87), (41, 89), (38, 88), (38, 86), (36, 84), (38, 74), (38, 68), (38, 64), (40, 65), (40, 62), (49, 63), (49, 64), (54, 64), (56, 65)])
    pygame.draw.polygon(b, (232,108,111),[(50, 61), (47, 60), (46, 62), (41, 60), (41, 63), (49, 64)])
    pygame.draw.polygon(b, (253,199,192),[(34, 62), (34, 68), (38, 67), (38, 66), (38, 64)])
    pygame.draw.polygon(b, (176,56,64),[(34, 66), (27, 59), (31, 54), (30, 50), (38, 46), (35, 57), (33, 62), (34, 62)])
    pygame.draw.polygon(b, (253,199,192),[(76, 66), (76, 70), (73, 72), (70, 70), (74, 67)])
    pygame.draw.polygon(b, (253,199,192),[(71, 69), (70, 69), (76, 71), (73, 72), (70, 70)])
    pygame.draw.polygon(b, (27,30,40),[(60, 92), (62, 96), (67, 96), (67, 93), (64, 91)])
    pygame.draw.polygon(b, (27,30,40),[(41, 89), (41, 90), (44, 92), (44, 94), (34, 94), (34, 92), (37, 90), (38, 88), (41, 88)])
    b.set_colorkey((0,255,0))
    return b

def overworld_item():
    b = pygame.Surface((50,50))
    b.fill ((0,255,0))
    pygame.draw.polygon(b, (200,30,30),[(5, 16), (4, 44), (43, 44), (43, 16)])
    pygame.draw.polygon(b, (255,255,255),[(21, 16), (20, 28), (5, 29), (5, 32), (21, 33), (21, 44), (21, 44), (24, 44), (24, 33), (43, 33), (43, 29), (25, 28), (25, 16), (25, 16)])
    pygame.draw.polygon(b, (255,255,255),[(21, 16), (15, 14), (11, 12), (8, 8), (9, 5), (11, 4), (13, 4), (16, 6), (19, 8), (21, 12), (23, 14), (24, 12), (27, 8), (30, 6), (33, 4), (34, 4), (35, 6), (35, 8), (34, 9), (31, 11), (30, 12), (26, 14), (25, 16)])
    pygame.draw.polygon(b, (0,255,0),[(20, 14), (16, 8), (13, 7), (11, 6), (11, 9), (13, 11), (16, 13), (20, 14)])
    pygame.draw.polygon(b, (0,255,0),[(24, 14), (28, 9), (32, 6), (33, 6), (34, 8), (30, 11), (25, 14)])
    b.set_colorkey((0,255,0))
    return b

def player_right():
    b = pygame.Surface((50,50))
    b.fill ((0,255,0))
    pygame.draw.polygon(b,(176,56,64),[(17, 15), (37, 16), (37, 12), (33, 12), (25, 5), (20, 4), (16, 5), (14, 8), (13, 14), (13, 16)])
    pygame.draw.polygon(b,(236,193,104),[(15, 15), (14, 20), (18, 24), (23, 25), (26, 22), (26, 18), (26, 15)])
    pygame.draw.polygon(b,(228,213,183),[(23, 25), (26, 22), (26, 16), (35, 15), (34, 20), (33, 23), (30, 24)])
    pygame.draw.polygon(b,(128,64,0),[(21, 25), (20, 34), (12, 38), (3, 34), (5, 26), (11, 22)])
    pygame.draw.polygon(b,(176,56,64),[(28, 25), (28, 37), (20, 37), (20, 24)])
    pygame.draw.polygon(b,(59,73,100),[(20, 37), (21, 48), (28, 48), (28, 36)])
    pygame.draw.polygon(b,(0,0,0),[(21, 48), (23, 45), (27, 45), (29, 46), (29, 48), (21, 48)])
    b.set_colorkey((0,255,0))
    return b

def player_left():
    b = pygame.Surface((50,50))
    b.fill ((0,255,0))
    pygame.draw.polygon(b,(176,56,64),[(17, 15), (37, 16), (37, 12), (33, 12), (25, 5), (20, 4), (16, 5), (14, 8), (13, 14), (13, 16)])
    pygame.draw.polygon(b,(236,193,104),[(15, 15), (14, 20), (18, 24), (23, 25), (26, 22), (26, 18), (26, 15)])
    pygame.draw.polygon(b,(228,213,183),[(23, 25), (26, 22), (26, 16), (35, 15), (34, 20), (33, 23), (30, 24)])
    pygame.draw.polygon(b,(128,64,0),[(21, 25), (20, 34), (12, 38), (3, 34), (5, 26), (11, 22)])
    pygame.draw.polygon(b,(176,56,64),[(28, 25), (28, 37), (20, 37), (20, 24)])
    pygame.draw.polygon(b,(59,73,100),[(20, 37), (21, 48), (28, 48), (28, 36)])
    pygame.draw.polygon(b,(0,0,0),[(21, 48), (23, 45), (27, 45), (29, 46), (29, 48), (21, 48)])
    b.set_colorkey((0,255,0))
    flipped_b = pygame.transform.flip(b, True, False)
    return flipped_b

def player_up():
    b = pygame.Surface((50,50))
    b.fill ((0,255,0))
    pygame.draw.polygon(b,(176,56,64),[(16, 9), (13, 16), (16, 20), (29, 21), (32, 14), (29, 9)])
    pygame.draw.polygon(b,(236,193,104),[(17, 20), (17, 25), (30, 25), (29, 20)])
    pygame.draw.polygon(b,(128,64,0),[(17, 25), (14, 27), (10, 32), (14, 38), (33, 39), (35, 31), (33, 26), (30, 25)])
    pygame.draw.polygon(b,(176,56,64),[(12, 29), (7, 28), (4, 34), (6, 40), (10, 32)])
    pygame.draw.polygon(b,(176,56,64),[(34, 28), (38, 27), (41, 38), (39, 39)])
    pygame.draw.polygon(b,(59,73,100),[(14, 38), (14, 48), (20, 48), (24, 43), (28, 48), (34, 48), (33, 38)])
    b.set_colorkey((0,255,0))
    return b

def player_down():
    b = pygame.Surface((50,50))
    b.fill ((0,255,0))
    pygame.draw.polygon(b,(176,56,64),[(15, 7), (14, 14), (32, 14), (31, 7), (27, 6), (18, 6)])
    pygame.draw.polygon(b,(228,213,183),[(14, 14), (16, 22), (21, 27), (26, 26), (30, 21), (30, 14)])
    pygame.draw.polygon(b,(176,56,64),[(19, 25), (12, 26), (10, 30), (10, 37), (13, 37), (16, 30), (18, 31), (19, 39), (30, 38), (30, 30), (32, 29), (34, 34), (34, 37), (38, 37), (38, 29), (34, 25), (30, 24), (24, 26)])
    pygame.draw.polygon(b,(59,73,100),[(19, 38), (18, 49), (23, 48), (26, 43), (29, 49), (32, 48), (30, 38)])
    b.set_colorkey((0,255,0))
    return b


def vendor_down():
    b = pygame.Surface((50,50))
    b.fill ((0,255,0))
    pygame.draw.polygon(b,(115,251,253),[(15, 7), (14, 14), (32, 14), (31, 7), (27, 6), (18, 6)])
    pygame.draw.polygon(b,(228,213,183),[(14, 14), (16, 22), (21, 27), (26, 26), (30, 21), (30, 14)])
    pygame.draw.polygon(b,(176,56,64),[(19, 25), (12, 26), (10, 30), (10, 37), (13, 37), (16, 30), (18, 31), (19, 39), (30, 38), (30, 30), (32, 29), (34, 34), (34, 37), (38, 37), (38, 29), (34, 25), (30, 24), (24, 26)])
    pygame.draw.polygon(b,(59,73,100),[(19, 38), (18, 49), (23, 48), (26, 43), (29, 49), (32, 48), (30, 38)])
    b.set_colorkey((0,255,0))
    return b

def trainer_back():
    b = pygame.Surface((100,100))
    b.fill ((0,255,0)) #
    pygame.draw.polygon(b, (176,56,64),[(22, 36), (56, 34), (70, 28), (68, 24), (60, 24), (54, 16), (50, 10), (40, 6), (26, 5), (16, 8), (10, 16), (8, 22), (10, 28), (13, 32)])
    pygame.draw.polygon(b, (228,213,183),[(15, 32), (13, 43), (24, 52), (35, 58), (48, 56), (58, 56), (65, 52), (64, 44), (61, 39), (59, 34), (58, 33)])
    pygame.draw.polygon(b, (236,193,104),[(41, 32), (43, 47), (35, 54), (25, 54), (16, 45), (13, 42), (15, 32)])
    pygame.draw.polygon(b, (176,56,64),[(57, 56), (65, 58), (69, 63), (72, 68), (75, 72), (76, 68), (79, 65), (82, 66), (84, 69), (83, 74), (82, 75), (81, 78), (77, 79), (76, 80), (74, 81), (70, 81), (68, 80), (66, 80), (64, 79), (61, 76), (58, 72), (57, 71), (55, 69), (54, 67), (52, 62), (47, 56)])
    pygame.draw.polygon(b, (176,56,64),[(61, 77), (54, 67), (53, 80), (46, 92), (30, 92), (28, 100), (67, 99), (67, 99), (68, 100)])
    pygame.draw.polygon(b, (176,56,64),[(24, 5), (43, 28), (58, 33), (13, 32), (10, 30), (8, 25), (8, 20), (9, 16), (13, 10), (17, 6)])
    pygame.draw.polygon(b, (128,64,0),[(25, 53), (16, 56), (5, 65), (5, 74), (7, 79), (8, 85), (10, 89), (15, 92), (21, 94), (30, 96), (39, 96), (45, 96), (51, 92), (53, 85), (55, 78), (55, 71), (54, 65), (51, 60), (46, 54)])
    pygame.draw.polygon(b, (0,0,0),[(5, 69), (20, 70), (39, 72), (42, 92), (43, 92), (41, 72), (47, 56), (46, 54), (40, 71), (5, 68)])
    pygame.draw.polygon(b, (0,0,0),[(20, 70), (20, 67), (25, 68), (24, 72), (20, 72)])
    b.set_colorkey((0,255,0))
    return b