# 
import pygame
import sprites
pygame.mixer.init()
pygame.mixer.music.load("awake.mp3")
pygame.mixer.music.play(-1)

sound_effect1 = pygame.mixer.Sound("kefka.wav")
item_sound = pygame.mixer.Sound("item.mp3")

door_sound = pygame.mixer.Sound("door.mp3")

heal_sound =pygame.mixer.Sound("heal.wav")
pygame.mixer.music.set_volume(0.7)
pygame.mixer.music.play()

pygame.init()
screen = pygame.display.set_mode((500,500))
font = pygame.font.Font('freesansbold.ttf', 32)
font2 = pygame.font.Font('freesansbold.ttf', 28)
font3 = pygame.font.Font('freesansbold.ttf', 24)
font4 = pygame.font.Font('freesansbold.ttf', 34)
font5 = pygame.font.Font('freesansbold.ttf', 80)
font6 = pygame.font.Font('freesansbold.ttf', 16)
x = 500
y = 500

focus = []

def ui_string(ref,x,y,font_selection,color): #target is image, ref is string
        target = image()
        target.reel = [(x,y)]
        x,y = font_selection.size(ref)
        target.img = pygame.Surface((x,y))
        name = font_selection.render(ref, True, (255,237,63))
        target.img.fill((0,0,0))
        target.img.blit(name,(0,0))
        return target

class title_page:
    def __init__ (self):
        self.pointer = None
        x,y = font5.size('Pygamon')
        self.title = ui_string("Pygamon",((500-x)/2),50,font5,(255,237,63))
        
        x,y = font3.size("By Nicholas Zettel")
        self.author = ui_string("By Nicholas Zettel",((500-x)/2),150,font3,(255,237,63))
        
        x,y = font6.size('Press x')
        self.icon = image()
        self.icon.img = sprites.bulbasaur_face()
        self.icon.reel = [(550-i,220) for i in range (340)]
       
        self.button_map = image()
        self.button_map.reel = [(100,300)]
        self.button_map.img = pygame.Surface((310,190))
        pygame.draw.rect(self.button_map.img,(255,255,255), (250,150,40,40))
        pygame.draw.rect(self.button_map.img,(255,255,255), (200,150,40,40))
        pygame.draw.rect(self.button_map.img,(255,255,255), (150,150,40,40))
        pygame.draw.rect(self.button_map.img,(255,255,255), (200,100,40,40))
        pygame.draw.rect(self.button_map.img,(255,255,255), (20,70,40,40))
        pygame.draw.rect(self.button_map.img,(255,255,255), (70,70,40,40))
        x = font.render("x", True, (0,0,0))
        z = font.render("z", True, (0,0,0))
        pygame.draw.polygon(self.button_map.img,(0,0,0),[(175,185),(160,170),(175,155)])
        pygame.draw.polygon(self.button_map.img,(0,0,0),[(265,185),(280,170),(265,155)])
        pygame.draw.polygon(self.button_map.img,(0,0,0),[(205,165),(235,165),(220,180)])
        pygame.draw.polygon(self.button_map.img,(0,0,0),[(205,125),(235,125),(220,110)])
        self.button_map.img.blit(z,(29,73))
        self.button_map.img.blit(x,(79,73))
        x,y = font3.size("Press x")
        self.prompt = None
        
    def draw (self):
        for i in [self.title,
                  self.author,
                  self.icon,
                  self.prompt,
                  self.button_map]:
            if i:
                i.draw()

        if self.prompt:
            self.prompt.draw()
                
    def new_input (self,event):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:
                    del self.pointer.focus[-1]

def kill_intro_open_overworld():
    global focus
    global overworld
    focus = [overworld]
    
def open_battle(battle):
    global focus
    print (focus)
    focus.append(battle)
    print (focus)

def kill_battle_trainer_won():
    global battle
    global bad
    global focus
    bad = opponent()
    bad.pokemon = [pokemon(),pokemon()]
    bad.pokemon[0].species = "Pikachu"
    bad.pokemon[0].front.img = sprites.pikachu_front()
    bad.pokemon[1].front.img = sprites.bulbasaur_face()
    bad.trainer_sprite.img = sprites.trainer_front()
    pygame.mixer.music.stop()
    pygame.mixer.music.load("awake.mp3")
    pygame.mixer.music.play(-1)
    battle = battle_logic(nick,bad)
    del focus[-1]

    
class portal:
    def __init__ (self,a,b):
        pass

class overworld_logic():
    def __init__ (self):
        global battle
        self.facing = 'right'
        self.state = 0
        item1 = item()
        item1.name = "super potion"
        item1.aid = True
        item1.quantity = 1
        item1.healing = 200
        
        self.player = image()
        self.player.img = pygame.Surface((50,50), pygame.SRCALPHA, 32)
        self.player.img = self.player.img.convert_alpha()
        if self.facing == 'right':
            self.player.img.blit(sprites.player_right(),(0,0))
        elif self.facing == 'left':
            print ('here')
            self.player.img.blit(sprites.player_left(),(0,0))
        elif self.facing == 'up':
            print ('here')
            self.player.img.blit(sprites.player_up(),(0,0))
        elif self.facing == 'down':
            print ('here')
            self.player.img.blit(sprites.player_down(),(0,0))
        
        
        self.item_img = image()
        self.item_img.img = sprites.overworld_item()
        
        self.visuals = visual_logic()
        self.world_bitmap = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                             [0,1,1,1,item1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                             [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                             [0,1,1,1,1,1,1,1,1,1,2,2,2,2,2,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                             [0,1,1,1,1,1,1,1,1,1,3,3,3,3,3,1,1,battle,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                             [0,1,1,1,1,1,1,1,1,1,3,3,3,3,3,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                             [0,1,1,1,1,1,1,1,1,1,3,3,4,3,3,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                             [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                             [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6,7,6,6,6,0,0,0,0],
                             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6,6,6,6,6,0,0,0,0],
                             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6,6,6,6,6,0,0,0,0],
                             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6,6,5,6,6,0,0,0,0]]

        
        self.world = image()
        self.world.img = pygame.Surface((len(self.world_bitmap[0])*50,len(self.world_bitmap)*50))
        
        self.position = (1,1)
        self.update_map()
        #self.world.reel= [(50*self.position[0],50*self.position[1])]
                    
        self.world.reel= [(225-self.position[0]*50,225-self.position[1]*50)]
        #self.visuals.focus.append(self.world)
        
        screen.blit(self.world.img,((225-self.position[0]*50,225-self.position[1]*50)))
        
        
        
#self.world.img.blit(self.item_img.img,(j*50,i*50))
        #future image locations
        
        #image is 80x80

        self.new_position = [0,0]
        self.visuals.focus.append(Text("Welcome to Pygamon."))
        self.visuals.focus[-1].pointer = self.visuals.focus

        self.target = None
    def update_map(self):
        green = (0,200,0)
        black = (0,0,0)
        red = (200,50,50)
        dark_brown = (76,43,32)
        light_brown = (155,103,60)
        self.world.img.fill((0,0,0))
        for i in range (len(self.world_bitmap)):
            for j in range (len(self.world_bitmap[0])):
                if self.world_bitmap[i][j] == 0:
                    pygame.draw.rect(self.world.img, black, (j*50,i*50,50,50))
                elif self.world_bitmap[i][j] == 1:
                    pygame.draw.rect(self.world.img, green, (j*50,i*50,50,50))
                elif self.world_bitmap[i][j] == 2:
                    pygame.draw.rect(self.world.img, dark_brown, (j*50,i*50,50,50))
                elif self.world_bitmap[i][j] == 3 or self.world_bitmap[i][j] == 6:
                    pygame.draw.rect(self.world.img, light_brown, (j*50,i*50,50,50))
                elif type(self.world_bitmap[i][j]) == item:
                    print ('here')
                    pygame.draw.rect(self.world.img, green, (j*50,i*50,50,50))
                    self.world.img.blit(self.item_img.img,(j*50,i*50))
                elif type(self.world_bitmap[i][j]) == battle_logic:
                    pygame.draw.rect(self.world.img, green, (j*50,i*50,50,50))
                    self.world.img.blit(sprites.player_down(),(j*50,i*50))
                elif self.world_bitmap[i][j] == 7:
                    pygame.draw.rect(self.world.img, light_brown, (j*50,i*50,50,50))
                    self.world.img.blit(sprites.vendor_down(),(j*50,i*50))
                    
        self.world.reel= [(225-self.position[0]*50,225-self.position[1]*50)]
        screen.blit(self.world.img,((225-self.position[0]*50,225-self.position[1]*50)))
        print ('here')
        self.player = image()
        self.player.img = pygame.Surface((50,50), pygame.SRCALPHA, 32)
        self.player.img = self.player.img.convert_alpha()
        if self.facing == 'right':
            self.player.img.blit(sprites.player_right(),(0,0))
        elif self.facing == 'left':
            print ('here')
            self.player.img.blit(sprites.player_left(),(0,0))
        elif self.facing == 'up':
            print ('here')
            self.player.img.blit(sprites.player_up(),(0,0))
        elif self.facing == 'down':
            print ('here')
            self.player.img.blit(sprites.player_down(),(0,0))
        self.player.reel = [(225,225)]
        
    def update(self):
        self.world.reel= [(225-self.position[0]*50,225-self.position[1]*50)]
        screen.blit(self.world.img,((225-self.position[0]*50,225-self.position[1]*50)))
        screen.blit(self.player.img,(225,225))
        if self.state == 1:
            if not any(isinstance(i,Text) for i in self.visuals.focus):
                self.state = 0
                print (self.new_position)
                
                open_battle(self.target)
                for i in self.world_bitmap:
                    print (i)
                self.update_map()
        
    def new_input(self,events):
        try:
            self.visuals.focus[-1].new_input(events)
        except:
            for event in events:
                if event.type == pygame.KEYDOWN:
                    movement = (0,0)
                    if event.key == pygame.K_DOWN:
                        self.facing = 'down'
                        movement = (0,1)
                    elif event.key == pygame.K_UP:
                        self.facing = 'up'
                        movement = (0,-1)
                    elif event.key == pygame.K_LEFT:
                        self.facing = 'left'
                        movement = (-1,0)
                    elif event.key == pygame.K_RIGHT:
                        self.facing = 'right'
                        movement = (1,0)
                    elif event.key == pygame.K_x:
                        if self.facing == 'down':
                            self.new_position = [self.position[0] + 0,self.position[1] + 1]
                        elif self.facing == 'up':
                            self.new_position = [self.position[0] + 0,self.position[1] - 1]
                        elif self.facing == 'right':
                            self.new_position = [self.position[0] + 1,self.position[1] + 0]
                        elif self.facing == 'left':
                            self.new_position = [self.position[0] -1 ,self.position[1] + 0]
                        if type(self.world_bitmap[self.new_position[1]][self.new_position[0]]) == item:
                            self.visuals.focus.append(Text("You found a " + self.world_bitmap[self.new_position[1]][self.new_position[0]].name+'!'))
                            pygame.mixer.Sound.play(item_sound)
                            nick.items.append(self.world_bitmap[self.new_position[1]][self.new_position[0]])
                            self.world_bitmap[self.new_position[1]][self.new_position[0]] = 1
                            self.visuals.focus[-1].pointer = self.visuals.focus
                            self.update_map()                     
                        elif type(self.world_bitmap[self.new_position[1]][self.new_position[0]]) == battle_logic:
                            self.state = 1
                            self.target = self.world_bitmap[self.new_position[1]][self.new_position[0]]
                            pygame.mixer.music.stop()
                            pygame.mixer.Sound.play(sound_effect1)
                            self.world_bitmap[self.new_position[1]][self.new_position[0]] = 1
                        elif self.world_bitmap[self.new_position[1]][self.new_position[0]] == 7:
                            self.visuals.focus.append(Text("Let me heal your pokemon"))
                            pygame.mixer.Sound.play(heal_sound)
                            self.visuals.focus[-1].pointer = self.visuals.focus
                            for i in nick.pokemon:
                                i.hp = i.max_hp
                           
                    self.new_position = [self.position[0] + movement[0],self.position[1] + movement[1]]
                    if self.world_bitmap[self.new_position[1]][self.new_position[0]] in [1,6]:
                        self.position = self.new_position
                    elif self.world_bitmap[self.new_position[1]][self.new_position[0]] in [4]:
                        pygame.mixer.Sound.play(door_sound)
                        self.position = [31,15]
                    elif self.world_bitmap[self.new_position[1]][self.new_position[0]] in [5]:
                        pygame.mixer.Sound.play(door_sound)
                        self.position = [12,7]
                    self.update_map()

class intro:
    def __init__ (self):
        self.state = 0
        self.movement_countdown = 340
        self.visuals = visual_logic()
        self.visuals.focus = [title_page()]
        self.visuals.focus[-1].pointer = self.visuals
        
    def new_input(self,events):
        try:
            self.visuals.focus[-1].new_input(events)
        except:
            pass
        
    def update(self):
        if self.state == 0 and self.visuals.movement_countdown == 0 and self.visuals.focus != []:
            if self.visuals.focus[-1].prompt:
                self.visuals.focus[-1].prompt = None
            else:
                x,y = font3.size("Press x")
                self.visuals.focus[-1].prompt = ui_string("Press x",((500-x)/2),320,font3,(255,255,255))
            self.visuals.movement_countdown = 300
        elif self.state == 0 and self.visuals.movement_countdown == 0:
            pass
        if self.visuals.movement_countdown > 0:
            self.visuals.movement_countdown -= 1
        if self.visuals.focus == []:
            global kill_intro_open_overworld
            kill_intro_open_overworld()
            print ('dead')
            del self
    def add_focus(self,new_focus):
        print ('battle visuals is adding a focus')
        self.focus.append(new_focus)

class block:
    def __init__ (self):
        pass
    def new_input(self,events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                print ('blocked')

class d2_menu: # 2 dimensional list
    def __init__ (self):
        self.selection = 0
        self.option1 = None
        self.option2 = None
        self.option3 = None
        self.option4 = None
    def triangle (x,y):
        return (x,y), (x-10,y-10), (x-10,y+10)
    def draw(self):
        x = 500
        y = 500
        pygame.draw.rect(screen,(240,145,47),(0,y-120,x,y))
        #draw text
        screen.blit(self.option1,(280,400))
        screen.blit(self.option2,(395,400))
        screen.blit(self.option3,(280,450))
        screen.blit(self.option4,(395,450))
        #draw triangle
        if self.selection == 2:
                pygame.draw.polygon(screen,(255,255,255),d2_menu.triangle(390,415))
        elif self.selection == 0:
            pygame.draw.polygon(screen,(255,255,255),d2_menu.triangle(275,415))
        elif self.selection == 1:
            pygame.draw.polygon(screen,(255,255,255),d2_menu.triangle(275,465))
        elif self.selection == 3:
            pygame.draw.polygon(screen,(255,255,255),d2_menu.triangle(390,465))        

class battle_menu(d2_menu):
    def __init__ (self):
        super().__init__ ()
        #render text
        self.pointer = None
        self.option1 = font.render("Fight", True, (255,237,63))
        self.option2 = font.render("Pkm", True, (255,237,63))
        self.option3 = font.render("Items", True, (255,237,63))
        self.option4 = font.render("Run", True, (255,237,63))
    def new_input(self,events):
        global battle
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                    if self.selection == 0 or self.selection == 2:
                            self.selection += 1
                    else:
                        self.selection -= 1
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                    if self.selection == 0 or self.selection == 1:
                        self.selection += 2
                    else:
                        self.selection -= 2
                elif event.key == pygame.K_x:
                    print ('x')
                    print (self.selection)
                    if self.selection == 0:
                        print ('hello')
                        print (move_menu)
                        print (battle)
                        xz = move_menu(battle.get_moves())
                        print (battle.focus)
                        battle.add_focus(xz)
                        xz.pointer = self.visuals.focus
                    elif self.selection == 2:
                        battle.add_focus(pokemon_menu(battle.player.pokemon,1))
                    elif self.selection == 1:
                        battle.add_focus(item_menu(battle.player.pokemon,battle.player.items))
                    elif self.selection == 3:
                        if type(battle.opp) == opponent:
                            battle.add_focus(Text("You can't run from a trainer battle!"))
                        else:
                            if battle.opp.level<=battle.player.pokemon[battle.player_current].level:
                                battle.add_focus(Text("Got away safely."))
                                battle.state = 21
                            else:
                                battle.add_focus(Text("Can't escape."))
                                battle.player_went = True
                                battle.state = 20
                        
class move_menu():
    def __init__ (self,contents):
        global battle
        #battle.get_moves():
        self.selection = 0
        self.options = []
        for i in range (len(battle.player.pokemon[battle.player_current].moves)):
            self.options.append(font3.render(str(battle.player.pokemon[battle.player_current].moves[i].name), True, (255,237,63)))
            
    def triangle2 (self,x,y):
        return (x,y), (x-10,y-10), (x-10,y+10)
        
    def draw(self):
        x = 500
        y = 500
        pygame.draw.rect(screen,(240,145,47),(0,y-120,x,y))
        for i in range(len(self.options)):
            screen.blit(self.options[i],(280,385+28*i))
        pygame.draw.polygon(screen,(255,255,255),self.triangle2(275,395+self.selection*28))
            
    def new_input(self,events):
        global battle
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    if self.selection < len(self.options)-1:
                        self.selection += 1
                    else:
                        self.selection = 0
                elif event.key == pygame.K_UP:
                    if self.selection > 0:
                        self.selection -= 1
                    else:
                        self.selection = len(self.options)-1
                elif event.key == pygame.K_x:
                    if battle.player.pokemon[battle.player_current].moves[self.selection].pp > 0:
                        battle.selection = self.selection
                        del battle.visuals.focus[-1]
                        battle.lock_move()
                    else:
                        battle.add_focus(Text("There's no pp left for that move!"))
                elif event.key == pygame.K_z:
                    del battle.visuals.focus[-1]

class pokemon_menu:
    def __init__ (self,pok_list,use):
        self.use = use
        self.pointer = None
        self.options = [font4.render('lvl: '+ str(i.level) + "  " +i.species+ "  hp:" + str(i.hp)+"/"+str(i.max_hp), True, (255,237,63)) for i in pok_list]
        self.selection = 0
        self.choose_msg = font4.render("Which pokemon?", True,(60,237,63))
        self.pok_list = pok_list
  
    def draw(self):
        x = 500
        y = 500
        screen.fill ((0,0,0))
        for i in range(len(self.options)):
            screen.blit(self.options[i],(20,120+60*i))
        pygame.draw.polygon(screen,(255,255,255),self.triangle2(18,135+self.selection*60))
        screen.blit(self.choose_msg,(20,20))
        
    def triangle2 (self,x,y):
        return (x,y), (x-15,y-15), (x-15,y+15)
    
    def new_input(self,events):
        global battle
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    if self.selection == len(self.options)-1:
                        self.selection = 0
                    else:
                        self.selection += 1
                elif event.key == pygame.K_UP:
                    if self.selection == 0:
                        self.selection = len(self.options)-1
                    else:
                        self.selection -=1
                elif event.key == pygame.K_x:
                    if self.use == 1:
                        if self.pok_list[self.selection].hp == 0:
                            battle.add_focus(Text(self.pok_list[self.selection].species +" has no will to fight!"))
                        elif self.selection == battle.player_current:
                            battle.add_focus(Text("Already out!"))
                        else:
                            battle.visuals.pokemon = None
                            battle.player_current = self.selection
                            battle.visuals.movement_countdown = battle.visuals.pokeball.trainer_throw()
                            #del battle.visuals.focus[-1]
                            battle.visuals.focus = [battle.visuals.focus[0]]
                            battle.state = 5
                            if battle.player_fainted == False:
                                battle.player_went = True
                            battle.player_fainted = False
                            print ('here')
                    elif type(self.use) == item:
                        if self.use.aid:
                            del battle.visuals.focus[-1]
                            del battle.visuals.focus[-1]
                            i = battle.player.items.index(self.use)
                            battle.player.items[i].use(self.pok_list[self.selection])
                            battle.player.items[i].quantity -= 1
                            if battle.player.items[i].quantity == 0:
                                del battle.player.items[i]
                            battle.player_ui()
                            battle.add_focus(Text("Used "+ self.use.name + " on " + self.pok_list[self.selection].species+'.'))
                            battle.player_went = True
                            battle.state = 20

                elif event.key == pygame.K_z:
                    if battle.player_fainted:
                        battle.add_focus(Text("Choose a pokemon!"))
                    else:
                        del battle.visuals.focus[-1]
                    
class item_menu:
    def __init__ (self,pok_list,item_list):
        self.pointer = None
        self.options = [font4.render(str(i.quantity)+" "+str(i.name),True,(255,237,63)) for i in item_list]
        self.selection = 0
        self.actual = 0
        self.showing = 0
        self.item_list = item_list
        self.pok_list = pok_list
        self.choose_msg = font4.render("Choose an item", True,(60,237,63))
        
    def draw(self):
        x = 500
        y = 500
        screen.fill ((0,0,0))
        for i in range(6):
            try:
                screen.blit(self.options[self.showing+i],(20,120+60*i))
            except:
                pass
        pygame.draw.polygon(screen,(255,255,255),self.triangle2(18,135+self.selection*60))
        screen.blit(self.choose_msg,(20,20))
        
    def triangle2 (self,x,y):
        return (x,y), (x-15,y-15), (x-15,y+15)
    
    def new_input(self,events):
        global battle
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    if len(self.options) == 0:
                        self.selection = 0
                        self.showing = 0
                        self.actual = 0
                    else:
                        if self.actual == len(self.options)-1:
                            self.selection = 0
                            self.showing = 0
                            self.actual = 0
                        else:
                            self.selection += 1
                            self.actual += 1
                            if self.actual == self.showing +6:
                                self.showing += 1
                                self.selection = 5
                elif event.key == pygame.K_UP:
                    if len(self.options) == 0:
                        self.selection = 0
                        self.showing = 0
                        self.actual = 0
                    else:
                        if self.actual == 0:
                            self.selection = min(5,len(self.options)-1)
                            self.actual = len(self.options)-1
                            if len(self.options) >= 6:
                                self.showing = len(self.options)-6
                            else:
                                self.showing = 0
                        else:
                            self.selection -=1
                            self.actual -= 1
                            if self.actual < self.showing:
                                self.showing = self.actual
                            if self.selection < 0:
                                self.selection = 0
                elif event.key == pygame.K_x:
                    if battle.player.items[self.actual].aid:
                        battle.add_focus(pokemon_menu(battle.player.pokemon,battle.player.items[self.actual]))
                    elif battle.player.items[self.actual].ball:
                        if type(battle.opp) == pokemon:
                            battle.player.items[self.actual].quantity -= 1
                            if battle.player.items[self.actual].quantity == 0:
                                del battle.player.items[self.actual]
                            del battle.visuals.focus[-1]
                            battle.visuals.movement_countdown = battle.visuals.pokeball.attempt_capture()
                            battle.state = 22
                        else:
                            battle.add_focus(Text("You can't capture an owned pokemon!"))
                elif event.key == pygame.K_z:
                    battle.player_ui()
                    del battle.visuals.focus[-1]

class Text: #Text class was recycled from an older project. Time permitting it should be redone and documentation added.
    def __init__ (self,contents):
        self.blinker = True #set to False if you want no triangle flashing
        self.contents = contents
        self.pointer = None
        total_len = len(self.contents)
        chunk_len = 23
        start = 0
        end = chunk_len
        self.chunks = []
        #battle_logic to break the text up into smaller chunks
        while True:
            chunk = self.contents[start:end]
            try:
                while self.contents[end] != " ":
                    end -=1
                chunk = self.contents[start:end]
                self.chunks.append(chunk)
                if end > total_len:
                    break
                start = end+1
                end = end+chunk_len
            except:
                self.chunks.append(self.contents[start:])
                break

        text_imgs = []
        for i in self.chunks:
            new = font.render(i, True, (255,237,63))
            text_imgs.append(new)
        self.chunks = text_imgs
        
        self.slot1 = None
        self.slot2 = None
        self.ticker1 = 0 #hides top line of text
        self.ticker2 = 0 #hides bottom line
        self.slider = -1
        self.finished = False
        
        self.ticker3 = 0 
        self.show_tri = False
    def triangle (x,y):
        return (x,y), (x-10,y-10), (x+10,y-10)
    def draw(self):
        x = 500
        y = 500
        if self.slot1 == None:
            try:
                self.slot1 = self.chunks[0]
                del self.chunks[0]
                self.ticker1 = 50
            except:
                pass
        if self.slot2 == None:
            try:
                self.slot2 = self.chunks[0]
                del self.chunks[0]
                self.ticker2 = 50
            except:
                self.slot2 = None
        if self.ticker1 > 0:
            self.ticker1 -= 1
        elif self.ticker2 > 0 and self.ticker1 == 0:
            self.ticker2 -= 1
        if self.slider >= 0:
            self.slider += 1
        if self.slider == 50:
            self.slider = -1
            if self.chunks:
                self.slot1 = self.slot2
                self.slot2 = None
        pygame.draw.rect(screen,(240,145,47),(0,y-120,x,y))
        
        if self.slot1 and self.slider < 10:
            screen.blit(self.slot1,(0,390-self.slider))
        if self.slot2:
            screen.blit(self.slot2,(0,435-self.slider))
        if self.ticker1>0:
            pygame.draw.rect(screen,(240,145,47),(x-self.ticker1*10,y-120,x,70))
        if self.ticker2>0:
            pygame.draw.rect(screen,(240,145,47),(x-self.ticker2*10,y-72,x,70))
        if self.ticker1 == 0 and self.ticker2 == 0 and self.ticker3 == 0 and self.blinker:
            if self.show_tri == False:
                self.show_tri = True
            else:
                self.show_tri = False
            self.ticker3 = 250  
        if self.show_tri:
            pygame.draw.polygon(screen,(0,0,0),Text.triangle(450,490))
        if self.ticker3 >0:
            self.ticker3-=1
            
    def new_input(self,events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:
                    #print (self.slot1,"@@@",self.slot2,'###','ticker1',self.ticker1,', ticker2',self.ticker2,', slider:',self.slider,'show_tli',self.show_tri)
                    if self.ticker1 > 0 or self.ticker2 > 0:
                        self.ticker1 = 0
                        self.ticker2 = 0
                        self.show_tri = True
                        self.ticker3 = 50
                    elif self.chunks and self.slider == -1:
                        self.slider = 0
                        self.show_tri = False
                        self.ticker3 = 50
                    elif not self.chunks and self.slider == -1:
                        del self.pointer[-1]


class visual_logic:
    def __init__ (self):
        #sprites
        self.trainer = None
        self.opp_trainer = None
        self.pokemon = None
        self.opp_pokemon = None
        self.pokeball = None
        self.name = None
        self.level = None
        self.hp = None
        self.opp_name = None
        self.opp_level = None
        self.opp_hp = None
        self.title = None
        self.author = None
        self.button_map = None
        self.icon = None
        self.prompt = None
        
        #extra
        self.focus = []
        self.movement_countdown = 0
    
    def make_scene(self):
        global battle
        #self.state_marker = font.render(str(battle.state), True, (255,237,63))
        #screen.blit(self.state_marker,(50,50))
        
        for i in [self.trainer,
                  self.opp_trainer,
                  self.pokemon,
                  self.opp_pokemon,
                  self.pokeball,
                  self.name,
                  self.level,
                  self.hp,
                  self.opp_name,
                  self.opp_level,
                  self.opp_hp,
                  self.title,
                  self.author,
                  self.button_map,
                  self.icon,
                  self.prompt]:
            if i:
                i.draw()
        if self.movement_countdown > 0:
            self.movement_countdown -=1
        for i in self.focus:
            i.draw()
    def add_focus(self,new_focus):
        print ('battle visuals is adding a focus')
        self.focus.append(new_focus)
class image:
    def __init__ (self):
        #default settings
        self.img = pygame.Surface((80,80))
        self.img.fill((255,255,255))
        #future image locations
        self.reel = [(0,0),(1,1),(20,20),(40,40)]
        
    def draw(self):
        if len(self.reel)>1:
            #draw location popped if it's not the last remaining position
            screen.blit(self.img,self.reel.pop(0))
        else:
            screen.blit(self.img,self.reel[0])
    def opp_intro_slide(self):
        #movement pattern
        self.reel = [(i-80,30) for i in range (450)]
        #ends at [(370,30)]
        return 450
    def opp_slide_out(self):
        self.reel = [(370+i,30) for i in range (200)]
        return 200
    def opp_throw(self):
        self.reel = [(500-i,-51+i) for i in range (200)]
        self.reel += [(300,150-i) for i in range (50)]
        self.reel += [(600,0)]
        return 250
        #pokemon stands at at (300,150)
    def trainer_throw(self):
        self.reel = [(-100+i,100+i) for i in range (200)]
        self.reel += [(100,300-i) for i in range (50)]
        self.reel += [(600,0)]#### flip #####
        return 250
    def trainer_intro_slide(self):
        #movement pattern
        self.reel = [(500-i,280) for i in range (450)]
        return 450
    def trainer_slide_out(self):
        self.reel = [(50-i,280) for i in range (200)]
        return 200
    def player_tackle(self):
        self.reel = [(90+i,280) for i in range (0,80,2)]
        self.reel.append((90,280))
        return 40
    def opp_tackle(self):
        self.reel = [(300-i,150) for i in range (0,80,2)]
        self.reel.append((300,150))
        return 40
    def wild_intro_slide(self):
        self.reel = [(i-150,150) for i in range (450)]
        return 450
    def take_hit(self):
        self.reel = [self.reel[0] for i in range (40)]
        for i in range (20):
            self.reel += [(600,0) for i in range (4)] + [(self.reel[0]) for i in range (2)] 
        return 200
    def attempt_capture(self):
        global battle
        self.reel = [(100+i,300-i) for i in range (200)]
        self.reel += [(300,100-i) for i in range (50)]
        self.reel += [(300,100+i) for i in range (50)]
        return 500
    
class battle_logic:
    def __init__ (self,player,opp):
        #state keeps track of what is happening in the battle
        if type(opp) == opponent:
            self.state = 0
        elif type(opp) == pokemon:
            self.state = 16
        
        #determine where new inputs should be redirected
        self.focus = []
        
        #define combatents
        self.player = player
        self.opp = opp
        
        #define visual handler
        self.visuals = visual_logic()
        
        #define variable if each has attacked
        self.player_went = False
        self.opp_went = False
        
        #define variable if player's pokemon is fainted
        self.player_fainted = False
        
        self.combatents = []
        
        #
        self.selection = None
        
        #identify first non-fainted pokemon in player's party
        for i in range(len(player.pokemon)):
            if player.pokemon[i].hp > 0:
                self.player_current = i
                break
        #identify first pokemon in opponent's party
        self.opp_current = 0
    
    def create_pokeball(self):
        self.visuals.pokeball = image()
        self.visuals.pokeball.img.fill((0,0,0))
        
        red = pygame.Surface((80,40))
        pygame.draw.circle(red,(255,50,50),(40,40),40)
        
        white = pygame.Surface((80,40))
        pygame.draw.circle(white,(255,255,255),(40,0),40)
        
        grey = pygame.Surface((80,10))
        pygame.draw.circle(grey,(155,155,155),(40,5),40)
        
        rim = pygame.Surface ((20,20))
        pygame.draw.circle(rim,(155,155,155),(10,10),10)
        rim.set_colorkey((0,0,0))
        
        button = pygame.Surface ((20,20))
        pygame.draw.circle(button,(255,255,255),(10,10),6)
        button.set_colorkey((0,0,0))
        
        self.visuals.pokeball.img.blit(red,(0,0))
        self.visuals.pokeball.img.blit(white,(0,40))
        self.visuals.pokeball.img.blit(grey,(0,35))
        self.visuals.pokeball.img.blit(rim,(30,30))
        self.visuals.pokeball.img.blit(button,(30,30))
        self.visuals.pokeball.img.set_colorkey((0,0,0))
        self.visuals.pokeball.img = pygame.transform.scale(self.visuals.pokeball.img, (20,20))
        
    def opp_ui(self):
        try:
            self.visuals.opp_name = ui_string(self.opp.pokemon[self.opp_current].species,100,0,font,(255,237,63))
            self.visuals.opp_level = ui_string("Lvl: "+str(self.opp.pokemon[self.opp_current].level),100,25,font,(255,237,63))
            self.visuals.opp_hp = ui_string(str("Hp:"+str(self.opp.pokemon[self.opp_current].hp)+"/"+str(self.opp.pokemon[self.opp_current].max_hp)),100,50,font,(255,237,63))
        except:
            self.visuals.opp_name = ui_string(self.opp.species,100,0,font,(255,237,63))
            self.visuals.opp_level = ui_string("Lvl: "+str(self.opp.level),100,25,font,(255,237,63))
            self.visuals.opp_hp = ui_string(str("Hp:"+str(self.opp.hp)+"/"+str(self.opp.max_hp)),100,50,font,(255,237,63))

    def player_ui(self):
        self.visuals.name = ui_string(self.player.pokemon[self.player_current].species,300,300,font,(255,237,63))
        self.visuals.level = ui_string("Lvl: "+str(self.player.pokemon[self.player_current].level),300,325,font,(255,237,63))
        self.visuals.hp = ui_string(str("Hp:"+str(self.player.pokemon[self.player_current].hp)+"/"+str(self.player.pokemon[self.player_current].max_hp)),300,350,font,(255,237,63))
    
        #self.visuals.opp_level.reel = [(0,0)]
        #self.visuals.opp_hp.reel = [(0,0)]
    
    def update(self):
        if self.state == 0:
            pygame.mixer.music.load("battle.mp3")
            pygame.mixer.music.play(-1)
            self.visuals.trainer = self.player.trainer_sprite
            self.visuals.opp_trainer = self.opp.trainer_sprite
            self.visuals.movement_countdown = self.visuals.opp_trainer.opp_intro_slide()
            self.visuals.trainer.trainer_intro_slide()
            self.state = 1
        if self.state == 1 and self.visuals.movement_countdown == 0 and self.visuals.focus == []:
            self.visuals.focus = [Text(self.opp.name+" wants to battle!")]
            self.visuals.focus[0].pointer = self.visuals.focus
            self.state = 2
        if self.state == 2 and self.visuals.focus == []:
            self.create_pokeball()
            self.visuals.opp_trainer.opp_slide_out()
            self.visuals.pokeball.opp_throw()
            self.visuals.movement_countdown = self.visuals.pokeball.opp_throw()
            self.state = 3
        if self.state == 3 and self.visuals.movement_countdown == 0:
            self.opp_ui()
            self.visuals.opp_pokemon = self.opp.pokemon[self.opp_current].front
            self.visuals.opp_pokemon.reel = [(300,150)]
            self.visuals.focus = [Text(self.opp.name+" sent out "+self.opp.pokemon[self.opp_current].species+"!")]
            self.visuals.focus[0].pointer = self.visuals.focus
            self.state = 4
        if self.state == 4 and self.visuals.focus == []:
            self.create_pokeball()
            self.visuals.trainer.trainer_slide_out()
            self.visuals.movement_countdown = max(self.visuals.trainer.trainer_slide_out(),self.visuals.pokeball.trainer_throw())
            self.visuals.pokeball.trainer_throw()
            self.state = 5
        if self.state == 5 and self.visuals.movement_countdown == 0:
            self.player_ui()
            self.visuals.pokemon = self.player.pokemon[self.player_current].back
            self.visuals.pokemon.reel = [(90,280)]
            self.visuals.focus = [Text("Go "+ self.player.pokemon[self.player_current].species + "!")]
            self.visuals.focus[0].pointer = self.visuals.focus
            self.state = 6
        if self.state == 6 and self.visuals.focus == []:
            if self.player_went:
                self.lock_move()
            else:
                self.visuals.focus = [battle_menu()]
                self.visuals.focus[0].pointer = self.visuals.focus
                self.state = 7
        if self.state == 8 and self.visuals.movement_countdown == 0 and type(self.visuals.focus[-1]) != Text:
            self.lock_move()
        if self.state == 9 and not any(isinstance(i,Text) for i in self.visuals.focus): #opponent fainted
            if type(self.opp) == opponent:
                for i in range (len(self.opp.pokemon)):
                    if self.opp.pokemon[i].hp > 0:
                        self.opp_current = i
                        self.visuals.movement_countdown = self.visuals.pokeball.opp_throw()
                        self.visuals.focus = []
                        self.state = 10
                        break
            if self.state == 9:#opponent has not pokemon left
                self.state = 11
                self.visuals.pokemon = None
                try:
                    self.visuals.opp_trainer.opp_intro_slide()
                except:
                    pass
                try:
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load('Victory.mp3')
                    pygame.mixer.music.play(-1)
                    self.visuals.focus = [Text(self.opp.defeat_text)]
                    self.visuals.focus[0].pointer = self.visuals.focus
                    self.visuals.movement_countdown = self.visuals.trainer.trainer_intro_slide()
                except:
                    self.state = 11
                    self.visuals.focus = []
                self.visuals.opp_name = None
                self.visuals.opp_level = None
                self.visuals.opp_hp = None
                self.visuals.name = None
                self.visuals.level = None
                self.visuals.hp = None
        if self.state == 10 and self.visuals.movement_countdown == 0:#opponent new pokemon
            self.visuals.opp_pokemon = self.opp.pokemon[self.opp_current].front
            self.visuals.opp_pokemon.reel = [(300,150)]
            self.opp_ui()
            self.state = 12
        if self.state == 11 and self.visuals.focus == []:
            kill_battle_trainer_won()
        if self.state == 12:
            self.visuals.focus = [battle_menu(), Text(self.opp.name+" sent out "+self.opp.pokemon[self.opp_current].species)]
            self.visuals.focus[1].pointer = self.visuals.focus
            self.state = 13
        if self.state == 14 and not any(isinstance(i,Text) for i in self.visuals.focus):#player's pokemon fainted
            self.whited_out = True
            for i in self.player.pokemon:
                if i.hp > 0:
                    self.visuals.focus.append(pokemon_menu(self.player.pokemon,1))
                    self.visuals.focus[-1].pointer = self.visuals.focus
                    self.whited_out = False
                    self.state = 13
            if self.whited_out:
                self.state = 15
                self.visuals.focus = [Text("Battle lost!")]
                self.visuals.focus[0].pointer = self.visuals.focus
        if self.state == 15 and not any(isinstance(i,Text) for i in self.visuals.focus):#player's lost battle
            quit()
        
        #wild pokemon encounter
        if self.state == 16:
            self.visuals.trainer = self.player.trainer_sprite
            self.visuals.opp_pokemon = self.opp.front
            self.visuals.movement_countdown = self.visuals.opp_pokemon.wild_intro_slide()
            self.visuals.trainer.trainer_intro_slide()
            self.state = 17
        if self.state == 17 and self.visuals.movement_countdown == 0:
            battle.opp_ui()
            battle.add_focus(Text("A wild " + self.opp.species + " appeared!"))
            self.state =4
        if self.state == 18 and not any(isinstance(i,Text) for i in self.visuals.focus):
            self.visuals.movement_countdown = self.visuals.trainer.trainer_slide_out()
            self.state = 19
        if self.state == 19 and self.visuals.movement_countdown == 0:
            pass
        if self.state == 20 and not any(isinstance(i,Text) for i in self.visuals.focus):
            self.lock_move()
        if self.state == 21 and not any(isinstance(i,Text) for i in self.visuals.focus):
            print ('kill battle, player ran')
        if self.state == 22 and self.visuals.movement_countdown == 250:
            self.visuals.opp_pokemon = None
        if self.state == 22 and self.visuals.movement_countdown == 0:
            if self.attempt_capture():
                if len(self.player.pokemon) < 6:
                    self.player.pokemon.append(self.opp)
                    self.state = 23
                    battle.add_focus(Text("Gotcha!" + self.opp.species+ " was caught!"))
                else:
                    self.opp.hp = self.opp.max_hp
                    self.player.pc_pokemon.append(self.opp)
                    battle.add_focus(Text(self.opp.species+ " was sent to the PC"))
                    battle.add_focus(Text(self.opp.species+ " was caught!!"))
                    self.state = 23
            else:
                self.visuals.opp_pokemon = self.opp.img
                self.visuals.opp_pokemon.reel = [(300,150)]
                #self.visuals.pokeball.reel= [(600,0)]
                battle.add_focus(Text(self.opp.species+ " broke free!"))
                self.player_went = True
                self.state = 20
        if self.state == 23 and not any(isinstance(i,Text) for i in self.visuals.focus):
            print ('kill battle, pokemon caught')
    
    def attempt_capture(self):
        if self.opp.hp < self.opp.max_hp:
            return True
        else:
            return False
    
    def new_input(self,events):
        try:
            self.visuals.focus[-1].new_input(events)
        except:
            pass
    
    def add_focus(self,new_focus):
        self.visuals.focus.append(new_focus)
        self.visuals.focus[-1].pointer = self.visuals.focus
    
    def remove_focus(self,new_focus):
        del self.focus[0]
    
    def get_moves(self):
        return self.player.pokemon[self.player_current].moves
    
    def lock_move(self):
        self.state = 8
        if self.player_went == False and self.opp_went == False:
            player_speed_check = self.player.pokemon[self.player_current].speed * self.player.pokemon[self.player_current].moves[self.selection].speed
            try:
                opp_speed_check = self.opp.pokemon[self.opp_current].speed * self.opp.pokemon[self.opp_current].moves[0].speed
            except:
                opp_speed_check = self.opp.speed * self.opp.moves[0].speed
            if opp_speed_check>player_speed_check:
                self.opp_attack()
            else:
                self.player_attack()
        elif self.player_went and self.opp_went == False:
            self.visuals.focus = [battle_menu()]
            self.opp_attack()
        elif self.opp_went and self.player_went == False:
            self.visuals.focus = [battle_menu()]
            self.player_attack()
        else:
            self.visuals.focus = [battle_menu()]
            self.visuals.focus[0].pointer = self.visuals.focus
            self.state = 7
            self.player_went = False
            self.opp_went = False
    def player_attack(self):
        self.visuals.pokemon.player_tackle()
        self.visuals.opp_pokemon.take_hit()
        self.visuals.movement_countdown = max(self.visuals.pokemon.player_tackle(),self.visuals.opp_pokemon.take_hit())
        self.visuals.focus.append(Text(self.player.pokemon[self.player_current].species + " used " + self.player.pokemon[self.player_current].moves[self.selection].name + "!"))
        self.visuals.focus[-1].pointer = self.visuals.focus
        self.player.pokemon[self.player_current].moves[self.selection].pp -=1
        if self.player.pokemon[self.player_current].moves[self.selection].att_type == 'physical':
            #physical dabade calculation
            dabade_dealt = self.player.pokemon[self.player_current].strength * self.player.pokemon[self.player_current].moves[self.selection].power * .01
            try:
                self.opp.pokemon[self.opp_current].hp -= dabade_dealt
                self.opp.pokemon[self.opp_current].hp = int(self.opp.pokemon[self.opp_current].hp)
            except:
                self.opp.hp -= dabade_dealt
                self.opp.hp = int(self.opp.hp)
        elif self.player.pokemon[self.player_current].moves[self.selection].att_type == 'special':
            #special dabade calculation
            dabade_dealt = self.player.pokemon[self.player_current].special * self.player.pokemon[self.player_current].moves[self.selection].power * .01
            try:
                self.opp.pokemon[self.opp_current].hp -= dabade_dealt
                self.opp.pokemon[self.opp_current].hp = int(self.opp.pokemon[self.opp_current].hp)
            except:
                self.opp.hp -= dabade_dealt
                self.opp.hp = int(self.opp.hp)
        try:
            target = self.opp.pokemon[self.opp_current]
        except:
            target = self.opp
        if target.hp <= 0:
            self.state = 9 #fainted opponent pokemon
            self.visuals.opp_pokemon = None
            target.hp = 0
            self.visuals.focus.insert(1,Text(target.species + " fainted!"))
            self.visuals.focus[1].pointer = self.visuals.focus
    
            self.player_went = False
            self.opp_went = False
        else:
            self.player_went = True
        self.opp_ui()
        
    def opp_attack(self):
        print ('health start')
        print (self.player.pokemon[self.player_current].hp)
        try:
            target = self.player.pokemon[self.opp_current]
        except:
            target = self.opp
        self.visuals.opp_pokemon.opp_tackle()
        self.visuals.pokemon.take_hit()
        self.visuals.movement_countdown = max(self.visuals.opp_pokemon.opp_tackle(),self.visuals.pokemon.take_hit())
        self.visuals.focus.append(Text("Enemy " +target.species + " used " + target.moves[0].name))
        self.visuals.focus[-1].pointer = self.visuals.focus
        self.opp_went = True
        self.opp_selection = 0
        if target.moves[self.opp_selection].att_type == 'physical':
            #physical dabade calculation
            dabade_dealt = target.strength * target.moves[self.opp_current].power * .01
            print ("dabade dealt",dabade_dealt)
            self.player.pokemon[self.player_current].hp -= dabade_dealt
            self.player.pokemon[self.player_current].hp = int(self.player.pokemon[self.player_current].hp)
        elif self.player.pokemon[self.opp_current].moves[self.opp_selection].att_type == 'special':
            print ('here')
            #special dabade calculation
            dabade_dealt = target.special * target.moves[self.opp_current].power * .01
            self.player.pokemon[self.opp_current].hp -= dabade_dealt
            self.player.pokemon[self.player_current].hp = int(self.opp.pokemon[self.player_current].hp)
        if self.player.pokemon[self.player_current].hp <= 0:
            self.state = 14
            self.visuals.pokemon = None
            self.visuals.focus.insert(1,Text(self.player.pokemon[self.player_current].species + " fainted!"))
            self.visuals.focus[1].pointer = self.visuals.focus
            self.player.pokemon[self.player_current].hp = 0
            self.player_went = False
            self.opp_went = False
            self.player_fainted = True
        print ('health end')
        print(self.player.pokemon[self.player_current].hp)
        self.player_ui()

class player:
    def __init__ (self):
        self.trainer_sprite = image()
        self.pokemon = []
        self.items = []
        self.pc_pokemon = []
        self.pc_items = []
    
class pokemon:
    def __init__ (self):
        self.level = 50
        self.back = image()
        self.front = image()
        self.max_hp = 200
        self.hp = 100
        self.species = "Bulbasaur"
        self.nickname = None
        self.moves = [move(),move(),move(),move()]
        self.speed = 50
        self.strength = 50
        self.special = 50

class move:
    def __init__ (self):
        self.name = "tackle"
        self.att_type = 'physical'
        self.speed = 2
        self.power = 80
        self.pp = 20
        self.max_pp = 20
        self.crit_chance = 10
        
class obstacle:
    def __init__ (self):
        self.img = pygame.Surface((20,20))
        
class opponent(obstacle):
    def __init__ (self):
        super().__init__()
        self.defeat_text = "Bad Guy: You beat me :( Thanks for playing. This is a proof of concept game for CST8333 Programming Language Research Project."
        self.name = "Evil Guy"
        self.img.fill((255,0,0))
        self.trainer_sprite = image()
        self.pokemon= []

class treasure(obstacle):
    def __init__ (self):
        super().__init__()
        self.img.fill((0,0,255))

class border(obstacle):
    def __init__ (self):
        super().__init__()
        self.img.fill((0,255,0))

class barrier(obstacle):
    def __init__ (self):
        super().__init__()
        self.img.fill(100,100,150)

class item:
    def __init__ (self):
        self.name = 'example'
        self.quantity = 2
        self.aid = False
        self.ball = False
        self.healing = 20
    def use (self,target):
        target.hp += self.healing
        if target.hp > target.max_hp:
            target.hp = target.max_hp
        


x = intro()
bad = opponent()
bad.pokemon = [pokemon(),pokemon()]
bad.pokemon[0].species = "Pikachu"
bad.pokemon[0].front.img = sprites.pikachu_front()
bad.pokemon[1].front.img = sprites.bulbasaur_face()
bad.trainer_sprite.img = sprites.trainer_front()


nick = player()
nick.pokemon = [pokemon(),pokemon()]
for i in nick.pokemon:
    i.back.img = sprites.bulbasaur_back()
nick.pokemon[0].back.img = sprites.pikachu_back()
nick.pokemon[0].species = "Pikachu"
xxx = pokemon()
xxx.front.img = sprites.bulbasaur_face()

battle = battle_logic(nick,bad)
nick.items.append(item())
nick.items[0].name= "poke ball"
nick.items[0].quantity = 50
nick.items[0].ball = True
nick.trainer_sprite.img = sprites.trainer_back()
#focus = [intro()]
focus = [x]
overworld = overworld_logic()
while True:
    pygame.time.wait(1)
    screen.fill((0,0,0))
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.KEYDOWN:
            focus[-1].new_input(events)
    focus[-1].update()
    focus[-1].visuals.make_scene()
    pygame.display.update()
    
      