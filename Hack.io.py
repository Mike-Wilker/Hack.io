import sys
import string
import random
import tkinter as tk
import winsound
# yeah, I know the code is bad
# I had more important things to do
class BackgroundWindow(tk.Frame):
    def __init__(self, master):
        self.master = master
        super().__init__(self.master)
        self.pack()
        self.master.config(bg='black')
        self.master.overrideredirect(True)
        self.master.geometry(f'{self.master.winfo_screenwidth()}x{self.master.winfo_screenheight()}+0+0')
        self.character_rain = tk.Label(self, text='', wraplength=self.master.winfo_screenwidth(), font=('Consolas', 8), fg='green', bg='black')
        self.character_rain.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
        self.scramble_text()
        self.master.protocol('WM_DELETE_WINDOW', lambda:[])
        winsound.PlaySound('metal crusher.wav', winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_LOOP)
        FirstLevel(tk.Toplevel(self.master))
        self.mainloop()
    def scramble_text(self):
        self.master.lower()
        self.character_rain.config(text=random.choices(string.ascii_letters + string.punctuation, k=self.master.winfo_screenheight() * self.master.winfo_screenwidth() // 96))
        self.after(100, self.scramble_text)
class MainMenu(tk.Frame):
    def __init__(self, master):
        self.master = master
        super().__init__(self.master)
        self.pack()
        self.master.overrideredirect(True)
        self.master.geometry(f'+{self.master.winfo_screenwidth() // 2-200}+{self.master.winfo_screenheight() // 4}')
        self.play_button = tk.Button(self, text='Play Game', font=('Consolas', 36), bg='green', command=self.play)
        self.play_button.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
        self.instructions_label = tk.Label(self, text='Instructions: You are being hacked by a rogue AI. Exploit vulnerabilities in its code to reverse the attack against your attackers. The instructions available to you are limited to adding and subtracting one from a variable by putting + or - after it, calling functions in the same way you would a normal programming language, and entering literal values in open spaces by typing out a number.', wraplength=300, font=('Consolas', 12), bg='blue')
        self.instructions_label.grid(column=0, row=1, sticky=(tk.N, tk.W, tk.E, tk.S))
        self.credits_label = tk.Label(self, text='Credits:\nWindows SFX: Microsoft.\nError remix: 4096 @ Youtube.com\nMetal Crusher: Toby Fox\nEverything else: Michael Wilker', font=('Consolas', 12), bg='yellow')
        self.credits_label.grid(column=0, row=2, sticky=(tk.N, tk.W, tk.E, tk.S))
        self.exit_button = tk.Button(self, text='Exit', font=('Consolas', 36), bg='red', command=sys.exit)
        self.exit_button.grid(column=0, row=3, sticky=(tk.N, tk.W, tk.E, tk.S))
        self.master.protocol('WM_DELETE_WINDOW', lambda:[])
        winsound.PlaySound('error remix.wav', winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_LOOP)
        self.mainloop()
    def play(self):
        winsound.PlaySound('bong.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)
        self.play_button.config(state=tk.DISABLED)
        BackgroundWindow(tk.Toplevel(self.master))
class FirstLevel(tk.Frame):
    def __init__(self, master):
        self.master = master
        super().__init__(self.master)
        self.pack()
        self.master.geometry('+50+500')
        self.master.overrideredirect(True)
        self.lives = 3
        self.line_one = tk.Label(self, text='final a = 1', font=('Consolas', 36), bg='green')
        self.line_one.grid(column=0, row=0, columnspan=2, sticky=(tk.N, tk.W, tk.E, tk.S))
        self.line_two = tk.Label(self, text='label: restart', font=('Consolas', 36), bg='green')
        self.line_two.grid(column=0, row=1, columnspan=2, sticky=(tk.N, tk.W, tk.E, tk.S))
        self.line_three = tk.Label(self, text='vulnerability detected', font=('Consolas', 36), bg='yellow')
        self.line_three.grid(column=0, row=2, columnspan=2, sticky=(tk.N, tk.W, tk.E, tk.S))
        self.line_four = tk.Entry(self, font=('Consolas', 36), bg='yellow')
        self.line_four.grid(column=0, row=3, columnspan=2, sticky=(tk.N, tk.W, tk.E, tk.S))
        self.line_five = tk.Label(self, text='if a > 1, goto restart', font=('Consolas', 36), bg='green')
        self.line_five.grid(column=0, row=4, columnspan=2, sticky=(tk.N, tk.W, tk.E, tk.S))
        self.line_six_left = tk.Label(self, text='else,', font=('Consolas', 36), bg='green')
        self.line_six_left.grid(column=0, row=5, sticky=(tk.N, tk.W, tk.E, tk.S))
        self.line_six_right = tk.Label(self, text='failure', font=('Consolas', 36), bg='red')
        self.line_six_right.grid(column=1, row=5, sticky=(tk.N, tk.W, tk.E, tk.S))
        self.hint = tk.Label(self, text='hint: cause an infinite loop', font=('Consolas', 36), bg='blue')
        self.hint_button = tk.Button(self, text='Show Hint', font=('Consolas', 36), bg='blue', command=self.show_hint)
        self.hint_button.grid(column=0, row=7, columnspan=2, sticky=(tk.N, tk.W, tk.E, tk.S))
        self.check_button = tk.Button(self, text='Compile and Run', font=('Consolas', 36), fg='white', bg='black', command=self.check)
        self.check_button.grid(column=0, row=8, columnspan=2, sticky=(tk.N, tk.W, tk.E, tk.S))
        self.life_counter = tk.Label(self, text=f'lives: {self.lives}', font=('Consolas', 36), bg='black', fg='green')
        self.life_counter.grid(column=0, row=9, columnspan=2, sticky=(tk.N, tk.W, tk.E, tk.S))
        self.master.protocol('WM_DELETE_WINDOW', lambda:[])
        self.mainloop()
    def show_hint(self):
        winsound.PlaySound('bong.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)
        self.hint.grid(column=0, row=6, columnspan=2, sticky=(tk.N, tk.W, tk.E, tk.S))
        self.hint_button.configure(state=tk.DISABLED)
    def check(self):
        if (self.line_four.get() == 'a+'):
            winsound.PlaySound('bong.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)
            SecondLevel(tk.Toplevel(self.master))
        else:
            winsound.PlaySound('error.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)
            self.check_button.config(text='Counterattack\nFailed!', state=tk.DISABLED)
            self.after(2000, self.damage)
    def damage(self):
        self.lives -= 1
        if (self.lives > 0):
            self.life_counter.config(text=f'lives: {self.lives}')
            self.check_button.config(text='Compile and Run', state=tk.ACTIVE)
        else:
            print("yes")
            GameOver(tk.Toplevel(self.master))
class SecondLevel(tk.Frame):
    def __init__(self, master):
        self.master = master
        super().__init__(self.master)
        self.pack()
        self.master.overrideredirect(True)
        self.master.geometry(f'+{self.master.winfo_screenwidth() * 5 // 8}+100')
        self.lives = 3
        self.line_one = tk.Label(self, text='func make_you_fail()', font=('Consolas', 36), bg='green')
        self.line_one.grid(column=0, row=0, columnspan=2, sticky=(tk.N, tk.W, tk.E, tk.S))
        self.line_two = tk.Label(self, text='vulnerability detected', font=('Consolas', 36), bg='yellow')
        self.line_two.grid(column=0, row=1, columnspan=2, sticky=(tk.N, tk.W, tk.E, tk.S))
        self.line_three = tk.Entry(self, font=('Consolas', 36), bg='yellow')
        self.line_three.grid(column=0, row=2, columnspan=2, sticky=(tk.N, tk.W, tk.E, tk.S))
        self.line_four = tk.Label(self, text='failure', font=('Consolas', 36), bg='red')
        self.line_four.grid(column=0, row=3, columnspan=2, sticky=(tk.N, tk.W, tk.E, tk.S))
        self.hint = tk.Label(self, text='hint: recursion', font=('Consolas', 36), bg='blue')
        self.hint_button = tk.Button(self, text='Show Hint', font=('Consolas', 36), bg='blue', command=self.show_hint)
        self.hint_button.grid(column=0, row=5, columnspan=2, sticky=(tk.N, tk.W, tk.E, tk.S))
        self.check_button = tk.Button(self, text='Compile and Run', font=('Consolas', 36), fg='white', bg='black', command=self.check)
        self.check_button.grid(column=0, row=6, columnspan=2, sticky=(tk.N, tk.W, tk.E, tk.S))
        self.life_counter = tk.Label(self, text=f'lives: {self.lives}', font=('Consolas', 36), bg='black', fg='green')
        self.life_counter.grid(column=0, row=7, columnspan=2, sticky=(tk.N, tk.W, tk.E, tk.S))
        self.master.protocol('WM_DELETE_WINDOW', lambda:[])
        self.mainloop()
    def show_hint(self):
        winsound.PlaySound('bong.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)
        self.hint.grid(column=0, row=3, columnspan=2, sticky=(tk.N, tk.W, tk.E, tk.S))
        self.hint_button.configure(state=tk.DISABLED)
    def check(self):
        if (self.line_three.get() == 'make_you_fail()'):
            winsound.PlaySound('bong.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)
            ThirdLevel(tk.Toplevel(self.master))
        else:
            winsound.PlaySound('error.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)
            self.check_button.config(text='Counterattack\nFailed!', state=tk.DISABLED)
            self.after(2000, self.damage)
    def damage(self):
        self.lives -= 1
        if (self.lives > 0):
            self.life_counter.config(text=f'lives: {self.lives}')
            self.check_button.config(text='Compile and Run', state=tk.ACTIVE)
        else:
            GameOver(tk.Toplevel(self.master))
class ThirdLevel(tk.Frame):
    def __init__(self, master):
        self.master = master
        super().__init__(self.master)
        self.pack()
        self.master.overrideredirect(True)
        self.master.geometry(f'+{self.master.winfo_screenwidth() * 5 // 8}+{self.master.winfo_screenheight() * 1 // 2}')
        self.lives = 3
        self.line_one = tk.Label(self, text='//surely, this will work', font=('Consolas', 36), bg='green')
        self.line_one.grid(column=0, row=0, columnspan=3, sticky=(tk.N, tk.W, tk.E, tk.S))
        self.line_two = tk.Label(self, text='replace three, 2', font=('Consolas', 36), bg='green')
        self.line_two.grid(column=0, row=1, columnspan=3, sticky=(tk.N, tk.W, tk.E, tk.S))
        self.line_three = tk.Label(self, text='vulnerability detected', font=('Consolas', 36), bg='yellow')
        self.line_three.grid(column=0, row=2, columnspan=3, sticky=(tk.N, tk.W, tk.E, tk.S))
        self.line_four_left = tk.Label(self, text='replace ', font=('Consolas', 36), bg='green')
        self.line_four_left.grid(column=0, row=3, sticky=(tk.N, tk.W, tk.E, tk.S))
        self.input = tk.Entry(self, font=('Consolas', 36), bg='yellow')
        self.input.grid(column=1, row=3, sticky=(tk.N, tk.W, tk.E, tk.S))
        self.line_four_right = tk.Label(self, text=', 6', font=('Consolas', 36), bg='green')
        self.line_four_right.grid(column=2, row=3, sticky=(tk.N, tk.W, tk.E, tk.S))
        self.line_five_left = tk.Label(self, text='if three > 1, ', font=('Consolas', 36), bg='green')
        self.line_five_left.grid(column=0, row=4, columnspan=2, sticky=(tk.N, tk.W, tk.E, tk.S))
        self.line_five_right = tk.Label(self, text='failure', font=('Consolas', 36), bg='red')
        self.line_five_right.grid(column=2, row=4, columnspan=1, sticky=(tk.N, tk.W, tk.E, tk.S))
        self.hint = tk.Label(self, text='hint: replace something valuable', font=('Consolas', 36), bg='blue')
        self.hint_button = tk.Button(self, text='Show Hint', font=('Consolas', 36), bg='blue', command=self.show_hint)
        self.hint_button.grid(column=0, row=8, columnspan=3, sticky=(tk.N, tk.W, tk.E, tk.S))
        self.check_button = tk.Button(self, text='Compile and Run', font=('Consolas', 36), fg='white', bg='black', command=self.check)
        self.check_button.grid(column=0, row=9, columnspan=3, sticky=(tk.N, tk.W, tk.E, tk.S))
        self.life_counter = tk.Label(self, text=f'lives: {self.lives}', font=('Consolas', 36), bg='black', fg='green')
        self.life_counter.grid(column=0, row=10, columnspan=3, sticky=(tk.N, tk.W, tk.E, tk.S))
        self.master.protocol('WM_DELETE_WINDOW', lambda:[])
        self.mainloop()
    def show_hint(self):
        winsound.PlaySound('bong.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)
        self.hint.grid(column=0, row=7, columnspan=3, sticky=(tk.N, tk.W, tk.E, tk.S))
        self.hint_button.configure(state=tk.DISABLED)
    def check(self):
        if (self.input.get() == '1' or self.input.get() == 'failure'):
            YouWin(tk.Toplevel(self.master))
        else:
            winsound.PlaySound('error.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)
            self.check_button.config(text='Counterattack\nFailed!', state=tk.DISABLED)
            self.after(2000, self.damage)
    def damage(self):
        self.lives -= 1
        if (self.lives > 0):
            self.life_counter.config(text=f'lives: {self.lives}')
            self.check_button.config(text='Compile and Run', state=tk.ACTIVE)
        else:
            GameOver(tk.Toplevel(self.master))
        self.master.protocol('WM_DELETE_WINDOW', lambda:[])
        self.mainloop()
class YouWin(tk.Frame):
    def __init__(self, master):
        self.master = master
        super().__init__(self.master)
        self.master.config(bg='black')
        self.pack()
        self.master.overrideredirect(True)
        self.master.geometry(f'{self.master.winfo_screenwidth()}x{self.master.winfo_screenheight()}+0+0')
        self.message = tk.Label(self, text='Your data is safe... for now.\n💯', font=('Consolas', 48), fg='red', bg='white')
        self.message.grid(column=0, row=5, sticky=(tk.N, tk.W, tk.E, tk.S))
        self.master.protocol('WM_DELETE_WINDOW', lambda:[])
        winsound.PlaySound('tada.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)
        self.after(5000, sys.exit)
        self.mainloop()
class GameOver(tk.Frame):
    def __init__(self, master):
        self.master = master
        super().__init__(self.master)
        self.master.config(bg='black')
        self.pack()
        self.master.overrideredirect(True)
        self.master.geometry(f'{self.master.winfo_screenwidth()}x{self.master.winfo_screenheight()}+0+0')
        self.skull = tk.Label(self, text='''	
                             ...----....
                         ..-:"''         ''"-..
                      .-'                      '-.
                    .'              .     .       '.
                  .'   .          .    .      .    .''.
                .'  .    .       .   .   .     .   . ..:.
              .' .   . .  .       .   .   ..  .   . ....::.
             ..   .   .      .  .    .     .  ..  . ....:IA.
            .:  .   .    .    .  .  .    .. .  .. .. ....:IA.
           .: .   .   ..   .    .     . . .. . ... ....:.:VHA.
           '..  .  .. .   .       .  . .. . .. . .....:.::IHHB.
          .:. .  . .  . .   .  .  . . . ...:.:... .......:HIHMM.
         .:.... .   . ."::"'.. .   .  . .:.:.:II;,. .. ..:IHIMMA
         ':.:..  ..::IHHHHHI::. . .  ...:.::::.,,,. . ....VIMMHM
        .:::I. .AHHHHHHHHHHAI::. .:...,:IIHHHHHHMMMHHL:. . VMMMM
       .:.:V.:IVHHHHHHHMHMHHH::..:" .:HIHHHHHHHHHHHHHMHHA. .VMMM.
       :..V.:IVHHHHHMMHHHHHHHB... . .:VPHHMHHHMMHHHHHHHHHAI.:VMMI
       ::V..:VIHHHHHHMMMHHHHHH. .   .I":IIMHHMMHHHHHHHHHHHAPI:WMM
       ::". .:.HHHHHHHHMMHHHHHI.  . .:..I:MHMMHHHHHHHHHMHV:':H:WM
       :: . :.::IIHHHHHHMMHHHHV  .ABA.:.:IMHMHMMMHMHHHHV:'. .IHWW
       '.  ..:..:.:IHHHHHMMHV" .AVMHMA.:.'VHMMMMHHHHHV:' .  :IHWV
        :.  .:...:".:.:TPP"   .AVMMHMMA.:. "VMMHHHP.:... .. :IVAI
       .:.   '... .:"'   .   ..HMMMHMMMA::. ."VHHI:::....  .:IHW'
       ...  .  . ..:IIPPIH: ..HMMMI.MMMV:I:.  .:ILLH:.. ...:I:IM
     : .   .'"' .:.V". .. .  :HMMM:IMMMI::I. ..:HHIIPPHI::'.P:HM.
     :.  .  .  .. ..:.. .    :AMMM IMMMM..:...:IV":T::I::.".:IHIMA
     'V:.. .. . .. .  .  .   'VMMV..VMMV :....:V:.:..:....::IHHHMH
       "IHH:.II:.. .:. .  . . . " :HB"" . . ..PI:.::.:::..:IHHMMV"
        :IP""HHII:.  .  .    . . .'V:. . . ..:IH:.:.::IHIHHMMMMM"
        :V:. VIMA:I..  .     .  . .. . .  .:.I:I:..:IHHHHMMHHMMM
        :"VI:.VWMA::. .:      .   .. .:. ..:.I::.:IVHHHMMMHMMMMI
        :."VIIHHMMA:.  .   .   .:  .:.. . .:.II:I:AMMMMMMHMMMMMI
        :..VIHIHMMMI...::.,:.,:!"I:!"I!"I!"V:AI:VAMMMMMMHMMMMMM'
        ':.:HIHIMHHA:"!!"I.:AXXXVVXXXXXXXA:."HPHIMMMMHHMHMMMMMV
          V:H:I:MA:W'I :AXXXIXII:IIIISSSSSSXXA.I.VMMMHMHMMMMMM
            'I::IVA ASSSSXSSSSBBSBMBSSSSSSBBMMMBS.VVMMHIMM'"'
             I:: VPAIMSSSSSSSSSBSSSMMBSSSBBMMMMXXI:MMHIMMI
            .I::. "H:XIIXBBMMMMMMMMMMMMMMMMMBXIXXMMPHIIMM'
            :::I.  ':XSSXXIIIIXSSBMBSSXXXIIIXXSMMAMI:.IMM
            :::I:.  .VSSSSSISISISSSBII:ISSSSBMMB:MI:..:MM
            ::.I:.  ':"SSSSSSSISISSXIIXSSSSBMMB:AHI:..MMM.
            ::.I:. . ..:"BBSSSSSSSSSSSSBBBMMMB:AHHI::.HMMI
            :..::.  . ..::":BBBBBSSBBBMMMB:MMMMHHII::IHHMI
            ':.I:... ....:IHHHHHMMMMMMMMMMMMMMMHHIIIIHMMV"
              "V:. ..:...:.IHHHMMMMMMMMMMMMMMMMHHHMHHMHP'
               ':. .:::.:.::III::IHHHHMMMMMHMHMMHHHHM"
                 "::....::.:::..:..::IIIIIHHHHMMMHHMV"
                   "::.::.. .. .  ...:::IIHHMMMMHMV"
                     "V::... . .I::IHHMMV"'
                       '"VHVHHHAHHHHMMV:"
                You got hacked!''', font=('Consolas', 12 * self.master.winfo_screenheight() // 1080), fg='green', bg='black')
        self.skull.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
        master.protocol('WM_DELETE_WINDOW', lambda:[])
        winsound.PlaySound('shutdown.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)
        self.after(5000, sys.exit)
        self.mainloop()
def main():
    MainMenu(tk.Tk())
if __name__ == '__main__':
    main()