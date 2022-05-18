"""
Пример П4.19.
    Простая модель полимера в растворе интерпретирует его как последовательность случайно ориентированных сегментов, т.е. не существует связи между
ориентацией какого-либо сегмента и любого другого сегмента (это так называемая модель случайного перемещения (случайного блуждения) в пространстве.)
"""

"""
    Определим класс Polymer для описания такого полимера. В этом классе позиции сегментов хранится в списке кортежей (x,y,z).
Объект Polymer будет инициализироваться значениями N и а - количеством сегментов и длиной сегмента соотвественно. Метод инициализации вызывает метод
make_polymer для заполнения списка позиции сегментов.


    Объект Polymer также вычисляет общее расстояние между противоположными концами полимера и реализует метод calc_Rg для вычисления и возврата радиуса инерции полимера
"""

import math
import random

class Polymer:
    """
    Класс, представляющий модель случайного перемещения полимера в растворе.
    """
    def __init__(self,N,a):

        """
        Инициализация объекта Polymer с N сегментами и длиной каждого сегмента а.
        """
        self.N,self.a = N,a
        self.xyz = [(None,None,None)] * N
        self.R = None
        self.make_polymer()

    def make_polymer(self):
        """
        Вычисление позиций сегментов, центра масс и общего расстояния между противоположными концами модели случайного перемещения полимера в растворе.
        """

        self.xyz = x,y,z = cx, cy, cz = 0,0,0
        for i in range  (1,self.N):
            theta = math.acos(2*random.random() - 1)
            phi = random.random() * 2. * math.pi

            x += self.a * math.sin(theta) * math.cos(phi)
            y += self.a * math.sin(theta) * math.sin(phi)
            z += self.a * math.cos(theta)

            self.xyz[i] = x,y,z
            cx,cy,cz = cx + x, cy+ y,cz + z
        cx,cy,cz = cx / self.N, cy / self.N, cz / self.N
        self.R = x,y,z

        for i in range(self.N):
            self.xyz[i] = (self.xyz[i][0] - cx, self.xyz[i][1] - cy, self.xyz[i][2] - cz)


    def calc_Rg(self):

        self.Rg = 0
        for x,y,z in self.xyz:
            self.Rg += x**2 + y**2 + z**2
        self.Rg = math.sqrt(self.Rg / self.N)
        return self.Rg

