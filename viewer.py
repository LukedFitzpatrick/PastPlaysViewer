# Fury of Dracula game log viewer
# Luke Fitzpatrick, 2015
import sys, pygame
pygame.init()

fo = open("log.txt", "r+")
log = fo.read().split();
fo.close()

map = pygame.image.load("pics/map.jpg")
maprect = map.get_rect()

size = maprect.width+200, maprect.height+40
screen = pygame.display.set_mode(size)

font = pygame.font.SysFont("monospace", 15)
currentplay = 0
keysdown = []

clock = pygame.time.Clock()

playerx = [10, 20, 30, 40, 50]
playery = [10, 20, 30, 40, 50]
playerimages = [pygame.image.load("pics/h0.png"), pygame.image.load("pics/h1.png"), pygame.image.load("pics/h2.png"), pygame.image.load("pics/h3.png"), pygame.image.load("pics/d.png")]

playerlocations = ["??", "??", "??", "??", "??"]

places = [["Adriatic Sea", "AS",584,428], ["Alicante", "AL",217,538], ["Amsterdam", "AM",372,183], ["Athens", "AT",789,540], ["Atlantic Ocean", "AO",48,278], ["Barcelona", "BA",263,479], ["Bari", "BI",650,499], ["Bay of Biscay", "BB",164,342], ["Belgrade", "BE",705,416], ["Berlin", "BR",513,181], ["Black Sea", "BS",911,357], ["Bordeaux", "BO",230,368], ["Brussels", "BU",358,229], ["Bucharest", "BC",793,370], ["Budapest", "BD",656,306], ["Cadiz", "CA",71,578], ["Cagliari", "CG",442,549], ["Castle Dracula", "CD",776,292], ["Clermont-Ferrand", "CF",315,354], ["Cologne", "CO",417,199], ["Constanta", "CN",873,342], ["Dublin", "DU",164,146], ["Edinburgh", "ED",243,71], ["English Channel", "EC",232,244], ["Florence", "FL",501,421], ["Frankfurt", "FR",449,240], ["Galatz", "GA",815,319],["Galway", "GW",114,132], ["Geneva", "GE",396,340], ["Genoa", "GO",450,407], ["Granada", "GR",133,556], ["Hamburg", "HA",442,164], ["Ionian Sea", "IO",675,576], ["Irish Sea", "IR",124,202], ["Klausenburg", "KL",727,317], ["Le Havre", "LE",270,259], ["Leipzig", "LI",484,211], ["Lisbon", "LS",9,510], ["Liverpool", "LV",213,153], ["London", "LO",275,200], ["Madrid", "MA",126,481], ["Manchester", "MN",255,137], ["Marseilles", "MR",376,427], ["Mediterranean Sea", "MS",346,553], ["Milan", "MI",446,372], ["Munich", "MU",508,309], ["Nantes", "NA",209,309], ["Naples", "NP",574,504], ["North Sea", "NS",356,121], ["Nuremburg", "NU",495,270], ["Paris", "PA",319,292], ["Plymouth", "PL",199,224], ["Prague", "PR",538,262], ["Rome", "RO",517,470], ["Salonica", "SA",774,484], ["Santander", "SN",152,410], ["Saragossa", "SR",202,456], ["Sarajevo", "SJ",662,430], ["Sofia", "SO",777,427], ["St Joseph and St Marys", "JM",642,387], ["Strasbourg", "ST",410,283], ["Swansea", "SW",210,190], ["Szeged", "SZ",678,364], ["Toulouse", "TO",273,401], ["Tyrrhenian Sea", "TS",494,560], ["Valona", "VA",717,527], ["Varna", "VR",864,418], ["Venice", "VE",514,377], ["Vienna", "VI",588,304], ["Zagreb", "ZA",600,370], ["Zurich","ZU",435,332], ["Nowhere","??", -100, -100]]

while True:
   milliseconds = clock.tick(20) 
   for event in pygame.event.get():
      if event.type == pygame.QUIT: sys.exit()
      elif event.type == pygame.KEYDOWN: keysdown.append(event.key)
      elif event.type == pygame.KEYUP: keysdown.remove(event.key)
   
   if(pygame.K_DOWN in keysdown):
      currentplay += 1
      currentplay = min(currentplay, len(log)-1)
   if(pygame.K_UP in keysdown):
      currentplay -= 1
      currentplay = max(currentplay, 0)

   playerlocations = ["??", "??", "??", "??", "??"]
   for p in range(0, min(currentplay+1, len(log))):
      if(log[p][0] == "G"): player = 0
      elif(log[p][0] == "S"): player = 1
      elif(log[p][0] == "H"): player = 2
      elif(log[p][0] == "M"): player = 3
      else: player = 4
      
      playerlocations[player] = str(log[p][1]) + str(log[p][2])

      if (player == 4):
         backdistance = 0
         if (playerlocations[4] == "TP"): playerlocations[4] == "CD"
         while (playerlocations[4] == "HI" or playerlocations[4][1].isdigit()):
            if (playerlocations[4] == "HI"): backdistance += 1
            else: backdistance += int(playerlocations[4][1])
            p = currentplay - 5 * backdistance
            playerlocations[4] = str(log[p][1]) + str(log[p][2])


   for i in range(0, len(playerimages)):
      for p in places:
         if(p[1] == playerlocations[i]):
            playerx[i], playery[i] = p[2], p[3]
                  
   screen.fill((0, 0, 0))
   screen.blit(map, maprect)
   
   for i in range(0, len(playerimages)):
      screen.blit(playerimages[i], (playerx[i], playery[i]))
      label = font.render("Player "+str(i)+": "+playerlocations[i],1,(255,255,255))
      screen.blit(label, (i*150+80, maprect.height+5))

   y = 0
   start = max(0, currentplay-8)
   end = start + (maprect.height/20)
   for i in range(start, min(len(log), end)):
      colour = (255, 255, 255)
      if(i == currentplay): colour = (255, 100, 100)
      label = font.render("Play "+str(i)+": "+log[i],1,colour)
      screen.blit(label, (maprect.width, y*20))
      y += 1

   pygame.display.flip()
