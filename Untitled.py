
# coding: utf-8

# In[ ]:

#封装（encapsulation）就是把一组相关的功能用一个盒子装起来


# In[3]:

class Person:
    def set_name(self,name):
        self.name=name
    
    def get_name(self):
        return self.name
    
    def greet(self):
        print("Hello,I'm {}".format(self.name))
        
za=Person()#创建类的实例
za.set_name("za")
za.greet()
Li=Person()#创建类的实例
Li.set_name("li")
Li.greet()


# In[14]:

class Person:
    def __init__(self,name=None):#构造函数，双下划线，建立对象时自动调用
        self.name=name
    
    def set_name(self,name):
        self.name=name
    
    def get_name(self):
        return self.name
    
    def greet(self):
        print("Hello,I'm {}".format(self.name))
        
za=Person('za')
za.greet()


# In[34]:

class Person:
    count=0
    
    def __init__(self,name=None):#构造函数，双下划线，建立对象时自动调用
        self.name=name
        Person.count+=1
        print(Person.count)
    
    def set_name(self,name):
        #assert(isinstance(nane,str))
        if isinstance(name,str):
            self.name=name
        else:
            print("not a vilid name")
        self.name=name
    
    def get_name(self):
        return self.name
    
    def greet(self):
        print("Hello,I'm {}".format(self.name))
        
za=Person("sf")
za.greet()


# In[18]:

help(list)


# In[20]:

#多态：同一形式，多种结果
1+2


# In[21]:

'a'+'b'


# In[22]:

print("hello".count("e"))


# In[23]:

print([1,2,3,"e","e",4].count("e"))


# In[24]:

my_list=['Hello',[1,2,3,"e","e"]]
for item in my_list:
    print(item.count("e"))


# In[31]:

class Cat:
    def meow(self):
        print("meow...")
        
class Dog:
    def wang(self):
        print("wang,wang..")
        
pets=list()
pets.append(Cat())
pets.append(Dog())

for item in pets:
    if isinstance(item,Cat):
        item.meow()
    elif isinstance(item,Dog):
        item.wang()
    else:
        pass


# In[30]:

class Cat:
    def talk(self):
        print("meow...")
        
class Dog:
    def talk(seld):
        print("wang,wang..")
        
pets=[Cat(),Dog(),Cat()]

for item in pets:
    item.talk()


# In[32]:

def add(a,b):
    return a+b

a=1
b=2
print(add(a,b))
x,y="a",'b'
print(add(x,y))


# In[35]:

#inheritence子类继承父类所有的方法和属性
class student(Person):
    def set_score(self,score):
        self.__score=score
    def get_score(self):
        return self.__score
    def show_score(self):
        print("My score is {}".format(self.__score))
zs=student()
zs.set_name("zhangsan")
zs.set_score(100)
zs.greet()
zs.show_score()


# In[38]:

#inheritence子类继承父类所有的方法和属性
class student(Person):
    def set_score(self,score):
        self.__score=score
    def get_score(self):
        return self.__score
    def show_score(self):
        print("My score is {}".format(self.__score))
    def greet(self):
        Person.greet(self)
        self.show_score()
zs=student()
zs.set_name("zhangsan")
zs.set_score(100)
zs.greet()
zs.show_score()


# In[39]:

#inheritence子类继承父类所有的方法和属性
class student(Person):
    def __init__(self,name=None):
        Person.__init__(self,name)
        self.__score=60
        
    def set_score(self,score):
        self.__score=score
    def get_score(self):
        return self.__score
    def show_score(self):
        print("My score is {}".format(self.__score))
    def greet(self):
        Person.greet(self)
        self.show_score()
zs=student()
zs.set_name("zhangsan")
zs.set_score(100)
zs.greet()
zs.show_score()


# In[43]:

people=list()
zs=Person("zhangsan")
ls=student("Lisi")
ls.set_score(100)
people.append(zs)
people.append(ls)

for p in people:
    p.greet()


# In[44]:

issubclass(student,Person)


# In[45]:

isinstance(zs,Person)


# In[46]:

isinstance(zs,student)


# In[47]:

isinstance(ls,Person)


# In[49]:

isinstance(ls,student)


# In[51]:

ls.__class__


# In[3]:

class Filter:
    def __init__(self):
        self.blocked=[]
    def filter(self,sequence):
        return[x for x in sequence if x not in self.blocked]
class SpamFilter(Filter):
    def __init__(self):
        self.blocked=["SPAM"]
f=SpamFilter()
f.filter([1,2,3])


# In[4]:

sf=SpamFilter()
sf.filter(["SAPM","spam","bacon","egg"])


# In[76]:

#不要使用多重继承
class Calculator:
    def calculate(self,expression):
        self.value=eval(expression)
class Talker:
    def talk(self):
        print("My value is",self.value)
class TalkingCalculator(Calculator,Talker):
    pass

tc=TalkingCalculator()
tc.calculate('1+2+3')
tc.talk()


# In[82]:

class Calculator:
    def calculate(self,expression):
        return eval(expression)
class Talker:
    def talk(self,value):
        print("My value is",value)
class TalkingCalculator():
    def __init__(self):
        self.__calculator=Calculator()
        self.__talker=Talker()
        self.__value=None
        
    def calculate(self,expression):
        self.__value=self.__calculator.calculate(expression)
    def talk(self):
        self.__talker.talk(self.__value)


tc=TalkingCalculator()
tc.calculate('1+2+3')
tc.talk()


# In[ ]:



