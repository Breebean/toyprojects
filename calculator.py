from tkinter import * #tkinter모듈 전부 호출

expression = "" #expression 변수 선언


def press(num): #expression 변수에 함수 적용
    global expression

    expression = expression + str(num)

    equation.set(expression)    #??

#마지막 expression의 값을 구하기 위한 함수
def equalpress():
    # 0으로 나누는 등의 에러를 잡아내기 위해 try except 구문 활용
    # try 블럭에 코드 생성

    try:

        global expression
        #eval - expression을 계산하기 위한 함수
        #str - 계산값을 String으로 변환해주는 함수
        total = str(eval(expresison))

        equation.set(total)
        expression = "" #expression 변수를 초기화하기 위해 빈 string  값을 넣어줌
    except: #에러 발생시 except 블럭으로 처리

        equation.set("error")
        expression = ""

def clear():    #모두 지우기 버튼 기능
    global expression
    expression = ""
    equation.set("")

#동작코드
if __name__ == "__main__": #GUI윈도우 생성
    gui = Tk()
    gui.configure(background="black") #배경색
    gui.title("나만의계산기") #상단바에 표시될 이름
    gui.geometry("265x125") #창 크기

    equation = StringVar() #가변클래스 >> 인스턴스 생성
    expression_field = Entry(gui, textvariable=equation) #입력상자(수식보여주는곳)
    expression_field.grid(columnspan=4, ipadx=70) #버튼들을 배치하기 위한 그리드

    equation.set("계산식을 입력하세요")

    button1 = Button(gui, text=' 1 ', fg='white', bg='grey',
                     command=lambda: press(1), height=1, width=7)
    button1.grid(row=2, column=0)

    button2 = Button(gui, text=' 2 ', fg='white', bg='grey',
                     command=lambda: press(2), height=1, width=7)
    button2.grid(row=2, column=1)

    button3 = Button(gui, text=' 3 ', fg='white', bg='grey',
                     command=lambda: press(3), height=1, width=7)
    button3.grid(row=2, column=2)

    button4 = Button(gui, text=' 4 ', fg='white', bg='grey',
                     command=lambda: press(4), height=1, width=7)
    button4.grid(row=3, column=0)

    button5 = Button(gui, text=' 5 ', fg='white', bg='grey',
                     command=lambda: press(5), height=1, width=7)
    button5.grid(row=3, column=1)

    button6 = Button(gui, text=' 6 ', fg='white', bg='grey',
                     command=lambda: press(6), height=1, width=7)
    button6.grid(row=3, column=2)

    button7 = Button(gui, text=' 7 ', fg='white', bg='grey',
                     command=lambda: press(7), height=1, width=7)
    button7.grid(row=4, column=0)

    button8 = Button(gui, text=' 8 ', fg='white', bg='grey',
                     command=lambda: press(8), height=1, width=7)
    button8.grid(row=4, column=1)

    button9 = Button(gui, text=' 9 ', fg='white', bg='grey',
                     command=lambda: press(9), height=1, width=7)
    button9.grid(row=4, column=2)

    button0 = Button(gui, text=' 0 ', fg='white', bg='grey',
                     command=lambda: press(0), height=1, width=7)
    button0.grid(row=5, column=0)

    plus = Button(gui, text=' + ', fg='white', bg='grey',
                  command=lambda: press("+"), height=1, width=7)
    plus.grid(row=2, column=3)

    minus = Button(gui, text=' - ', fg='white', bg='grey',
                   command=lambda: press("-"), height=1, width=7)
    minus.grid(row=3, column=3)

    multiply = Button(gui, text=' * ', fg='white', bg='grey',
                      command=lambda: press("*"), height=1, width=7)
    multiply.grid(row=4, column=3)

    divide = Button(gui, text=' / ', fg='white', bg='grey',
                    command=lambda: press("/"), height=1, width=7)
    divide.grid(row=5, column=3)

    equal = Button(gui, text=' = ', fg='white', bg='grey',
                   command=equalpress, height=1, width=7)
    equal.grid(row=5, column=2)

    clear = Button(gui, text='Clear', fg='white', bg='grey',
                   command=clear, height=1, width=7)
    clear.grid(row=5, column='1')

gui.mainloop()
