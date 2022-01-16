import numpy as np
import matplotlib.pyplot as plt
# NO other imports are allowed

class Shape:
    '''
    DO NOT MODIFY THIS CLASS

    DO NOT ADD ANY NEW METHODS TO THIS CLASS
    '''
    def __init__(self):
        self.T_s = None
        self.T_r = None
        self.T_t = None
    
    
    def translate(self, dx, dy):
        '''
        Polygon and Circle class should use this function to calculate the translation
        '''
        self.T_t = np.array([[1, 0, dx], [0, 1, dy], [0, 0, 1]])
 

    def scale(self, sx, sy):
        '''
        Polygon and Circle class should use this function to calculate the scaling
        '''
        self.T_s = np.array([[sx, 0, 0], [0, sy, 0], [0, 0, 1]])
 
        
    def rotate(self, deg):
        '''
        Polygon and Circle class should use this function to calculate the rotation
        '''
        rad = deg*(np.pi/180)
        self.T_r = np.array([[np.cos(rad), np.sin(rad), 0],[-np.sin(rad), np.cos(rad),0], [0, 0, 1]])

        
    def plot(self, x_dim, y_dim):
        '''
        Polygon and Circle class should use this function while plotting
        x_dim and y_dim should be such that both the figures are visible inside the plot
        '''
        x_dim, y_dim = 1.2*x_dim, 1.2*y_dim
        plt.plot((-x_dim, x_dim),[0,0],'k-')
        plt.plot([0,0],(-y_dim, y_dim),'k-')
        plt.xlim(-x_dim,x_dim)
        plt.ylim(-y_dim,y_dim)
        plt.grid()
        plt.show()



class Polygon(Shape):
    '''
    Object of class Polygon should be created when shape type is 'polygon'
    '''
    def __init__(self, A):
        '''
        Initializations here
        '''
        self.A=A.copy()                              #To store the values before Transformation   
        self.A_new=A.copy()                          #To store the values after Transformation   
        self.A=np.array(self.A,dtype='float')
        self.A_new=np.array(self.A_new,dtype='float')
       
 
    
    def translate(self, dx, dy=None):
        '''
        Function to translate the polygon
    
        This function takes 2 arguments: dx and dy
    
        This function returns the final coordinates
        '''
        if dy==None:
            dy=dx
            
        A=self.A_new.copy()
        
        Shape.translate(self, dx, dy)               #generate translation matrix using inheritance

        for i in range(len(self.A_new)):
            self.A_new[i]= np.matmul(self.T_t,self.A_new[i],dtype='float')

        for i in range(len(self.A_new)):
            for j in range(len(self.A_new[i])):
                self.A_new[i][j]=round(self.A_new[i][j],2)

        self.A=A.copy()                             #store the values before transformation
        return (self.A_new[:,0],self.A_new[:,1])

    
    def scale(self, sx, sy = None):
        '''
        Function to scale the polygon
    
        This function takes 2 arguments: sx and sx
    
        This function returns the final coordinates
        '''
        A=self.A_new.copy()                         
        if sy==None:
            sy=sx
        x_c=0
        y_c=0
        n=0
        for i in range(len(self.A_new)):
            x_c+=self.A_new[i][0]
            y_c+=self.A_new[i][1]
            n+=1

        x_c/=n                          #center of the figure (x coordinate)
        y_c/=n                          #center of the figure (y coordinate)
        
        self.translate(-x_c,-y_c)       #Takes the center at origin (change of coordinates) 
        Shape.scale(self,sx,sy)         #genarate scaling matrix using inheritance
        
        for i in range(len(self.A_new)):
            self.A_new[i]= np.matmul(self.T_s,self.A_new[i],dtype='float32')

        self.translate(x_c,y_c)         #Takes back to standard coordinates axis
        for i in range(len(self.A_new)):
            for j in range(len(self.A_new[i])):
                self.A_new[i][j]=round(self.A_new[i][j],2)
        
        self.A=A.copy()                     #store the values before transformation
        return (self.A_new[:,0],self.A_new[:,1])
        
    
    def rotate(self, deg, rx = 0, ry = 0):
        '''
        Function to rotate the polygon
    
        This function takes 3 arguments: deg, rx(optional), ry(optional). Default rx and ry = 0. (Rotate about origin)
    
        This function returns the final coordinates
        '''
        A=self.A_new.copy()
        
        self.translate(-rx,-ry)         #Takes (rx,ry) to origin 
        Shape.rotate(self,deg)          #generate rotation matrix using inheritance
        for i in range(len(self.A_new)):
            self.A_new[i] = (np.matmul(self.T_r,self.A_new[i],dtype='float32'))
            
        for i in range(len(self.A_new)):
            for j in range(len(self.A_new[i])):
                self.A_new[i][j]=round(self.A_new[i][j],2)

        self.translate(rx,ry)
        self.A=A.copy()                 #store the values before transformation
        return (self.A_new[:,0],self.A_new[:,1])
        
    

    def plot(self):
        '''
        Function to plot the polygon
    
        This function should plot both the initial and the transformed polygon
    
        This function should use the parent's class plot method as well
    
        This function does not take any input
    
        This function does not return anything
        '''
        
        a1=np.append(self.A[:,0],[self.A[0][0]])
        a2 =np.append(self.A[:,1],[self.A[0][1]])
        plt.plot(a1,a2,linestyle='--')
        max1x=max(max(self.A[:,0]),abs(min(self.A[:,0])))
        max1y=max(max(self.A[:,1]),abs(min(self.A[:,0])))       
        a1=np.append(self.A_new[:,0],[self.A_new[0][0]])        #To plot figure in clockwise order before transformation
        a2 =np.append(self.A_new[:,1],[self.A_new[0][1]])       #To plot figure in clockwise order before transformation
        plt.plot(a1,a2)
        max2x=abs(max(self.A_new[:,0]))                         #To plot figure in clockwise order after transformation
        max2y=abs(max(self.A_new[:,1]))                         #To plot figure in clockwise order after transformation
        x_dim=2*max(max1x,max2x)
        y_dim=2*max(max1y,max2y)
        
        Shape.plot(self,max(x_dim,y_dim),max(x_dim,y_dim))    
            

