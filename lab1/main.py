import tkinter as tk
import convert_numbers


def main():
    root = tk.Tk()

    main_frame = tk.Frame(root, width=500, height=200, bg='white')
    main_frame.pack(side='top')

    res1 = tk.StringVar(value='')
    res2 = tk.StringVar(value='')

    input_10 = tk.Text(main_frame, width=200, height=50, bg='gray', fg='black', font='Arial 20')
    output_8 = tk.Label(main_frame, width=200, height=50, bg='gray', fg='black', font='Arial 20', textvariable=res1)
    input_8 = tk.Text(main_frame, width=200, height=50, bg='gray', fg='black', font='Arial 20')
    output_10 = tk.Label(main_frame, width=200, height=50, bg='gray', fg='black', font='Arial 20', textvariable=res2)
    button1 = tk.Button(main_frame, text='=', font='Arial 32', bg='gray', fg='black')
    button2 = tk.Button(main_frame, text='=', font='Arial 32', bg='gray', fg='black')

    button1.bind('<Button-1>', lambda *args: res1.set(maths.from_dec_to_oct(float(input_10.get('1.0', 'end')))))
    button2.bind('<Button-1>', lambda *args: res2.set(maths.from_oct_to_dec(input_8.get('1.0', 'end').strip())))

    input_10.place(x=20, y=20, width=200, height=36)
    button1.place(x=230, y=20, width=40, height=36)
    output_8.place(x=280, y=20, width=200, height=36)
    input_8.place(x=20, y=80, width=200, height=36)
    button2.place(x=230, y=80, width=40, height=36)
    output_10.place(x=280, y=80, width=200, height=36)

    keyboard = tk.Frame(root, width=500, height=300)
    keyboard.pack(side='bottom')
    keys = [tk.Button(keyboard, width=50, )]

    root.mainloop()


if __name__ == '__main__':
    main()
