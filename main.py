import time

print("Welcome to Treasure Island.")
time.sleep(0.5)
print(''' ____________________________________________________________________
 / \-----     ---------  -----------     -------------- ------    ----\
 \_/__________________________________________________________________/
 |~ ~~ ~~~ ~ ~ ~~~ ~ _____.----------._ ~~~  ~~~~ ~~   ~~  ~~~~~ ~~~~|
 |  _   ~~ ~~ __,---'_       "         `. ~~~ _,--.  ~~~~ __,---.  ~~|
 | | \___ ~~ /      ( )   "          "   `-.,' (') \~~ ~ (  / _\ \~~ |
 |  \    \__/_   __(( _)_      (    "   "     (_\_) \___~ `-.___,'  ~|
 |~~ \     (  )_(__)_|( ))  "   ))          "   |    "  \ ~~ ~~~ _ ~~|
 |  ~ \__ (( _( (  ))  ) _)    ((     \\//    " |   "    \_____,' | ~|
 |~~ ~   \  ( ))(_)(_)_)|  "    ))    //\\ " __,---._  "  "   "  /~~~|
 |    ~~~ |(_ _)| | |   |   "  (   "      ,-'~~~ ~~~ `-.   ___  /~ ~ |
 | ~~     |  |  |   |   _,--- ,--. _  "  (~~  ~~~~  ~~~ ) /___\ \~~ ~|
 |  ~ ~~ /   |      _,----._,'`--'\.`-._  `._~~_~__~_,-'  |H__|  \ ~~|
 |~~    / "     _,-' / `\ ,' / _'  \`.---.._          __        " \~ |
 | ~~~ / /   .-' , / ' _,'_  -  _ '- _`._ `.`-._    _/- `--.   " " \~|
 |  ~ / / _-- `---,~.-' __   --  _,---.  `-._   _,-'- / ` \ \_   " |~|
 | ~ | | -- _    /~/  `-_- _  _,' '  \ \_`-._,-'  / --   \  - \_   / |
 |~~ | \ -      /~~| "     ,-'_ /-  `_ ._`._`-...._____...._,--'  /~~|
 | ~~\  \_ /   /~~/    ___  `---  ---  - - ' ,--.     ___        |~ ~|
 |~   \      ,'~~|  " (o o)   "         " " |~~~ \_,-' ~ `.     ,'~~ |
 | ~~ ~|__,-'~~~~~\    \"/      "  "   "    /~ ~~   O ~ ~~`-.__/~ ~~~|
 |~~~ ~~~  ~~~~~~~~`.______________________/ ~~~    |   ~~~ ~~ ~ ~~~~|
 |____~jrei~__~_______~~_~____~~_____~~___~_~~___~\_|_/ ~_____~___~__|
 / \----- ----- ------------  ------- ----- -------  --------  -------\
 \_/__________________________________________________________________/''')
print("Your mission is to find the treasure.")
start = input("Type begin to start. \n").lower()
if start == 'begin':
    print('''
        It's april 1st, you wake up and find yourself stranded on an island
                   
                     %%%%
                    %%%%-(
                  _%%%%%_/                        \ ' /
                _%%%%%%%%                        - (_) -
              _%%%%%%%/ \%                        / , \
             %%%%%%%%%\\ \_
               %%%%%%   \ \\
                   )    /\_/
                 /(___. \
                 '----' (
                /       )
    ---....____/        (_____ __ _ ___ ___ __ _ _ _____ _ _ ___
              /         )---...___ =-= = -_= -=_= _-=_-_ -=- =-_
            ,'          (         ```--.._= -_= -_= _-=- -_= _=-
         ,-'            )                 ``--._=-_ =-=_-= _-= _
         '-._    '-..___(                       ``-._=_-=_- =_-=
             ``---....__)                            `-._-=_-_=-
                   )|)|                                  `-._=-_
                  '-'-.\_                                    `-.

        You look around and see a dark scary path into the forest but that's your only option

''')

decision1 = input('You walk into the forest and come across a cross road... Where do you want to go? Type "left" or "right". \n').lower()

if decision1 == 'right':
    print(" uh oh you fell into a boobie trap and died. Game over!")