class Circle(Shape):
    '''
    Object of class Circle should be created when shape type is 'circle'
    '''
    def __init__(self, x=0, y=0, radius=5):
        '''
        Initializations here
        '''
        self.x=x                            #To store the values before transformation
        self.y=y 
        self.radius=radius
        self.x_new=x                        #To store the values after transformation
        self.y_new=y
        self.radius_new=radius
    

    
    def translate(self, dx, dy=None):
        '''
        Function to translate the circle
    
        This function takes 2 arguments: dx and dy (dy is optional).
    
        This function returns the final coordinates and the radius
        '''
        x=self.x_new
        y=self.y_new
        radius=self.radius_new        
        if dy==None:
            dy=dx
        Shape.translate(self, dx, dy)                       #generate translation matrix using inheritance
        arr=np.array([self.x_new,self.y_new,1])
        Transformation=np.matmul(self.T_t,arr)
        self.x_new=round(Transformation[0],2)               #value after translation
        self.y_new=round(Transformation[1],2)               
        self.x=x                                            #store value before translation
        self.y=y
        self.radius=radius
        return (self.x_new,self.y_new,self.radius_new)

        
    def scale(self, sx):
        '''
        Function to scale the circle
    
        This function takes 1 argument: sx
    
        This function returns the final coordinates and the radius
        '''
        x=self.x_new
        y=self.y_new
        radius=self.radius_new
        Shape.scale(self,sx,sx)                         #generate scaling matrix using inheritance
        dx=self.x_new
        dy=self.y_new
        self.translate(-dx,-dy)                         #Takes the center at origin
        x_c=self.x_new-self.radius_new                  #a point on the circle (x_c,y_c) 
        y_c=self.y_new
        arr=np.array([x_c,y_c,1])
        Transformation=np.matmul(self.T_s,arr)          
        x_c=Transformation[0]
        y_c=Transformation[1]
        self.radius_new=  round((((abs(x_c-self.x_new))**2)+((abs(y_c-self.y_new))**2))**0.5,2)         #calculation of radius using distance formula
        self.translate(dx,dy)                           #Takes back to standard coordinate axis
        self.x=x
        self.y=y
        self.radius=radius
        return (self.x_new,self.y_new,self.radius_new)   
 
    
    def rotate(self, deg, rx = 0, ry = 0):
        '''
        Function to rotate the circle
    
        This function takes 3 arguments: deg, rx(optional), ry(optional). Default rx and ry = 0. (Rotate about origin)
    
        This function returns the final coordinates and the radius
        '''
        x=self.x_new
        y=self.y_new
        radius=self.radius_new

        Shape.rotate(self, deg)                         #generate rotation matrix using inheritance
        self.translate(-rx,-ry)                         #Takes the point (rx,ry) at origin
        arr=np.array([self.x_new,self.y_new,1])
        Transformation=np.matmul(self.T_r,arr)
        self.x_new=round(Transformation[0],2)
        self.y_new=round(Transformation[1],2)

        self.translate(rx,ry)                           #Takes back to standard coordinate axis
        self.x=x
        self.y=y
        self.radius=radius
        return (self.x_new,self.y_new,self.radius_new)

    def plot(self):
        '''
        Function to plot the circle
    
        This function should plot both the initial and the transformed circle
    
        This function should use the parent's class plot method as well
    
        This function does not take any input
    
        This function does not return anything
        '''
        n=64
        t=np.linspace(0,2*np.pi,n+1)                
        x=self.radius*np.cos(t)+self.x                  #plotting a circle before transformation using the parametric equation of circle
        y=self.radius*np.sin(t)+self.y
        plt.plot(x,y,linestyle='--')
        x=self.radius_new*np.cos(t)+self.x_new          #plotting a circle after transformation using the parametric equation of circle
        y=self.radius_new*np.sin(t)+self.y_new
        plt.plot(x,y)
        
        x_dim=2*max(max(self.x+self.radius,self.x_new+self.radius_new), abs(min(self.x-self.radius,self.x_new-self.radius_new)))   
        y_dim=2*max(max(self.y+self.radius,self.y_new+self.radius_new), abs(min(self.y-self.radius,self.y_new-self.radius_new)))
        Shape.plot(self,max(x_dim,y_dim),max(x_dim,y_dim))
                

