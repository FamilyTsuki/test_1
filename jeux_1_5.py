import pyxel


class Joueur:


    def __init__(self):

        self.en_saut = 1
        self.co = {"1": [100,16,0,0],"2": [116,16,0,0],"3": [100,0,0,0],"4": [116,0,0,0]}
        self.tc = 0 
        self.dir = 1
        self.tran = {"1":[1,1],"2":[1,1],"3":[1,1],"4":[1,1]}
        
        self.list_m = [[0,-1000,1000],[382,-1000,1000]]
        self.list_p = [[0,382,100]]
        


    def colision(self):
        global platform
        
        def platform(x1,x2,y):
            
            if (self.co["1"][1]<= y <= self.co["1"][1]+ self.co["1"][3]) :
                if (x2>= self.co["1"][0] >= x1) and not (((self.co["1"][1] <= t1.get_pos_y() <= self.co["1"][1]+self.co["1"][3] or self.co["3"][1] <= t1.get_pos_y() <= self.co["3"][1]+self.co["3"][3]) )) and (( t1.get_pos_x() <= self.co["1"][0] <=t1.get_pos_x()+24 or t1.get_pos_x() <= self.co["3"][0] <=t1.get_pos_x()+24)):
                    
                    for i in ["1","3"]:
                        self.co[i][3] = y - self.co["1"][1]
                    self.en_saut = 1
                    
                    if self.co["1"][2] > 0: 
                        if self.co["1"][2] > 1.5:
                            for i in ["1","3"]:
                                self.co[i][2] -= 1.5
                        else:
                            for i in ["1","3"]:
                                self.co[i][2] = 0
                    elif self.co[i][2] < 0: 
                        if self.co[i][2] < -1.5:
                            for i in ["1","3"]:
                                self.co[i][2] += 1.5
                        else:
                            for i in ["1","3"]:
                                self.co[i][2] = 0
            if (self.co["2"][1]<= y <= self.co["2"][1]+ self.co["2"][3]) :
                if (x2>= self.co["2"][0] >= x1) and not ((self.co["2"][1] <= t1.get_pos_y() <= self.co["2"][1]+self.co["2"][3] or self.co["4"][1] <= t1.get_pos_y() <= self.co["4"][1]+self.co["4"][3]) and ( t1.get_pos_x() <= self.co["2"][0] <=t1.get_pos_x()+24 or t1.get_pos_x() <= self.co["4"][0] <=t1.get_pos_y()+24)):
                    for i in ["2","4"]:
                        self.co[i][3] = y - self.co["2"][1]
                    self.en_saut = 1
                    if self.co["1"][2] > 0: 
                        if self.co["1"][2] > 1.5:
                            for i in ["2","4"]:
                                self.co[i][2] -= 1.5
                        else:
                            for i in ["2","4"]:
                                self.co[i][2] = 0
                    elif self.co[i][2] < 0: 
                        if self.co[i][2] < -1.5:
                            for i in ["2","4"]:
                                self.co[i][2] += 1.5
                        else:
                            for i in ["2","4"]:
                                self.co[i][2] = 0
                
                        
        def mur(x , y1 , y2):

            if self.co["2"][0] <= x and self.co["2"][0] + self.co["2"][2] >= x :#si le perso est a goche
                if (y2>=self.co["4"][1] >= y1 or  y2 >= self.co["2"][1] >= y1) and not (((t1.get_pos_y()-24 <= self.co["4"][1] <= t1.get_pos_y() and  t1.get_pos_y()-24 <= self.co["2"][1] <= t1.get_pos_y()) and (self.co["2"][0] <= t1.get_pos_x() and self.co["2"][0] + self.co["2"][2] >= t1.get_pos_x())) or ((t2.get_pos_y()-24 <= self.co["4"][1] <= t2.get_pos_y() and  t2.get_pos_y()-24 <= self.co["2"][1] <= t2.get_pos_y()) and (self.co["2"][0] <= t2.get_pos_x() and self.co["2"][0] + self.co["2"][2] >= t2.get_pos_x()))):
                    for i in self.co:#                                                                          test y au t1                                            test y ba t1                                                   test y au t2                                         test y ba t2                                       _             test x droit t1                                                                                         test x droit t2                   
                        self.co[i][2] = x-self.co["2"][0]
                    

            elif self.co["1"][0] >= x and self.co["1"][0] + self.co["1"][2] <= x:#si le perso est a droit                                                                                                           pour t1                                                                                                                         pour t2
                if (y2>=self.co["3"][1] >= y1 or  y2 >= self.co["1"][1] >= y1) and not (((t1.get_pos_y()-24 <= self.co["3"][1] <= t1.get_pos_y() and  t1.get_pos_y()-24 <= self.co["1"][1] <= t1.get_pos_y()) and (self.co["1"][0] >= t1.get_pos_x() and self.co["1"][0] + self.co["1"][2] <= t1.get_pos_x())) or ((t2.get_pos_y()-24 <= self.co["3"][1] <= t2.get_pos_y() and  t2.get_pos_y()-24 <= self.co["1"][1] <= t2.get_pos_y()) and (self.co["1"][0] >= t2.get_pos_x() and self.co["1"][0] + self.co["1"][2] <= t2.get_pos_x()))):
                    for i in self.co:
                        self.co[i][2] = x-self.co["1"][0]
                    
                    

        platform(0,382,100)
      
        mur(382,-1000,1000)
        mur(0,-1000,1000)
    def vecteur(self):
        player = [( self.co["1"][0] + self.co["2"][0] )/2 , ( self.co["1"][1] + self.co["3"][1] )/2 ]
        souri = [pyxel.mouse_x , (self.co["1"][1]+self.co["3"][1])/2-100 + pyxel.mouse_y]
        
        n = souri[0] - player[0]
        r = (souri[1] - player[1])/n
        return r
    def recherche_plat():
        pass
    def recherche_mur(self,s):
        if s == "l":
            p = t1
        else:
            p = t2
        r = self.vecteur()
        xn = int(( self.co["1"][0] + self.co["2"][0] )/2)
        x0 = int(( self.co["1"][0] + self.co["2"][0] )/2)
        yn = int(( self.co["1"][1] + self.co["3"][1] )/2)
        y0 = int(( self.co["1"][1] + self.co["3"][1] )/2)
        while -5 < xn < 387 and (y0-300) < yn < (y0 + 300):
            for tab in self.list_m:#[0,-1000,1000]
                if xn == tab[0] :
                    if tab[1]< yn < tab[2]:
                        
                        for i in self.list_p:#[0,382,100]
                            if y0 <= i[2] and yn +12>= i[2]:
                                p.set_pos(xn,i[2])
                            else:
                                p.set_pos(xn,yn+12)
                        if pyxel.mouse_x > x0:
                            p.set_angle(0)
                        else:
                            p.set_angle(180)
                        break
            if pyxel.mouse_x > x0:
                xn+=1
                yn+=r
            else:
                xn-=1
                yn-=r



    def commande(self):

        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            self.recherche_mur("l")
        if pyxel.btnp(pyxel.MOUSE_BUTTON_RIGHT):
            self.recherche_mur("r")
        if pyxel.btn(pyxel.KEY_D):
            if self.co["1"][2] < 6:
                for i in self.co:
                        self.co[i][2] += 3 
        if pyxel.btn(pyxel.KEY_Q):
            if self.co["1"][2] > -6:
                for i in self.co:
                        self.co[i][2] -= 3 
        if pyxel.btn(pyxel.KEY_Z):
            if self.en_saut == 1 and self.co["1"][3] == 0:
                self.tc = pyxel.frame_count
                for i in self.co:
                    self.co[i][3] -= 6 
                
                self.en_saut = 0
            else:
                if 8 > (pyxel.frame_count - self.tc) > 1:
                    for i in self.co:
                        self.co[i][3] -= 1
                    
    
    
    def actu1(self):
        for i in self.co:
            self.co[i][3] += 1
        if self.en_saut == 0:
            if self.co["1"][2] > 0: 
                for i in self.co:
                    self.co[i][2] -= 0.5
            elif self.co["1"][2] < 0: 
                for i in self.co:
                    self.co[i][2] += 0.5


    def actu2(self):
        
        for i in ["1","2","3","4"]:
            if self.tran[i][0] == 1:
                self.co[i][0] += self.co[i][2]
            elif self.tran[i][0] == -1:
                self.co[i][0] -= self.co[i][2]
            elif self.tran[i][0] == 2:
                self.co[i][0] += self.co[i][3]
            elif self.tran[i][0] == -2:
                self.co[i][0] -= self.co[i][3]


        for i in ["1","2","3","4"]:
            if self.tran[i][1] == 1:
                self.co[i][1] += self.co[i][3]
            elif self.tran[i][1] == -1:
                self.co[i][1] -= self.co[i][3]
            elif self.tran[i][1] == 2:
                self.co[i][1] += self.co[i][2]
            elif self.tran[i][1] == -2:
                self.co[i][1] -= self.co[i][2]

            
        



        
    def set_tran(self,n,m):
        self.tran[n] = m
        

            

        
    def portaille(self):
        
        if t1.get_angle() == 0:
            if t2.get_angle() == 180:
                key = '2'
                
                if (self.co[key][0] <= t1.get_pos_x() and (self.co[key][0] + self.co[key][2]) > t1.get_pos_x() and ((t1.get_pos_y()- 24) <=  self.co[key][1] <= t1.get_pos_y()))     and    (self.co[["2","4"][(["2","4"].index(key)-1)]][0] <= t1.get_pos_x() and (self.co[["2","4"][(["2","4"].index(key)-1)]][0] + self.co[["2","4"][(["2","4"].index(key)-1)]][2]) > t1.get_pos_x() and ((t1.get_pos_y()- 24) <=  self.co[["2","4"][(["2","4"].index(key)-1)]][1] <= t1.get_pos_y())):
                    for key in ["2","4"]:# ver la droit 
                        self.co[key][0] = (t2.get_pos_x() + self.co[key][0] - t1.get_pos_x())
                        self.co[key][1] -= t1.get_pos_y() - t2.get_pos_y()
                        self.set_tran("1",[1,0])
                        self.set_tran("2",[1,0])
                        self.set_tran("3",[1,0])
                        self.set_tran("4",[1,0])
                       
                        
                key = "1"
                if (self.co[key][0] <= t1.get_pos_x() and (self.co[key][0] + self.co[key][2]) > t1.get_pos_x() and ((t1.get_pos_y()- 24) <=  self.co[key][1] <= t1.get_pos_y()))     and    (self.co[["1","3"][(["1","3"].index(key)-1)]][0] <= t1.get_pos_x() and (self.co[["1","3"][(["1","3"].index(key)-1)]][0] + self.co[["1","3"][(["1","3"].index(key)-1)]][2]) > t1.get_pos_x() and ((t1.get_pos_y()- 24) <=  self.co[["1","3"][(["1","3"].index(key)-1)]][1] <= t1.get_pos_y())):
                    for key in ["1","3"]:
                        self.co[key][0] = t2.get_pos_x() + self.co[key][0] - t1.get_pos_x()
                        self.co[key][1] -= t1.get_pos_y() - t2.get_pos_y()
                        self.set_tran("1",[1,1])
                        self.set_tran("2",[1,1])
                        self.set_tran("3",[1,1])
                        self.set_tran("4",[1,1])
                        
            

            if t2.get_angle()  == 90:# verre le bas 
                key = "2"
                
                if (self.co[key][0] <= t1.get_pos_x() and (self.co[key][0] + self.co[key][2]) > t1.get_pos_x() and ((t1.get_pos_y()- 24) <=  self.co[key][1] <= t1.get_pos_y()))     and    (self.co[["2","4"][(["2","4"].index(key)-1)]][0] <= t1.get_pos_x() and (self.co[["2","4"][(["2","4"].index(key)-1)]][0] + self.co[["2","4"][(["2","4"].index(key)-1)]][2]) > t1.get_pos_x() and ((t1.get_pos_y()- 24) <=  self.co[["2","4"][(["2","4"].index(key)-1)]][1] <= t1.get_pos_y())):
                    for key in ["2","4"]:
                        self.co[key][0] = t2.get_pos_x() - (self.co["4"][1]- t1.get_pos_y())
                        self.co[key][1] = t2.get_pos_y()+ (self.co[key][1]-t1.get_pos_y())
                        self.set_tran("1",[1,0])
                        self.set_tran("3",[1,0])
                        self.set_tran("4",[0,2])
                        self.set_tran("2",[0,2])
                key = "1"
                if (self.co[key][0] <= t1.get_pos_x() and (self.co[key][0] + self.co[key][2]) > t1.get_pos_x() and ((t1.get_pos_y()- 24) <=  self.co[key][1] <= t1.get_pos_y()))     and    (self.co[["1","3"][(["1","3"].index(key)-1)]][0] <= t1.get_pos_x() and (self.co[["1","3"][(["1","3"].index(key)-1)]][0] + self.co[["1","3"][(["1","3"].index(key)-1)]][2]) > t1.get_pos_x() and ((t1.get_pos_y()- 24) <=  self.co[["1","3"][(["1","3"].index(key)-1)]][1] <= t1.get_pos_y())):
                    for key in ["1","3"]:
                        self.co[key][0] = t2.get_pos_x()
                        self.co[key][1] = t2.get_pos_y()- (7.5*(int(key)-1))+16
                        self.co[str(int(key)+1)][0] = t2.get_pos_x()+16
                        self.co[str(int(key)+1)][1] = self.co[key][1]
                        self.co[str(int(key)+1)][2] = self.co[str(int(key)+1)][3]
                        self.set_tran("1",[1,1])
                        self.set_tran("3",[1,1])
                        self.set_tran("4",[1,1])
                        self.set_tran("2",[1,1])
                        self.co[key][2] = self.co[str(int(key)+1)][2]
                        self.co[key][3] = self.co[str(int(key)+1)][3]
            if t2.get_angle()  == 270:# verre le O
                key = "2"
                if (self.co[key][0] <= t1.get_pos_x() and (self.co[key][0] + self.co[key][2]) > t1.get_pos_x() and ((t1.get_pos_y()- 24) <=  self.co[key][1] <= t1.get_pos_y()))     and    (self.co[["2","4"][(["2","4"].index(key)-1)]][0] <= t1.get_pos_x() and (self.co[["2","4"][(["2","4"].index(key)-1)]][0] + self.co[["2","4"][(["2","4"].index(key)-1)]][2]) > t1.get_pos_x() and ((t1.get_pos_y()- 24) <=  self.co[["2","4"][(["2","4"].index(key)-1)]][1] <= t1.get_pos_y())):
                    for key in ["2","4"]:
                        self.co[key][0] = t2.get_pos_x() - (self.co["4"][1]- t1.get_pos_y())
                        self.co[key][1] = t2.get_pos_y()+ (self.co[key][1]-t1.get_pos_y())+16
                        self.set_tran("1",[1,0])
                        self.set_tran("3",[1,0])
                        self.set_tran("4",[0,-2])
                        self.set_tran("2",[0,-2])
                key = "1"
                if (self.co[key][0] <= t1.get_pos_x() and (self.co[key][0] + self.co[key][2]) > t1.get_pos_x() and ((t1.get_pos_y()- 24) <=  self.co[key][1] <= t1.get_pos_y()))     and    (self.co[["1","3"][(["1","3"].index(key)-1)]][0] <= t1.get_pos_x() and (self.co[["1","3"][(["1","3"].index(key)-1)]][0] + self.co[["1","3"][(["1","3"].index(key)-1)]][2]) > t1.get_pos_x() and ((t1.get_pos_y()- 24) <=  self.co[["1","3"][(["1","3"].index(key)-1)]][1] <= t1.get_pos_y())):
                    for key in ["1","3"]:
                        self.co[key][0] = t2.get_pos_x()
                        self.co[key][1] = t2.get_pos_y()- (7.5*(int(key)-1))-16
                        self.co[str(int(key)+1)][0] = t2.get_pos_x()+16
                        self.co[str(int(key)+1)][1] = self.co[key][1]
                        self.co[str(int(key)+1)][2] = self.co[str(int(key)+1)][3]
                        self.set_tran("1",[1,1])
                        self.set_tran("3",[1,1])
                        self.set_tran("4",[1,1])
                        self.set_tran("2",[1,1])
                        self.co[key][2] = self.co[str(int(key)+1)][2]
                        self.co[key][3] = self.co[str(int(key)+1)][3]


            if t2.get_angle()  == 0:
                def mur(x , y1 , y2):

                    if self.co["2"][0] <= x and self.co["2"][0] + self.co["2"][2] >= x:
                        if y2>=self.co["4"][1] >= y1 or  y2 >= self.co["2"][1] >= y1:
                            for i in self.co:
                                self.co[i][2] = x-self.co["2"][0]

                    elif self.co["1"][0] >= x and self.co["1"][0] + self.co["1"][2] <= x:
                        if y2>=self.co["3"][1] >= y1 or  y2 >= self.co["1"][1] >= y1:
                            for i in self.co:
                                self.co[i][2] = x-self.co["1"][0]
                mur(t1.get_pos_x() , t1.get_pos_y() , t1.get_pos_y() + 24)





                
        if t1.get_angle() == 180:
            if t2.get_angle() == 180:
                def mur(x , y1 , y2):

                    if self.co["2"][0] <= x and self.co["2"][0] + self.co["2"][2] >= x:
                        if y2>=self.co["4"][1] >= y1 or  y2 >= self.co["2"][1] >= y1:
                            for i in self.co:
                                self.co[i][2] = x-self.co["2"][0]

                    elif self.co["1"][0] >= x and self.co["1"][0] + self.co["1"][2] <= x:
                        if y2>=self.co["3"][1] >= y1 or  y2 >= self.co["1"][1] >= y1:
                            for i in self.co:
                                self.co[i][2] = x-self.co["1"][0]
                mur(t1.get_pos_x() , t1.get_pos_y() , t1.get_pos_y() + 24)
                
                        
            if t2.get_angle()  == 0:
                key = "1"
                if (self.co[key][0] >= t1.get_pos_x() and (self.co[key][0] + self.co[key][2]) < t1.get_pos_x() and ((t1.get_pos_y()- 24) <=  self.co[key][1] <= t1.get_pos_y()))     and    (self.co[["1","3"][(["1","3"].index(key)-1)]][0] >= t1.get_pos_x() and (self.co[["1","3"][(["1","3"].index(key)-1)]][0] + self.co[["1","3"][(["1","3"].index(key)-1)]][2]) < t1.get_pos_x() and ((t1.get_pos_y()- 24) <=  self.co[["1","3"][(["1","3"].index(key)-1)]][1] <= t1.get_pos_y())):
                    for key in ["1","3"]:
                        self.co[key][0] = t2.get_pos_x() + (self.co[key][0]-t1.get_pos_x())
                        self.co[key][1] -= t1.get_pos_y() - t2.get_pos_y()
                        self.set_tran("1",[1,0])
                        self.set_tran("2",[1,0])
                        self.set_tran("3",[1,0])
                        self.set_tran("4",[1,0])
                key = "2"
                if (self.co[key][0] >= t1.get_pos_x() and (self.co[key][0] + self.co[key][2]) < t1.get_pos_x() and ((t1.get_pos_y()- 24) <=  self.co[key][1] <= t1.get_pos_y()))     and    (self.co[["2","4"][(["2","4"].index(key)-1)]][0] >= t1.get_pos_x() and (self.co[["2","4"][(["2","4"].index(key)-1)]][0] + self.co[["2","4"][(["2","4"].index(key)-1)]][2]) < t1.get_pos_x() and ((t1.get_pos_y()- 24) <=  self.co[["2","4"][(["2","4"].index(key)-1)]][1] <= t1.get_pos_y())):
                    for key in ["2","4"]:
                        self.co[key][0] = t2.get_pos_x() + (self.co[key][0]-t1.get_pos_x())
                        self.co[key][1] -= t1.get_pos_y() - t2.get_pos_y()
                        self.set_tran("1",[1,1])
                        self.set_tran("2",[1,1])
                        self.set_tran("3",[1,1])
                        self.set_tran("4",[1,1])

            if t2.get_angle()  == 90:# verre le bas 
                key = "1"
                if (self.co[key][0] >= t1.get_pos_x() and (self.co[key][0] + self.co[key][2]) < t1.get_pos_x() and ((t1.get_pos_y()- 24) <=  self.co[key][1] <= t1.get_pos_y()))     and    (self.co[["1","3"][(["1","3"].index(key)-1)]][0] >= t1.get_pos_x() and (self.co[["1","3"][(["1","3"].index(key)-1)]][0] + self.co[["1","3"][(["1","3"].index(key)-1)]][2]) < t1.get_pos_x() and ((t1.get_pos_y()- 24) <=  self.co[["1","3"][(["1","3"].index(key)-1)]][1] <= t1.get_pos_y())):
                    for key in ["1","3"]:
                        self.co[key][0] = t2.get_pos_x() - (self.co["4"][1]- t1.get_pos_y())
                        self.co[key][1] = t2.get_pos_y()+ (self.co[key][1]-t1.get_pos_y())
                        self.set_tran("1",[1,0])
                        self.set_tran("3",[1,0])
                        self.set_tran("4",[0,2])
                        self.set_tran("2",[0,2])
                key = "2"
                if (self.co[key][0] >= t1.get_pos_x() and (self.co[key][0] + self.co[key][2]) < t1.get_pos_x() and ((t1.get_pos_y()- 24) <=  self.co[key][1] <= t1.get_pos_y()))     and    (self.co[["2","4"][(["2","4"].index(key)-1)]][0] >= t1.get_pos_x() and (self.co[["2","4"][(["2","4"].index(key)-1)]][0] + self.co[["2","4"][(["2","4"].index(key)-1)]][2]) < t1.get_pos_x() and ((t1.get_pos_y()- 24) <=  self.co[["2","4"][(["2","4"].index(key)-1)]][1] <= t1.get_pos_y())):
                    for key in ["2","4"]:
                        self.co[key][0] = t2.get_pos_x()
                        self.co[key][1] = t2.get_pos_y()- (7.5*(int(key)-1))+16
                        self.co[str(int(key)+1)][0] = t2.get_pos_x()+16
                        self.co[str(int(key)+1)][1] = self.co[key][1]
                        self.co[str(int(key)+1)][2] = self.co[str(int(key)+1)][3]
                        self.set_tran("1",[1,1])
                        self.set_tran("3",[1,1])
                        self.set_tran("4",[1,1])
                        self.set_tran("2",[1,1])
                        self.co[key][2] = self.co[str(int(key)+1)][2]
                        self.co[key][3] = self.co[str(int(key)+1)][3]
            if t2.get_angle()  == 270:# verre le O
                key = "1"
                if (self.co[key][0] >= t1.get_pos_x() and (self.co[key][0] + self.co[key][2]) < t1.get_pos_x() and ((t1.get_pos_y()- 24) <=  self.co[key][1] <= t1.get_pos_y()))     and    (self.co[["1","3"][(["1","3"].index(key)-1)]][0] >= t1.get_pos_x() and (self.co[["1","3"][(["1","3"].index(key)-1)]][0] + self.co[["1","3"][(["1","3"].index(key)-1)]][2]) < t1.get_pos_x() and ((t1.get_pos_y()- 24) <=  self.co[["1","3"][(["1","3"].index(key)-1)]][1] <= t1.get_pos_y())):
                    for key in ["1","3"]:
                        self.co[key][0] = t2.get_pos_x() - (self.co["4"][1]- t1.get_pos_y())
                        self.co[key][1] = t2.get_pos_y()+ (self.co[key][1]-t1.get_pos_y())+16
                        self.set_tran("1",[1,0])
                        self.set_tran("3",[1,0])
                        self.set_tran("4",[0,-2])
                        self.set_tran("2",[0,-2])
                key = "2"
                if (self.co[key][0] >= t1.get_pos_x() and (self.co[key][0] + self.co[key][2]) < t1.get_pos_x() and ((t1.get_pos_y()- 24) <=  self.co[key][1] <= t1.get_pos_y()))     and    (self.co[["2","4"][(["2","4"].index(key)-1)]][0] >= t1.get_pos_x() and (self.co[["2","4"][(["2","4"].index(key)-1)]][0] + self.co[["2","4"][(["2","4"].index(key)-1)]][2]) < t1.get_pos_x() and ((t1.get_pos_y()- 24) <=  self.co[["2","4"][(["2","4"].index(key)-1)]][1] <= t1.get_pos_y())):
                    for key in ["2","4"]:
                        self.co[key][0] = t2.get_pos_x()
                        self.co[key][1] = t2.get_pos_y()- (7.5*(int(key)-1))-16
                        self.co[str(int(key)+1)][0] = t2.get_pos_x()+16
                        self.co[str(int(key)+1)][1] = self.co[key][1]
                        self.co[str(int(key)+1)][2] = self.co[str(int(key)+1)][3]
                        self.set_tran("1",[1,1])
                        self.set_tran("3",[1,1])
                        self.set_tran("4",[1,1])
                        self.set_tran("2",[1,1])
                        self.co[key][2] = self.co[str(int(key)+1)][2]
                        self.co[key][3] = self.co[str(int(key)+1)][3]

        if t1.get_angle() == 90:    
            if t2.get_angle() == 0:
                
                if (self.co["1"][1]<= t1.get_pos_y() < self.co["1"][1]+ self.co["1"][3]  and self.co["2"][1]<= t1.get_pos_y() <= self.co["2"][1]+ self.co["2"][3] ) and (t1.get_pos_x() + 24 >= self.co["1"][0] >= t1.get_pos_x() and t1.get_pos_x() + 24 >= self.co["2"][0] >= t1.get_pos_x()):
                    for key in ["1","3"]:
                        self.co[key][1] = t2.get_pos_y() - (7.5* (int(key)-1))
                        self.co[key][0] = t2.get_pos_x() + 16
                        
                    '''for key in self.co:
                        self.co[key][2] = 0
                        self.co[key][3] = 0'''
                    self.set_tran("1",[-2,0])
                    self.set_tran("2",[0,1])
                    self.set_tran("3",[-2,0])
                    self.set_tran("4",[0,1])
                if (self.co["4"][1]<= t1.get_pos_y() <= self.co["4"][1]+ self.co["4"][3] ) and (t1.get_pos_x() + 24 >= self.co["4"][0] >= t1.get_pos_x()):
                    for key in ["2","4"]:
                        self.co[key][1] = t2.get_pos_y() - (7.5* (int(key)-2))
                        self.co[key][0] = t2.get_pos_x() -  16
                        
                        
                    self.set_tran("1",[0,0])
                    self.set_tran("2",[0,0])
                    self.set_tran("3",[0,0])
                    self.set_tran("4",[0,0])
                    """
                    self.set_tran("1",[1,1])
                    self.set_tran("2",[1,1])
                    self.set_tran("3",[1,1])
                    self.set_tran("4",[1,1])
                    
                    """
                
                

                      


