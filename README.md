# Xoring-Chall

Created with ❤️ by **Odin's Triskele**

# Echipa

## Acest proiect a fost realizat de echipa ***Odin's triskele*** , cu membrii componenți: 

#### ```Iliescu Gabriel Bogdan (grupa 132)        ```                                 
####                 ```Ghinea Dragoș Dumitru (grupa 132)    ```  
#### ```Andriciuc Andreea Cristina (grupa 132)```

# Requirements install 

**Install python3**
```
 sudo apt-get update
 sudo apt-get install python3
```
# Syntax


Use `python3 xor.py encrypt/decrypt key input output`


# Rezolvarea Cerintelor
####  `Parola folosita de echipa UnoZero este kI0peBcROjz78 `


#### 
#### 

### Cerinta 1

#### Pentru prima cerinta in care ni se permite folosirea inputului cat si a outputului am decis sa xoram direct, intrucat codul adversarilor pastreaza literele parolei in ordine, astfel am obtinut un text alcatuit doar din repetarea parolei folosite.


### Cerinta 2

#### Determinăm lungimea cheii prin XOR-area mesajului criptat cu el însuși, shift-at pe un număr variabil de poziții, pentru a vedea câți biți rămân neschimbați. Dacă numărul de biți care sunt egali depășește un anumit procentaj din întreg mesajul (≥8%, număr care se numește indice de coincidență), înseamnă că am găsit un multiplu al numărului care reprezintă lungimea parolei. Construim cheile caracter cu caracter, bazându-ne pe faptul ca cel mai frecvent caracter care se întâlnește în texte de dimensiuni mari este spațiul, cu codul ASCII 32. Componentele cheii sunt, de fapt, ce rezultă din XOR-area caracterului cel mai frecvent din subsiruri ale textului inițial de lungimea cheii și caracterul ” ”.

### ** Sintaxa script-ului cerinta2.py **

Use `python3 cerinta2.py outputadvers inputrecuperat.txt `  

```
outputadvers = fisierul care trebuie decryptat

inputrecuperat= fisierul unde va fi pus textul initial
```

##### Parola folosita pentru cryptare va fi afisata in consola.
