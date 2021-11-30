# Xoring-Chall

Created with ❤️ by **Odin's Triskele**

# Requirements install 

**Install python3**
```
 sudo apt-get update
 sudo apt-get install python3
```
# Syntax


Use `python3 xor.py encrypt/decrypt key input output`



# Descrierea proiectului



## Principiul operației XOR
#### În criptografie, cifrul XOR este un tip de cifru aditiv, care operează pe baza următoarelor reguli: 

```
A⨁0=A				

A⨁A=0				

A⨁B=B⨁A

(A⨁B)⨁C=A⨁(B⨁C)

(B⨁A)⨁A=B⨁0=B
```
 
######   Astfel, un șir poate fi codificat aplicând operația de adunare modulo 2 pe biți între caracterele șirului dat și o cheie dată. Pentru decriptare, reaplicarea operației XOR între caracterele codificate și cheie va rezulta în recuperarea textului inițial.  
######   Cifrul XOR oferă cel mai înalt grad de securitate când lungimea cheii este aceeași cu lungimea mesajului care trebuie criptat. În acest caz, este aproape imposibil ca un atacator să genereze și să testeze chei generate aleatoriu pentru a o găsi pe cea corectă. De aceea, cel puțin în teorie, această metodă face cifrul indescifrabil, căci pentru o cheie de lungime N, vor exista 2^N posibilități.


## Folosire generală

######   Datorită eficacității sale și a ușurinței de implementare, encriptarea XOR este adesea utilizată în algoritmi de criptare complecși folosiți în prezent. Este un exemplu clasic de criptare simetrică unde aceeași cheie e folosită atât pentru criptare, cât și pentru decriptare. Cu toate acestea, este la fel de dificil și să fie transmisă o parolă de lungime foarte mare în metode de siguranță. Mai mult, utilizarea repetată a unei aceleași chei pentru mai multe mesaje este supusă la atacuri bazate pe analiza frecvenței apariției unor caractere. O metodă de a rezolva această problemă este folosirea unei parole generate pseudo-aleator de la o parolă inițială pentru a obține un șir repetabil, dar greu-previzibil. În acest caz, doar partea din parolă folosită pentru generare este cea care trebuie cunoscută pentru decodarea șirului.
######    Din motivele anterior prezentate, este impractic să fie folosită encriptarea unor date folosind doar XOR, deși stă la baza majorității algoritmilor de encriptare simetrică: AES-256 (Advanced Encryption Standard), DES (Data Encryption Standard) etc.


## Spargerea unei criptări XOR

####  Cea mai rapidă modalitate de a sparge o astfel de criptare este următoarea(conform celor prezentate de Bruce Schneier în Applied Cryptography, second edition): 

###### 1. Determinăm lungimea cheii prin XOR-area mesajului criptat cu el însuși, shift-at pe un număr variabil de poziții, pentru a vedea câți biți rămân neschimbați. Dacă numărul de biți care sunt egali depășește un anumit procentaj din întreg mesajul (≥6%, număr care se numește indice de coincidență), înseamnă că am găsit un multiplu al numărului care reprezintă lungimea parolei.
###### 2. Shift-ăm textul cifrat cu un număr de poziții egal cu lungimea găsită anterior și aplicăm operația de XOR între șirul inițial și cel deplasat. Eliminăm astfel cheia și obținem doar textul care a fost criptat XOR-at cu același text shift-at cu lungimea cheii, de unde ar trebui să se poată determina conținutul mesajului.


## Cum funcționează codul propus?

###### 1. Pentru partea de encriptare, ideea principală este ca, pornind de la o parolă aleasă, să fie generat un șir aleator de lungimea inputului care trebuie codificat. Această generare se realizează cu pozițiile aleatoare ale caracterelor componente din parolă (obținute prin apelarea metodelor predefinite din clasa random). Acest lucru sporește securitatea, deoarece parola nu rămâne identică pe subșiruri de aceeași lungime ale textului din input, dar rămâne la fel pentru parte de decriptarea, căci, prin folosirea metodei random.seed(x) cu același parametru x, vom obține de fiecare dată aceeași secvență. Parametrul metodei îl alegem ca fiind suma codurilor ASCII aferente caracterelor componente din parolă, astfel că la parole diferite vom avea o altă regulă de generare a șirului care realizează codificarea. 

###### 2. Pentru decriptare, folosim din nou operația XOR dintre mesajul codificat și șirul generat pornind de la parola aleasă (care va fi la fel generat). 


# Echipa

## Acest proiect a fost realizat de echipa ***Odin's triskele*** , cu membrii componenți: 

#### Iliescu Gabriel Bogdan (grupa 132)                                         
#### Ghinea Dragoș Dumitru (grupa 132)
#### Andriciuc Andreea Cristina (grupa 132)

<img src="https://raw.githubusercontent.com/CoCodrilo1710/Xoring-Chall/main/logo.jpeg" width="200" height="400">