class Jeux:


    def __init__(self):

        pyxel.init(384, 230,title="My Pyxel App", fps=2)
        pyxel.load("my_resource.pyxres")
        global p1
        p1 = Joueur()   
        pyxel.run(self.update, self.draw)
        

    def update(self):

        p1.commande()
        p1.actu1()
        p1.portaille()
        
        p1.colision()
        
        p1.actu2()
        

    def draw(self):

        pyxel.cls(0)  
        
        pyxel.mouse(True)
        #pyxel.camera(0,(p1.co["2"][1]+p1.co["4"][1])/2-100)
        pyxel.camera(0,-100)
        pyxel.bltm(0, -924, 0, 0, 0, 3200, 1600)
        pyxel.line(p1.co["1"][0], p1.co["1"][1], p1.co["2"][0], p1.co["2"][1], 10)
        pyxel.line(p1.co["2"][0], p1.co["2"][1], p1.co["4"][0], p1.co["4"][1], 10)
        pyxel.line(p1.co["3"][0], p1.co["3"][1], p1.co["1"][0], p1.co["1"][1], 10)
        pyxel.line(p1.co["4"][0], p1.co["4"][1], p1.co["3"][0], p1.co["3"][1], 10)
        pyxel.rect(( p1.co["1"][0] + p1.co["2"][0] )/2 , ( p1.co["1"][1] + p1.co["3"][1] )/2 , 1 , 1 , 3)
        pyxel.rect(t1.get_pos_x()-1, t1.get_pos_y(), 24, 2, 2)
        pyxel.rect(t2.get_pos_x()-1, t2.get_pos_y()-24, 6, 24, 3)
        for i in p1.co:
            pe = f"x = {p1.co[i][0]} , vit_x = {p1.co[i][2]} , y = {p1.co[i][1]} , vit_y = {p1.co[i][3]} , {t1.get_pos_y()}"

            pyxel.text(10 , p1.co["2"][1]-100 + int(i)*10,pe,0 )

class Portail:


    def __init__(self,x,y,g):
        
        self.pos_x = x
        self.pos_y = y
        self.angle = g

    def set_pos(self,x,y):
        
        self.pos_x = x
        self.pos_y = y
    def set_angle(self,a):
        self.angle = a
    def get_pos_x(self):
        return self.pos_x
    def get_pos_y(self):
        return self.pos_y
    def get_angle(self):
        return self.angle
    
global t1 , t2
t1 = Portail(100, 100, 90)
t2 = Portail(100,100,0)


Jeux()




