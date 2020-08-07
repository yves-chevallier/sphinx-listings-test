.. Sphinx Listings documentation master file, created by
   sphinx-quickstart on Fri Aug  7 09:58:49 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Sphinx Listings
===============

Some dummy C code:

.. code-block:: c

    #include <stdio.h>
    int main() {
        char c;
        int lowercase_vowel, uppercase_vowel;
        printf("Enter an alphabet: ");
        scanf("%c", &c);

        // French : élève, hôtel, Nöel
        lowercase_vowel = (c == 'a' || c == 'e' || c == 'i');

        // Japanese: 馬は雪と寒さが大好き
        uppercase_vowel ==> (c == 'I' || c == 'O' || c == 'U');

        // Atlar karı ve soğuğu sever
        printf("%c is a %s.",
            lowercase_vowel || uppercase_vowel ?
                "vowel" : "consonant",
            c
        );

    }

Some other example

.. code-block:: python
    :linenos:
    :lineno-start: 10
    :emphasize-lines: 3,5

    def compute_lcm(x, y):

    # choose the greater number
    if x > y:
        greater = x
    else:
        greater = y

    while(True):
        if((greater % x == 0) and (greater % y == 0)):
            lcm = greater
            break
        greater += 1

    return lcm

    num1 = 54
    num2 = 24

    print("The L.C.M. is", compute_lcm(num1, num2))