elif decision1 == 'left':
    decision2 = input('You keep walking until you find yourself blocked by a lake. What do you want to do? Type "swim" to swim across or "wait" to wait for boat \n').lower()
    if decision2 == 'swim':
        print('''
                                      A MONSTER APPEARS
                                              ,--,  ,.-.
                            ,                   \,       '-,-`,'-.' | ._
                           /|           \    ,   |\         }  )/  / `-,',
                           [ '          |\  /|   | |        /  \|  |/`  ,`
                           | |       ,.`  `,` `, | |  _,...(   (      _',
                           \  \  __ ,-` `  ,  , `/ |,'      Y     (   \_L\
                            \  \_\,``,   ` , ,  /  |         )         _,/
                             \  '  `  ,_ _`_,-,<._.<        /         /
                              ', `>.,`  `  `   ,., |_      |         /
                                \/`  `,   `   ,`  | /__,.-`    _,   `\
                            -,-..\  _  \  `  /  ,  / `._) _,-\`       \
                             \_,,.) /\    ` /  / ) (-,, ``    ,        |
                            ,` )  | \_\       '-`  |  `(               \
                           /  /```(   , --, ,' \   |`<`    ,            |
                          /  /_,--`\   <\  V /> ,` )<_/)  | \      _____)
                    ,-, ,`   `   (_,\ \    |   /) / __/  /   `----`
                   (-, \           ) \ ('_.-._)/ /,`    /
                   | /  `          `/ \\ V   V, /`     /
                ,--\(        ,     <_/`\\     ||      /
               (   ,``-     \/|         \-A.A-`|     /
              ,>,_ )_,..(    )\          -,,_-`  _--`
             (_ \|`   _,/_  /  \_            ,--`
              \( `   <.,../`     `-.._   _,-`
               `                      ```
                                    It grabs you...
                ''')

        time.sleep(5)
        print('''
                                             ,---._
                                                     ,~~,-._  `._
                                                      v'~   `-.  `.
                                                           _,- ~.  \
                                                         .'  ,--`.  `\_
                                                         V-'~ ,'~~~`-. `-.
                                             ___             /_/~~~) ` `. `._
                                    ____,---'   ;            V     `.__ `--, `;
                                     `-._    ;  `.                ____)       :
                                         `.;  ; .'              ,'        _    |
                                          ; |   ;              ,';'~~~`--' `;  :
                                         ,': .-'               `,'  __ __   :  |
                                         )_  `-, ___     __        (__:__)   ; ;
                                    _,---. \___,'` ~`---;  `-.       |||    ;  ;
                                _,-/   :;     !   `     `|    `-.   |~~~~|   ; :
                            _,-' /~   .,'  ;  !!  `..    ``.    `.  :    ;  | :
                          ,'  ,-'    .;   `; !!   _,'-' ,--._    ====\__/===: `.
                        .'  ,-'   ,--.  ~~`-. !!  ~    ,'    `     `./  \   |  |
                       .'  :;   ,'    \        !: .   ;--.__   `;.  |. ~.|   : ;
                      .'  ,;    ' ,-'~~`-.     ,!  ;-'     #;   `;. \____/  : `.
                     .'  ,;      /__      `-._,'!!( _(0'~~`-'    `;.  `.     ; ;
                    .'  ,;    ,'    `---._(0))  !! ~   _,-,        `;  `.   ;  :
                    ;  ,;    ,' ;;-.__,-._~~~   !!__,--::::|.      `;:  :   `; )
                    ;  :|   ,'  ;/;;; :::;;;;----'|:: |::;\/#.      `;  |    ) ;
                    :  |:  ,'  ,' :/  :;; \/))):;;::/  ::' ##:      ;;  ;    ; |
                    |  :|  :;  :      `'    \/ \/ `'   `'  ##;      ;  .'  ,'  ;
                    :  |;  || .'        ;\.   ____ __,--._ ##;     ;' .'--'   ;
                _,--`. `.  :: `./;   /\/;:;,-'    `-.     `--.__     .'~   ,'~
               /     ;. `; ``. :::;\;.-'~~`./~~\/\ ..    _  :::  --. ' ,-'~
              /    .  `. `; `   ~~~ ;~      ~~~~~~`--.__~~`-. :::   ) ~
             /'    ;`--`. `. `.    :;      `;       ;   `---`._    ,'
             `.  \/      `-.` `_,_ `:,-'-. `.      :_,_    ;   `--'
              `.  `.        ` (___)-: ( ) :--,-'- -(___),'~~~`.
               {_  `.               `.___.' ( ; ;)      :((:)):
                 `.  `                       `--'       `.___.'
                   `. `.                 ;;:::;
                    `-  `.              ;;;o o;
                      `-. `.__        \\;;; - ;; //
                         `. ` `--..___ \\,--v-, //      
                           `--._   ~~~~~`)____(//
                                )    ~~   ~~~~~~;
                                `.    ~~  ------;
                                 `.~~_   ______,' 
                                  `. `.--';: |:
                                   ;  `. Cc; Cc
                                   `.  ;  __
                                    `. `-'  ~\
                                     `-.__,--'~

                                     You put up a good fight but you die a gruesome death... Game over!
                ''')
    elif decision2 == 'wait':
        print("You decided to wait for a boat")
        time.sleep(5)
        print("5 seconds later...")
        time.sleep(1)
        print('''
                                   
                                       ..
                                     .(  )`-._
                                   .'  ||     `._
                                 .'    ||        `.
                              .'       ||          `._
                            .'        _||_            `-.
                         .'          |====|              `..
                       .'             \__/               (  )
                     ( )               ||          _      ||
                     /|\               ||       .-` \     ||
                   .' | '              ||   _.-'    |     ||
                  /   |\ \             || .'   `.__.'     ||   _.-..
                .'   /| `.            _.-'   _.-'       _.-.`-'`._`.`
                \  .' |  |        .-.`    `./      _.-`.    `._.-'
                 |.   |  `.   _.-'   `.   .'     .'  `._.`---`
                .'    |   |  :   `._..-'.'        `._..'  ||
               /      |   \  `-._.'    ||                 ||
              |     .'|`.  |           ||_.--.-._         ||
              '    /  |  \ \       __.--'\    `. :        ||
               \  .'  |   \|   ..-'   \   `._-._.'        ||
`.._            |/    |    `.  \  \    `._.-              ||
    `-.._       /     |      \  `-.'_.--'                 ||
         `-.._.'      |      |        | |         _ _ _  _'_ _ _ _ _
              `-.._   |      \        | |        |_|_|_'|_|_|_|_|_|_|
                  [`--^-..._.'        | |       /....../|  __   __  |
                   \`---.._|`--.._    | |      /....../ | |__| |__| |
                    \__  _ `-.._| `-._|_|_ _ _/_ _ _ /  | |__| |__| |
                     \   _o_   _`-._|_|_|_|_|_|_|_|_/   '-----------/
                      \_`.|.'  _  - .--.--.--.--.--.`--------------'
      .```-._ ``-.._   \__   _    _ '--'--'--'--'--'  - _ - _  __/
 .`-.```-._ ``-..__``.- `.      _     -  _  _  _ -    _-   _  __/(.``-._
 _.-` ``--..  ..    _.-` ``--..  .. .._ _. __ __ _ __ ..--.._ / .( _..``
`.-._  `._  `- `-._  .`-.```-._ ``-..__``.-  -._--.__---._--..-._`...```
   _.-` ``--..  ..  `.-._  `._  `- `-._ .-_. ._.- -._ --.._`` _.-``-.

    ''')
        time.sleep(2)
        decision3 = input("You arrive at the other side unharmed... There is a house with 3 doors. One red, one yellow "
                      "and one blue. Which color do you choose? \n").lower()
        if decision3 == 'blue':
            print('''                                ___.-----.______
                                           ___.-----'::::::::::::::::`---.___
                        _.--._            (:::;,-----'~~~~~`----::::::::::.. `-.
           _          .'_---. `--.__       `~~'                 `~`--.:::::`..  `..
          ; `-.____.-' ' {0} ` `--._`---.____                         `:::::::: : ::
         :_^              ~   `--.___ `----.__`----.____                ~::::::.`;':
          :`--.__,-----.___(         `---.___ `---.___  `----.___         ~|;:,' : |
           `-.___,---.____     _,        ._  `----.____ `----.__ `-----.___;--'  ; :
                          `---' `.  `._    `))  ,  , , `----.____.----.____   --' :|
                                / `,--.\    `.` `  ` ` ,   ,  ,     _.--   `-----'|'
         _.~~~~~~._____    __./'_/'     :   .:----.___ ` ` ` ``  .-'      , ,  :::'
                         ///--\;  ____  :   :'    ____`---.___.--::     , ` ` ::'
                         `'           _.'   (    /______     (   `-._   `-._,-'
            ()  ()                 .-' __.-//     /_______---'       `-._   `.
          * *(o)'      ~~~        /////    `'       ~~~~~~      ~~ ______;   ::.
          `\ )( /*                `'`'                            /_______   _.'
            {()}      ,     ~~~                  ~~~~~~~~           /___.---'  --__
             !|       `                                              ~~~
          ~~~~~~~~
         ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
             You get eaten by an alligator... Game over!
         ''')
        elif decision3 == 'red':
            print('''
                       (  .      )
                   )           (              )
                         .  '   .   '  .  '  .
                (    , )       (.   )  (   ',    )
                 .' ) ( . )    ,  ( ,     )   ( .
              ). , ( .   (  ) ( , ')  .' (  ,    )
             (_,) . ), ) _) _,')  (, ) '. )  ,. (' )
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                You get burned by fire... Game over!
            ''')
        elif decision3 == 'yellow':
            print('''
            *******************************************************************************
                      |                   |                  |                     |
             _________|________________.=""_;=.______________|_____________________|_______
            |                   |  ,-"_,=""     `"=.|                  |
            |___________________|__"=._o`"-._        `"=.______________|___________________
                      |                `"=._o`"=._      _`"=._                     |
             _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
            |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
            |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
                      |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
             _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
            |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
            |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
            ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
            /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
            ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
            /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
            ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
            /______/______/______/______/______/______/______/______/______/______/_____ /
            *******************************************************************************
                                 CONGRATULATIONS YOU FOUND THE TREASURE!
            ''')