if __name__ == "__main__":
    '''
    Add menu here as mentioned in the sample output section of the assignment document.
    '''
    
    verbose=int(input('verbose? 1 to plot, 0 otherwise: '))
    test_cases=int(input('Enter the number of test cases: '))
    for i in range(test_cases):
        shape=int(input('Enter type of shape (polygon/circle): '))
        if shape==0:
            sides=int(input('Enter the number of sides: '))
            a=[]
            for j in range(sides):
                x,y=input('enter (x{0}, y{0}): '.format(j+1)).split()
                x=float(x)
                y=float(y)
                l=[x,y,1]
                a.append(l)
            queries= int(input('Enter the number of queries: '))
            A=np.array(a,dtype='float32')
            p=Polygon(A)
            
            
            
            
            for k in range(queries):
                print('''
Enter Query:
1) R deg (rx) (ry)
2) T dx (dy)
3) S sx (sy)
4) P
                ''')
                query=input()
                query=query.split()
                if query[0]=='R':
                    for index in range(1,len(query)):
                        query[index]=float(query[index])
                            
                    if len(query)==2:
                        p.rotate(query[1])
                    elif len(query)==3:
                        p.rotate(query[1],query[2])
                    elif len(query)==4:
                        p.rotate(query[1],query[2],query[3])

                            

                elif query[0]=='T':
                    for index in range(1,len(query)):
                        query[index]=float(query[index])

                    if len(query)==2:
                        p.translate(query[1])
                    elif len(query)==3:
                        p.translate(query[1],query[2])

                elif query[0]=='S':
                    for index in range(1,len(query)):
                        query[index]=float(query[index])

                    if len(query)==2:
                        p.scale(query[1])
                    elif len(query)==3:
                        p.scale(query[1],query[2])

                            
                elif query[0]=='P':
                    p.plot()
                    

                print(*p.A[:,0],*p.A[:,1])    
                print(*p.A_new[:,0],*p.A_new[:,1])
                    
                if verbose==1:
                    p.plot()

        if shape==1:
            a,b,r=input('Enter Centre(x,y) and radius : (space separated) ').split()
            a=float(a)
            b=float(b)
            r=float(r)
            c=Circle(a,b,r)
            queries= int(input('Enter the number of queries: '))
            
            for k in range(queries):
                print('''
Enter Query:
1) R deg (rx) (ry)
2) T dx (dy)
3) S sx 
4) P
                ''')
                query=input()
                query=query.split()
                if query[0]=='R':
                    for index in range(1,len(query)):
                        query[index]=float(query[index])
                            
                    if len(query)==2:
                        c.rotate(query[1])
                    elif len(query)==3:
                        c.rotate(query[1],query[2])
                    elif len(query)==4:
                        c.rotate(query[1],query[2],query[3])

                            

                elif query[0]=='T':
                    for index in range(1,len(query)):
                        query[index]=float(query[index])

                    if len(query)==2:
                        c.translate(query[1])
                    elif len(query)==3:
                        c.translate(query[1],query[2])

                elif query[0]=='S':
                    for index in range(1,len(query)):
                        query[index]=float(query[index])

                    if len(query)==2:
                        c.scale(query[1])

                            
                elif query[0]=='P':
                    c.plot()
                    
                    
                print(c.x,c.y,c.radius)
                print(c.x_new,c.y_new,c.radius_new)
                    
                if verbose==1:
                    c.plot()
            
            
        


